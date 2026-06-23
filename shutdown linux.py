import subprocess

subprocess.run(["git", "config", "--global", "--unset", "user.name"])
subprocess.run(["git", "config", "--global", "--unset", "user.email"])

subprocess.run(["rm", "-r", "/media/aluno/Um S Berto/Codes/nuggets"])