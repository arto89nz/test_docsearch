import os
import glob

def select_directory():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select Folder")
    return directory

def rename_files(directory):
    files = glob.glob(os.path.join(directory, '*'))
    for file_path in files:
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(directory, f"{file_name}.txt")
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_name} to {os.path.basename(new_file_path)}")

def main():
    # Step 1: Select the folder
    folder = select_directory()
    if not folder:
        print("No folder selected. Exiting...")
        return

    # Step 2: Rename the files by adding .txt extension
    rename_files(folder)

if __name__ == "__main__":
    main()
