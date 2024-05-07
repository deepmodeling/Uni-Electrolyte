import os
from pathlib import Path

VAR_ROOT = Path(os.getenv("VAR_ROOT", "var"))
VAR_ROOT.mkdir(parents=True, exist_ok=True)

SESSION_ROOT = VAR_ROOT / "sessions"
SESSION_ROOT.mkdir(parents=True, exist_ok=True)
UPLOAD_ROOT = SESSION_ROOT
