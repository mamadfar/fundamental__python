import subprocess
from pathlib import Path

root = Path(__file__).parent

try:
    # completed = subprocess.run(
    #     ["ls", "-l"], capture_output=True, text=True, check=True)
    # completed = subprocess.run(
    #     ["false"], capture_output=True, text=True, check=True)
    completed = subprocess.run(
        ["python", root / "other.py"], capture_output=True, text=True, check=True)
    print("Command executed successfully")
    print("args: ", completed.args)
    print("returncode: ", completed.returncode)
    print("stderr: ", completed.stderr)
    print("stdout: ", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
