import os
import shlex

def get_folders_from_user():
    return shlex.split(input("Please provide list of folders separated by spaces: "))

def list_files_in_folder(folder):
    """Try to list files in a folder. Handle if folder is invalid."""
    if not os.path.isdir(folder):
        print(f"Please provide a valid folder name, looks like the folder '{folder}' does not exist.")
        return

    print(f"\n ======== Listing of Files for the Folder - {folder} ========")
    try:
        files = os.listdir(folder)
        for file in files:
            print(file)
    except Exception as e:
        print(f"⚠️ Error accessing '{folder}': {e}")

def main():
    folders = get_folders_from_user()
    for folder in folders:
        list_files_in_folder(folder)

if __name__ == "__main__":
    main()
