
# This code checks if the list name has any name starting with 'J' and prints it.
# If no name is found, it prints "No name found".
names = ["pohn", "pane", "Doe"]

found = False
for name in names:
    if name[0] == 'J':
        print(name)
        found = True
        break
if not found:
    print("No name found")
