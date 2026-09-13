"""
Streamlit Cloud Entrypoint.
Executes app/main.py for India Image Eval platform.
"""

import os
import sys

# Ensure repository root is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

MAIN_PATH = os.path.join(BASE_DIR, "app", "main.py")
with open(MAIN_PATH, "r", encoding="utf-8") as f:
    code = f.read()

exec(compile(code, MAIN_PATH, "exec"), globals())
