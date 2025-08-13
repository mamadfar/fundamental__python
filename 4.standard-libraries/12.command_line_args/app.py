
import sys

if len(sys.argv) == 1:
    print("USAGE")
    print("python app.py -n <name>")
    print("python app.py -h")
else:
    if sys.argv[1] == '-n':
        name = sys.argv[2] if len(sys.argv) > 2 else 'Guest'
        print(f"Hello, {name}!")
    elif sys.argv[1] == '-h':
        print("Help: This script greets the user.")
        print("Options:")
        print(" -n <name>   Greet the user with the specified name.")
        print(" -h          Show this help message.")
