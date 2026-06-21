from pathlib import Path
import sys

# Ensure project root is on sys.path so tests can import top-level modules
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
