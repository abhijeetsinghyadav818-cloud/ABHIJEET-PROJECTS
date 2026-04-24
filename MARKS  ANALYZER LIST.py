
marks = []

# Input marks until -1 is entered
while True:
    mark = input("Enter a mark (or -1 to stop): ")
    if mark == '-1':
        break
    try:
        marks.append(int(mark))
    except ValueError:
        print("Invalid input, please enter a number.")

# Calculate min, max, average if list is not empty
if marks:
    minimum = min(marks)
    maximum = max(marks)
    average = sum(marks) / len(marks)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {average}")
else:
    print("No marks entered.")
