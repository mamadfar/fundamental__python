from pathlib import Path
import csv

parent = Path(__file__).parent

# with open(parent / "data.csv", "w") as file:
# * it should be file, not a path object, so we can't use Path
# writer = csv.writer(file)
# * Way 1
# writer.writerows([
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ])
# * Way 2
# writer.writerow(["Name", "Age", "City"])
# writer.writerow(["Alice", 30, "New York"])
# writer.writerow(["Bob", 25, "Los Angeles"])
# writer.writerow(["Charlie", 35, "Chicago"])


with open(parent / "data.csv") as file:
    reader = csv.reader(file)
    # * We can not iterate over the reader multiple times
    # print([item for item in list(reader) if item])
    for row in reader:
        print(row)
