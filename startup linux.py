# Desafio do Desafio
# No laboratório o problema volta todo dia: sentou na máquina, abriu o VS Code, foi dar commit — e o Git
# ainda está com o colega anterior.
# Crie um segundo arquivo, na raiz do seu repositório no GitHub (mesmo nível de pastas como src/ ou
# README.md), com um nome pessoal e fácil de lembrar. Exemplo: sou_ignacio.py (use o seu nome).
# Esse script é o ritual de início de trabalho: toda vez que for programar naquele PC, rode-o antes de codar
# ou commitar. Ele deve configurar automaticamente o user.name e o user.email corretos para você — sem
# perguntar, com seus dados já definidos no código.

import subprocess
# ///
# subprocess.run(["git", "config", "--global", "user.name", '"GreenHat-0f0"'])
# subprocess.run(["git", "config", "--global", "user.email", '"kiara.paasrosa@gmail.com"'])

# print("Executado com sucesso")
# print()
# print("Seu usuário é:") 
# subprocess.run(["git", "config", "user.name"])
# print()
# print("Seu email é:")
# subprocess.run(["git", "config", "user.email"])
# \\\

#///
# subprocess.run(["git", "clone", "https://github.com/GreenHat-0f0/chicken_nugget.git", r"G:\Codes\nuggets"])
#\\\

import os
import subprocess
import sys

# Define your paths and repository URL
PARENT_DIR = r"G:\codes"
NEW_FOLDER_NAME = "nuggets2"  # <-- Change this to your desired folder name
REPO_URL = "https://github.com/GreenHat-0f0/chicken_nugget.git"  # <-- Replace with your URL

# Combine them into the final target path (e.g., G:\codes\my-new-project)
TARGET_DIR = os.path.join(PARENT_DIR, NEW_FOLDER_NAME)

def main():
    try:
        # 1. Create the new folder inside G:\codes
        # os.makedirs will automatically create G:\codes too if it doesn't exist yet
        print(f"Creating folder: {TARGET_DIR}")
        os.makedirs(TARGET_DIR, exist_ok=True)

        # 2. Run git clone directly inside the new folder using 'cwd'
        print(f"Cloning repository into: {TARGET_DIR}...")
        
        # check=True raises an error if git fails
        # shell=True helps Windows locate the 'git' command in your PATH
        subprocess.run(["git", "clone", REPO_URL, "."], cwd=TARGET_DIR, check=True, shell=True)
        
        print("\nSuccess! Folder created and repository cloned successfully.")

    except subprocess.CalledProcessError:
        print(f"\n[Error] Git clone failed. Verify your URL and ensure '{TARGET_DIR}' is completely empty.", file=sys.stderr)
    except PermissionError:
        print(f"\n[Error] Permission denied. Try running your terminal as Administrator.", file=sys.stderr)
    except Exception as e:
        print(f"\n[Unexpected Error] {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
