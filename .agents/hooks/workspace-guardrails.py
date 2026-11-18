"""
Antigravity PreToolUse Hook: Workspace Guardrails.
Protege data/raw/, bloqueia comandos git destrutivos, impede caminhos absolutos
e bloqueia fallbacks aleatorios em scripts de tratamento/analise.
"""

import json
import re
import sys

GIT_DENY = [
    (re.compile(r"\bgit\s+reset\s+--hard\b"), "git reset --hard descarta alteracoes irreversivelmente."),
    (re.compile(r"\bgit\s+clean\b.*(-f|--force)"), "git clean -f remove arquivos nao rastreados (incluindo dados)."),
    (re.compile(r"\bgit\s+push\b.*(\s-f\b|--force\b)"), "git push --force sobrescreve o historico remoto."),
]

HARDCODED_PATH = re.compile(r"([A-Za-z]:\\\\Users\\\\|/Users/|/home/)")
FALLBACK_RANDOM = re.compile(r"\b(np\.random|random\.|Faker\()")


def reply(decision: str, reason: str = "") -> None:
    out = {"decision": decision}
    if reason:
        out["reason"] = reason
    print(json.dumps(out))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_call = payload.get("toolCall", {}) or {}
    name = tool_call.get("name", "")
    args = tool_call.get("args", {}) or {}

    if name == "run_command":
        cmd = args.get("CommandLine", "") or ""
        for pat, msg in GIT_DENY:
            if pat.search(cmd):
                reply("deny", f"Bloqueado por workspace-guardrails: {msg}")
                return 0
        reply("allow")
        return 0

    if name in ("write_file", "edit_file"):
        path = (args.get("Path", "") or "").replace("\\", "/")
        if "/data/raw/" in path:
            reply("deny", "Bloqueado: data/raw/ e READ-ONLY. Salve dados tratados em data/intermediate/ ou data/processed/.")
            return 0

        content = args.get("Content", "") or args.get("Replacement", "") or ""
        if path.endswith((".py", ".R", ".do", ".qmd")) and HARDCODED_PATH.search(content):
            reply("deny", "Bloqueado: caminho absoluto de maquina detectado no codigo. Use caminhos relativos para portabilidade (DCAS).")
            return 0

        if any(seg in path for seg in ("/2_data_treatment/", "/3_exploratory_analysis/", "/4_econometric_analysis/", "/5_robustness_checks/")):
            if FALLBACK_RANDOM.search(content):
                reply("deny", "Bloqueado: geracao aleatoria (np.random/random) proibida fora de 1_data_collection/ ou simulacoes.")
                return 0

    reply("allow")
    return 0


if __name__ == "__main__":
    main()
