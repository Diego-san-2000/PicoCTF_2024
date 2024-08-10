import os

def rename_extensions():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Iterate over all files in the given directory
    for filename in os.listdir(script_dir):
        # Check if the file has the .PNG extension (uppercase)
        if filename.endswith('.PNG'):
            # Create the new filename with the extension in lowercase
            new_filename = filename[:-4] + '.png'
            # Create full paths for the old and new filenames
            old_file = os.path.join(script_dir, filename)
            new_file = os.path.join(script_dir, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} to {new_filename}')

# Call the function to rename the extensions
rename_extensions()
