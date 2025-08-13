
from pathlib import Path
from zipfile import ZipFile

parent = Path(__file__).parent

# * Way 1 to create a zip file
with ZipFile(parent / "files.zip", "w") as zip:
    for path in Path("modules").rglob("*.*"):
        zip.write(path)

# * Way 2 to create a zip file
# try:
#     zip = ZipFile("files2.zip", "w")
#     for path in Path("modules").rglob("*.*"):
#         zip.write(path)
#     zip.close()
# except Exception as e:
#     print(f"An error occurred: {e}")

with ZipFile(parent / "files.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("modules/modules.py")
    print(info.file_size)
    print(info.compress_size)
    print(info.filename)
    zip.extractall(parent / "extracted_files")
