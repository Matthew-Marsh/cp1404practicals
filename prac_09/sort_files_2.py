""" Processes the files in the directory and sorts them into their appropriate folders. """
import shutil
import os


def main():
    """Sort through the files in the directory and put them into their appropriate extension directories."""
    os.chdir('FilesToSort')

    extensions = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        parts = filename.split('.')
        extension = parts[-1]
        if extension not in extensions:
            extensions.append(extension)

    extension_to_folder = get_extension_to_folder(extensions)
    for folder in extension_to_folder.values():
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
    move_files(extension_to_folder)


def get_extension_to_folder(extensions):
    """Gets the folder names that the user wants to sort files into."""
    extension_to_folder = {}
    for extension in extensions:
        extension_to_folder[extension] = input("What category would you like to sort {} files into? ".format(extension))
    return extension_to_folder


def move_files(extension_to_folder):
    """Moves files according to the user's choices in dictionary."""
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        parts = filename.split('.')
        extension = parts[-1]
        shutil.move(filename, extension_to_folder[extension] + '/' + filename)


main()
