"""
Cleanup file for Intermediate Exercises
"""

import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            old_name_path = os.path.join(directory_name, filename)
            new_name_path = os.path.join(directory_name, new_name)
            os.rename(old_name_path, new_name_path)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_")
    word = ''
    for i,letter in enumerate(new_name):
        if new_name[i].isupper() and new_name[i-1].islower() and i > 0:
            word = word + '_' + new_name[i]
        else:
            word = word + new_name[i]
    new_name = word
    parts = new_name.split('_')
    new_name = '_'.join(parts).title()
    new_name = new_name.replace(".Txt", ".txt")
    return new_name


main()
