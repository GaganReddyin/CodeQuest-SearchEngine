import os
import shutil

# Specify the source folder path
source_folder = "questionContent/"

# Specify the destination folder path
destination_folder = 'QData/'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get a list of text files in the source folder
text_files = [file for file in os.listdir(source_folder) if file.endswith('.txt')]

# Create folders and move files
for i, file in enumerate(text_files, start=1):
    folder_name = str(i)
    folder_path = os.path.join(destination_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(source_folder, file)
    shutil.move(file_path, folder_path)

print("Files moved successfully into separate folders!")
