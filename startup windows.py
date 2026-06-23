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