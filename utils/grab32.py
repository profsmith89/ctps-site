### utils/grab32.py
"""
This script works within the cs50.dev world and grabs the CS32 GitHub
repo files for a book chapter or a programming problem set.

For example, if you wanted the book files for Chapter 4, you'd run
this script as follows:

$ python3 grab32.py chap04

The input parameter (i.e., `chap04` in this example) should match the
name of a public CS32 GitHub repo.  The script will place the chapter's
files from the book's GitHub repository in a subdirectory of the user's
current codespace.  The subdirectory is given the same name as the
GitHub repo (i.e., `chap04` in the example).

If a subdirectory of the same name already exists in the current
codespace, this script assumes that the user wants a new clean copy
of the repo's files.  It will name the clean copy `REPO_clean` (e.g.,
`chap04_clean`).
"""

import os
import re
import subprocess
import sys
import zipfile

# Global constants and configuration parameters
ORG_URL = 'https://github.com/seas-cs32/'
MAIN_ZIP_PATH = '/archive/refs/heads/main.zip'
CODESPACES_ROOT = '/workspaces'

def determine_working_dir():
    """Finds and returns the root directory of the user's codespace"""
    # Grab the current directory path
    cwd = os.getcwd()

    # If cwd is the root directory of a codespace, use it
    p = CODESPACES_ROOT + r'/\d+'
    if re.fullmatch(p, cwd):
        return cwd

    # If we get here, we're not in a codespace root directory so we'll
    # try to discover where it is and cd there. This begins by checking
    # that CODESPACES_ROOT exists.
    if not os.path.exists(CODESPACES_ROOT) or not os.path.isdir(CODESPACES_ROOT):
        sys.exit(f"ERROR: {CODESPACES_ROOT} doesn't exist")

    # Now list all non-hidden directories within CODESPACES_ROOT
    subdirs = [
        name for name in os.listdir(CODESPACES_ROOT)
        if os.path.isdir(os.path.join(CODESPACES_ROOT, name)) and name[0] != '.'
    ]

    # We know what to do if there is exactly one directory within CODESPACES_ROOT
    if len(subdirs) == 1:
        codespace_path = os.path.join(CODESPACES_ROOT, subdirs[0])

        # Jump to the root of the user's codespace directory
        try:
            os.chdir(codespace_path)
        except Exception as e:
            sys.exit(f"ERROR changing directory: {e}")

        return codespace_path
    
    # We need the user's help to find the right place to put the repo
    print('ERROR: Failed to find the root directory of your codespace.')
    print('ERROR: Please cd there and rerun this script.')
    sys.exit()


def my_rename(frompath, topath):
    """Rename a file or directory path from `frompath` to `topath`"""
    try:
        os.rename(frompath, topath)
    except FileNotFoundError:
        sys.exit(f"ERROR: the directory `{frompath}` does not exist")
    except FileExistsError:
        sys.exit(f"ERROR: a directory or file named `{topath}` already exists")
    except Exception as e:
        sys.exit(f"ERROR: {e}")


def main():
    # Check usage and grab the repo name
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 grab32.py REPO")

    repo = sys.argv[1]

    # Start alerting the user to our progress
    print(f"STARTING grabchapter.py ...")

    # Make sure the script is in a codespaces directory
    codespace_path = determine_working_dir()
    print(f"... Working in directory: {codespace_path}")

    # Create URL to a zipfile of the specified github repo
    url = ORG_URL + repo + MAIN_ZIP_PATH
    zip_fname = os.path.basename(url)

    # Download the repo's files (quietly)
    try:
        command = ['wget', url]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except Exception as e:
        sys.exit(f"ERROR executing wget command: {e}")
    print(f"... Zip file downloaded from: {url}")

    # Unzip the downloaded file
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_fname, 'r') as zip_ref:
            # Extract contents to the current directory
            zip_ref.extractall()
    except zipfile.BadZipFile:
        sys.exit(f"ERROR: {zip_fname} is not a valid ZIP file")
    except Exception as e:
        sys.exit(f"Error unzipping {zip_fname}: {e}")
    print(f"... Unzipped {zip_fname}")

    # Remove the downloaded zip file
    try:
        os.remove(zip_fname)
    except Exception as e:
        sys.exit(f"ERROR removing file {zip_fname}: {e}")
    print(f"... Removed {zip_fname}")

    # Rename the repo directory to remove the "-main" suffix,
    # but how we do this depends on whether the user is downloading
    # the repo for the first time or as another clean copy.
    if os.path.exists(repo):
        # Rename as a clean copy of repo
        my_rename(repo + '-main', repo + '_clean')
        print(f"... Renamed {repo}-main to {repo}_clean")
    else:
        # Straightforward rename
        my_rename(repo + '-main', repo)
        print(f"... Renamed {repo}-main to {repo}")

    # Alert the user to the fact we're done
    print(f"grabchapter.py COMPLETE")
    print()
    print(f"To run a script in {repo}, make sure to put yourself")
    print(f"in that directory by executing: cd {codespace_path}/{repo}")
    print()

if __name__ == '__main__':
    main()
