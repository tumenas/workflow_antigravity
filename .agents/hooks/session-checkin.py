"""
Antigravity SessionStart Hook: Session Check-in.
Le quality_reports/session_logs/SESSION_STATE.md (se existir) e injeta no contexto.
"""

import json
import sys
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    cwd = payload.get("cwd") or "."
    state_file = Path(cwd) / "quality_reports" / "session_logs" / "SESSION_STATE.md"
    if not state_file.is_file():
        print(json.dumps({}))
        return 0

    try:
        text = state_file.read_text(encoding="utf-8", errors="replace").strip()
    except Exception:
        print(json.dumps({}))
        return 0

    if not text:
        print(json.dumps({}))
        return 0

    snippet = text[:1500]
    out = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": f"[Session Check-in] Estado anterior carregado de SESSION_STATE.md:\n{snippet}"
                }
            }
        ]
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    main()
