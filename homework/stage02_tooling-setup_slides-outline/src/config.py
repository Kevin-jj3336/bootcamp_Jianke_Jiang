import sys, os
from pathlib import Path
from typing import Optional

try:
    import numpy as np
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise


def load_env() -> None:
    load_dotenv()
    print(".env loaded (if present)")


def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


# Project paths
PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"

print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)