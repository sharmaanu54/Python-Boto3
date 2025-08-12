import os
import shlex

folders = shlex.split(input("Please provide list of folders separated by spaces :"))
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like the folder "+ folder + " does not exist")               
        continue
    print("\n ======== Listing of Files for the Folder - " + folder + " ========")
    
    for file in files:
        print(file)