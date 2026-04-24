names = set()

while True:
    name = input("Enter a name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    names.add(name)

print("Unique names:", sorted(names))