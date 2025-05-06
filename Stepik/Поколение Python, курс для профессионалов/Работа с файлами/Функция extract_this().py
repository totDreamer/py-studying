from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as z_file:
        if len(args) == 0:
            z_file.extractall()
        else:
            for f in args:
                z_file.extract(f)
