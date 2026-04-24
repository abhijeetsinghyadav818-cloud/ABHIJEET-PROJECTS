def show_menu():
    print("\nShopping List Manager")
    print("1. View items")
    print("2. Add item")
    print("3. Delete item")
    print("4. Quit")


def view_items(items):
    if not items:
        print("No items in the shopping list.")
        return
    print("Shopping list:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


def add_item(items):
    item = input("Enter product name to add: ").strip()
    if item:
        items.append(item)
        print(f"Added '{item}'.")
    else:
        print("No product entered.")


def delete_item(items):
    if not items:
        print("Shopping list is empty.")
        return
    view_items(items)
    choice = input("Enter item number or name to delete: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(items):
            removed = items.pop(index)
            print(f"Removed '{removed}'.")
            return
    else:
        if choice in items:
            items.remove(choice)
            print(f"Removed '{choice}'.")
            return
    print("Item not found.")


def main():
    shopping_list = []
    while True:
        show_menu()
        selection = input("Choose an option: ").strip()
        if selection == "1":
            view_items(shopping_list)
        elif selection == "2":
            add_item(shopping_list)
        elif selection == "3":
            delete_item(shopping_list)
        elif selection == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
