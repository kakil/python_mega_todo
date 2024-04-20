import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/kakil/Dev/Python Projects/pyCharmProjects/app1_todo/bonus/compressed.zip",
                    "/Users/kakil/Dev/Python Projects/pyCharmProjects/app1_todo/bonus/files")