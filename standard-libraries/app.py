

#! Read, write, and copy files

# from pathlib import Path
# from time import ctime
# import shutil

# # path = Path("modules/ecommerce/__init__.py")

# # path.exists()
# # path.rename("init.txt")
# # path.unlink()  # Remove the file
# # print(path.stat())  # Get file status
# # print(ctime(path.stat().st_birthtime))  # Get file status

# # path.read_bytes()  # Read file as bytes
# # print(path.read_text())  # Read file as text

# # path.write_text("This is a new file.")  # Write text to the file
# # path.write_bytes(b"This is a new file in bytes.")  # Write bytes to the file

# src = Path("modules/ecommerce/__init__.py")
# target = Path() / "__init__.py"

# # * Way 1 to copy a file
# target.write_text(src.read_text())  # Copy content from src to target

# # * Way 2 to copy a file
# shutil.copy(src, target)  # Copy the file from src to target

#! find all Python files in a directory and its subdirectories
# from pathlib import Path

# path = Path("modules/ecommerce")

# # path.exists()
# # path.mkdir()
# # path.rmdir()  # Remove the directory if it is empty
# # path.rename("ecommerce_new")  # Rename the directory

# # print(path.iterdir())  # Iterate through all files and directories in the path

# paths = [p for p in path.iterdir() if p.is_dir()]
# # List all Python files in the directory
# # Recursively find all Python files equals to path.glob("**/*.py")
# py_files = [p for p in path.rglob("*.py")]

# print(py_files)

#! path of a file

# from pathlib import Path

# path = Path("modules/ecommerce/shopping/sales.py")
# path.exists()
# path.is_file()  # Check if the path exists and is a file
# path.is_dir()  # Check if the path exists and is a directory
# print(path.name)  # Get the name of the file
# print(path.stem)  # Get the name without the extension
# print(path.suffix)  # Get the file extension
# print(path.parent)  # Get the parent directory
# # Change the file name (without changing the real file, it's just a Path object)
# path = path.with_name("file.txt")
# print(path)
# print(path.absolute())
# path = path.with_suffix(".py")  # Change the file extension
# print(path)


# from pathlib import Path

# Path("C:\\Program Files\\Microsoft Office")
# Path(r"C:\Program Files\Microsoft Office")
# Path()  # Current working directory
# Path("modules/ecommerce/shopping/__init__.py")  # Relative path
# Path() / Path("modules/ecommerce/shopping/__init__.py")  # Absolute path
# Path() / "modules" / "ecommerce" / "shopping" / \
#     "__init__.py"  # Using division operator for path joining
# Path().home()  # Home directory
# Path().cwd()  # Current working directory
