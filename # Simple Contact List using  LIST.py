# Simple Contact List using Python list

contacts = []  # List to store contacts as strings "name: phone"

# Function to add a contact
def add_contact(name, phone):
    contacts.append(f"{name}: {phone}")

# Function to search contacts one by one (linear search)
def search_contact(query):
    for contact in contacts:
        if query.lower() in contact.lower():
            return f"Found: {contact}"
    return "Not found"

# Example usage
add_contact("abhijeeet", "9109451807")
add_contact("anurag", "9876543210")

# Search example
query = "abhijeeet"
result = search_contact(query)
print(result)