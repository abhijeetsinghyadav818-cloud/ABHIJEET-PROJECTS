def attendance_checker():
    present_students = set()

    print("Attendance Checker")
    print("Enter student names one by one. Type 'done' when finished.")

    while True:
        name = input("Student name: ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Please enter a valid name.")
            continue
        if name in present_students:
            print(f"{name} is already marked present.")
        else:
            present_students.add(name)
            print(f"Marked {name} present.")

    print("\nAttendance complete.")
    print(f"Total present students: {len(present_students)}")
    for student in sorted(present_students):
        print(student)


if __name__ == "__main__":
    attendance_checker()
