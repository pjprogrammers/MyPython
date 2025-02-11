
import os

def bulk_rename_files(directory, new_name):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for count, filename in enumerate(os.listdir(directory)):
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        
        # Construct the new file name
        new_filename = f"{new_name}{count + 1}{ext}"
        
        # Get the full paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} to {new_file}")

# Example usage
directory_path = "/path/to/your/directory"
new_base_name = "new_name"
bulk_rename_files(directory_path, new_base_name)

## ( DOCUMENTATION: )

#Explanation:
        #Importing os Module: This module provides a way to interact with the operating system.
        #Function Definition: bulk_rename_files(directory, new_name) takes two arguments: the directory containing the files and the new base name for the files.
        #Directory Check: Ensures the specified directory exists.
        #Iterate Over Files: Loops through each file in the directory.
        #Split Filename and Extension: Uses os.path.splitext() to separate the file name from its extension.
        #Construct New Filename: Combines the new base name with an incremented counter and the original file extension.
        #Rename Files: Uses os.rename() to rename each file.
#Usage:
        #Replace "/path/to/your/directory" with the path to your directory.
        #Replace "new_name" with the desired base name for the files.
        #This script will rename all files in the specified directory to new_name_1.ext, new_name_2.ext, etc., while preserving their original extensions.


#Purpose of os.path.splitext():
        #os.path.splitext(filename) is a function in Python that splits a filename into two parts:
        #
        #The base name (everything before the file extension).
        #The extension (everything after the last dot . in the filename, including the dot itself)

#How Python assigns count and filename:
        #The enumerate() function returns a tuple for each element in the list:
        #The first item of the tuple is the index (the counter), which gets assigned to count.
        #The second item of the tuple is the actual element (the filename), which gets assigned to filename.