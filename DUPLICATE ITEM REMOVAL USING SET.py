def remove_duplicates(items):
    """Return only unique values from the input list."""
    return list(set(items))


if __name__ == "__main__":
    raw = input("Enter items separated by commas: ")
    items = [item.strip() for item in raw.split(",") if item.strip()]
    unique_items = remove_duplicates(items)
    print("Unique items:", unique_items)
