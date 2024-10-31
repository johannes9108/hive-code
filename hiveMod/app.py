import os

def readProjectVersion():
    # Determine the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to version.txt
    version_file_path = os.path.join(script_dir, '../data/version.txt')

    # Open and read the version file
    with open(version_file_path, 'r', encoding="UTF-8") as file:
        version = file.read().strip()
    return version
if __name__ == "__main__":
    print(readProjectVersion())
