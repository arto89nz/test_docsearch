import os
import glob
import tkinter as tk
from tkinter import filedialog

def select_directory(title="Select Folder"):
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title=title)
    return directory

def check_file_extension(file_path, extension):
    _, file_ext = os.path.splitext(file_path)
    return file_ext == extension

def rename_file(file_path, new_extension):
    file_name, _ = os.path.splitext(file_path)
    new_file_path = file_name + new_extension
    os.rename(file_path, new_file_path)
    print(f"Renamed {file_path} to {new_file_path}")

def split_file(file_path, max_size, destination_directory):
    file_name = os.path.basename(file_path)
    file_name_base, file_extension = os.path.splitext(file_name)

    with open(file_path, 'rb') as file:
        index = 1
        while True:
            chunk = file.read(max_size)
            if not chunk:
                break

            new_file_name = f"{file_name_base}_{index}{file_extension}"
            new_file_path = os.path.join(destination_directory, new_file_name)
            with open(new_file_path, 'wb') as new_file:
                new_file.write(chunk)

            print(f"Split {file_name} into {new_file_name}")
            index += 1

    os.remove(file_path)
    print(f"Deleted {file_name}")

def process_files(source_directory, destination_directory, extension, max_size):
    files = glob.glob(os.path.join(source_directory, '*'))
    for file_path in files:
        if os.path.isfile(file_path):
            if not check_file_extension(file_path, extension):
                rename_file(file_path, extension)
            elif os.path.getsize(file_path) > max_size:
                split_file(file_path, max_size, destination_directory)

def main():
    # Step 1: Select the source folder
    source_folder = select_directory(title="Select Source Folder")
    if not source_folder:
        print("No source folder selected. Exiting...")
        return

    # Step 2: Select the destination folder
    destination_folder = select_directory(title="Select Destination Folder")
    if not destination_folder:
        print("No destination folder selected. Exiting...")
        return

    # Step 3: Set the file extension and maximum size
    file_extension = ".txt"
    max_size = 20 * 1024  # 20KB

    # Step 4: Process the files in the source folder
    process_files(source_folder, destination_folder, file_extension, max_size)

if __name__ == "__main__":
    main()
