import subprocess

def run_app():
    subprocess.run(["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "web_store.__main__:app"])

