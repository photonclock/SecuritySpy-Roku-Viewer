#!/usr/bin/env python3
import re
import os
import zipfile
import subprocess
import sys

# --- Configuration ---
MANIFEST_PATH = "manifest"
DIRS_TO_ZIP = ["components", "images", "source"]
FILES_TO_ZIP = ["manifest"]
# ---------------------

def check_clean_git_state():
    """Aborts if there are uncommitted changes in the repo."""
    # --porcelain gives machine-readable output. If empty, repo is clean.
    result = subprocess.run(
        ["git", "status", "--porcelain"], 
        capture_output=True, 
        text=True, 
        check=True
    )
    
    if result.stdout.strip():
        print("ERROR: Working directory is not clean.")
        print("You have uncommitted changes:")
        print(result.stdout)
        print("Please commit or stash your changes before releasing.")
        sys.exit(1)

def get_current_version(content):
    major = re.search(r'^major_version=(\d+)', content, re.MULTILINE).group(1)
    minor = re.search(r'^minor_version=(\d+)', content, re.MULTILINE).group(1)
    build = re.search(r'^build_version=(\d+)', content, re.MULTILINE).group(1)
    return int(major), int(minor), int(build)

def update_manifest():
    with open(MANIFEST_PATH, 'r') as f:
        content = f.read()

    major, minor, build = get_current_version(content)
    new_build = build + 1
    
    new_content = re.sub(
        r'^build_version=\d+',
        f'build_version={new_build}',
        content,
        flags=re.MULTILINE
    )

    with open(MANIFEST_PATH, 'w') as f:
        f.write(new_content)
        
    version_str = f"{major}.{minor}.{new_build}"
    print(f"[-] Version bumped: {major}.{minor}.{build} -> {version_str}")
    return version_str

def create_zip(version_str):
    zip_name = f"Security_Spy_Viewer_v{version_str}.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_TO_ZIP:
            zf.write(file)
        for directory in DIRS_TO_ZIP:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.startswith('.'): continue
                    file_path = os.path.join(root, file)
                    zf.write(file_path)
    
    print(f"[-] Created Artifact: {zip_name}")
    return zip_name

def git_commit_and_push(version_str):
    subprocess.run(["git", "add", MANIFEST_PATH], check=True)
    msg = f"Build Release v{version_str}"
    subprocess.run(["git", "commit", "-m", msg], check=True)
    print(f"[-] Git Commit completed: {msg}")
    print("[-] Pushing to remote...")
    subprocess.run(["git", "push"], check=True)

def create_github_release(version_str, zip_name):
    tag = f"v{version_str}"
    title = f"{tag} Release"
    notes = "release"
    
    cmd = [
        "gh", "release", "create", tag, zip_name,
        "--title", title,
        "--notes", notes
    ]
    
    print(f"[-] Creating GitHub Release {tag}...")
    subprocess.run(cmd, check=True)

def main():
    if not os.path.exists(MANIFEST_PATH):
        print(f"Error: {MANIFEST_PATH} not found.")
        sys.exit(1)

    try:
        # 0. Safety Check
        check_clean_git_state()

        # 1. Bump Version
        version_str = update_manifest()
        
        # 2. Generate ZIP
        zip_name = create_zip(version_str)
        
        # 3. Commit and Push
        git_commit_and_push(version_str)
        
        # 4. Create GitHub Release
        create_github_release(version_str, zip_name)
        
        print("\nSUCCESS: Release Published to GitHub.")
        
    except subprocess.CalledProcessError as e:
        print(f"\nFAILED: Subprocess error (Exit Code {e.returncode})")
        sys.exit(1)
    except Exception as e:
        print(f"\nFAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
