import argparse
import os

DEFAULT_NAME = 'django_project'
BLACKLIST_DIRS = ['.git', 'migrations', '__pycache__', '.idea']
BLACKLIST_FILES = ['.DS_Store', 'db.sqlite3']

THIS_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# helper functions
def skip(string, skip_list):
    # truthy if one of BLACKLIST_STRS in the string
    return sum([s in string for s in skip_list])


def rename(directory, old, new):
    for root, dirs, files in os.walk(directory, topdown=False):
        if skip(root, BLACKLIST_DIRS):
            continue
        print(root, dirs, files, '\n\n')

        # Alter files first
        for file in files:
            if skip(file, BLACKLIST_FILES):
                continue
            print(file)
            full_old_path = os.path.join(root, file)
            with open(full_old_path, 'r',  encoding='utf-8') as f:
                text = f.read().replace(old, new)

            with open(full_new_path, 'w', encoding='utf-8') as f:
                f.write(text)

            full_new_path = os.path.join(root, file.replace(old, new))
            os.rename(full_old_path, full_new_path)

        os.rename(root, root.replace(old, new))


def main():
    parser = argparse.ArgumentParser(
        description='Rename the protect. Renames files and replaces references in files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument('-o', '--old', action='store', type=str, default=DEFAULT_NAME,
                        help=f'Specify old name with --old=old Default: {DEFAULT_NAME}', dest='old')

    parser.add_argument('-n', '--new', action='store', type=str, default=DEFAULT_NAME,
                        help=f'Specify new name with --new=new Default: {DEFAULT_NAME}', dest='new')

    parser.add_argument('-d', '--directory', action='store', type=str, default=THIS_DIR,
                        help=f'Specify directory to alter with --directory=directory Default: {THIS_DIR}',
                        dest='directory')


rename(THIS_DIR, 'test_123', 'django_project')
