import os
import sys
import subprocess
from pathlib import Path

def find_python_executable():
    root = Path(__file__).resolve().parent
    if sys.platform == "win32":
        venv_py = root / ".venv" / "Scripts" / "python.exe"
    else:
        venv_py = root / ".venv" / "bin" / "python"
    
    if venv_py.exists():
        return str(venv_py)
    return sys.executable

if __name__ == "__main__":
    py_exe = find_python_executable()
    cmd = [py_exe, "-m", "streamlit", "run", "app/main.py"]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        pass

