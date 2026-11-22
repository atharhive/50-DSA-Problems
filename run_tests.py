"""Run every problem's assertions and print a summary.

Finds every solution.py anywhere in the repo (any level, any folder depth),
runs each one as a script, and reports PASS or FAIL.

Usage (from the repo root):
    python run_tests.py              # run everything
    python run_tests.py two-sum      # only paths containing "two-sum"
    python run_tests.py level-1      # only paths containing "level-1"

A problem passes when its script exits with code 0 (all assertions held).
The script exits with code 1 if any problem fails, so it works in CI too.
"""
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 30
SKIP_DIRS = {".git", ".github", "venv", ".venv", "env", "node_modules", "__pycache__"}


def discover(filter_text: str = "") -> List[Path]:
    """Return every solution.py in the repo, skipping tooling folders."""
    files = []
    for path in sorted(ROOT.rglob("solution.py")):
        relative = path.relative_to(ROOT)
        if SKIP_DIRS.intersection(relative.parts):
            continue
        if filter_text and filter_text not in relative.as_posix():
            continue
        files.append(path)
    return files


def run_one(path: Path) -> Tuple[bool, str]:
    """Run one solution file. Return (passed, error output)."""
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            cwd=path.parent,
        )
    except subprocess.TimeoutExpired:
        return False, f"Timed out after {TIMEOUT_SECONDS} seconds"
    return result.returncode == 0, result.stderr.strip()


def main() -> int:
    filter_text = sys.argv[1] if len(sys.argv) > 1 else ""
    files = discover(filter_text)

    if not files:
        print("No solution.py files found.")
        return 1

    failed: List[Tuple[str, str]] = []
    for path in files:
        name = path.parent.relative_to(ROOT).as_posix()
        passed, error = run_one(path)
        print(f"{'PASS' if passed else 'FAIL'} | {name}")
        if not passed:
            failed.append((name, error))

    print(f"\n{len(files) - len(failed)}/{len(files)} problems passed")

    for name, error in failed:
        print(f"\n--- {name} ---")
        print(error or "(no error output)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())