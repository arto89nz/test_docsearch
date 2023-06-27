import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
import glob

# Configuration variables
SOURCE_DIRECTORY = ""  # Set the source directory path
DESTINATION_DIRECTORY = ""  # Set the destination directory path

def select_directory(prompt):
    root = Tk()
    root.withdraw()
    directory = askdirectory(title=prompt)
    return directory


def collect_files(directory):
    files = []
    for file_path in glob.glob(os.path.join(directory, '*')):
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


def copy_files(files, destination):
    for file_path in files:
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(destination, file_name)
        file_name_base, file_extension = os.path.splitext(file_name)

        counter = 1
        while os.path.exists(new_file_path):
            new_file_name = f"{file_name_base}_{counter}{file_extension}"
            new_file_path = os.path.join(destination, new_file_name)
            counter += 1

        shutil.copy(file_path, new_file_path)
        print(f"Copied {file_name} to {new_file_path}")


def main():
    # Step 1: Select the source directory
    if SOURCE_DIRECTORY == "":
        source_directory = select_directory("Select the source directory")
        if not source_directory:
            print("No source directory selected. Exiting...")
            return
    else:
        source_directory = SOURCE_DIRECTORY

    # Step 2: Collect the files from the source directory
    files = collect_files(source_directory)
    if not files:
        print("No files found in the source directory. Exiting...")
        return

    # Step 3: Select the destination folder
    if DESTINATION_DIRECTORY == "":
        destination = select_directory("Select the destination folder")
        if not destination:
            print("No destination folder selected. Exiting...")
            return
    else:
        destination = DESTINATION_DIRECTORY

    # Step 4: Copy the files to the destination folder as .txt files
    copy_files(files, destination)


if __name__ == "__main__":
    main()
