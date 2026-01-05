from re import sub, IGNORECASE


def normalize_jpeg(filename):
    return sub(r".jpeg$|.jpg$", r".jpg", filename, flags=IGNORECASE)


print(normalize_jpeg("stepik.jPeG"))
print(normalize_jpeg("mountains.JPG"))
print(normalize_jpeg("windows11.jpg"))
print(normalize_jpeg("stepik.jPeG.JPEG"))
