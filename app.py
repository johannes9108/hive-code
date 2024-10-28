def readProjectVersion():
    try:
        with open('version.txt', 'r') as file:
            return file.read().strip()
    except Exception:
        print("Error reading version file")

if __name__ == "__main__":
    print(readProjectVersion())