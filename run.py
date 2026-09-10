"""
Convenience launcher for the Josh Talks AI Evaluation Dashboard.
Usage: python run.py
"""
import sys
import subprocess

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app/main.py"])
