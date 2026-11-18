"""
Antigravity Stop Hook: Session Logger.
Registra arquivos modificados em quality_reports/session_logs/YYYY-MM-DD_auto.md.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    cwd = Path(payload.get("cwd") or ".")
    try:
        res = subprocess.run(
            ["git", "-C", str(cwd), "status", "--porcelain"],
            capture_output=True, text=True, timeout=5
        )
        status = res.stdout.strip() if res.returncode == 0 else ""
    except Exception:
        status = ""

    if not status:
        print(json.dumps({"decision": "allow"}))
        return 0

    logs_dir = cwd / "quality_reports" / "session_logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = logs_dir / f"{today}_auto.md"

    changed = [ln.strip() for ln in status.splitlines() if ln.strip()][:25]
    entry = [f"\n## {datetime.now().strftime('%H:%M')} — {len(changed)} arquivo(s) modificado(s)"]
    entry.extend(f"- `{ln}`" for ln in changed)

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("\n".join(entry) + "\n")
    except Exception:
        pass

    print(json.dumps({"decision": "allow"}))
    return 0


if __name__ == "__main__":
    main()
