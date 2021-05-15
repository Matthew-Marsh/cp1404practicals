""" Processes the files in the directory and sorts them into their appropriate folders. """
import shutil
import os


def main():
    """ Sort through the files in the directory and put them into their appropriate extension directories """
    os.chdir('FilesToSort')

    created_directories = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        parts = filename.split('.')
        extension = parts[-1]
        if extension not in created_directories:
            try:
                os.mkdir(extension)
            except FileExistsError:
                pass
            created_directories.append(extension)
        shutil.move(filename, extension + '/' + filename)


main()
