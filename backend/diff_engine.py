import subprocess

def apply(diff):
    with open("patch.diff","w") as f:
        f.write(diff)
    subprocess.run(["git","apply","patch.diff"])
