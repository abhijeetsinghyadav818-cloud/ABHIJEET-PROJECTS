movies = []

def display_menu():
    print("\nMovie List Manager")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. Update a movie")
    print("4. List all movies")
    print("5. Exit")

def add_movie():
    movie = input("Enter the movie name to add:'avatar',bahubali,kgf,sholay: ")
    movies.append(movie)
    print(f"'{movie}' added to the list.")

def remove_movie():
    movie = input("Enter the movie name to remove: ")
    if movie in movies:
        movies.remove(movie)
        print(f"'{movie}' removed from the list.")
    else:
        print(f"'{movie}' not found in the list.")

def update_movie():
    try:
        index = int(input("Enter the index of the movie to update (starting from 0): "))
        if 0 <= index < len(movies):
            new_movie = input("Enter the new movie name: ")
            old_movie = movies[index]
            movies[index] = new_movie
            print(f"'{old_movie}' updated to '{new_movie}'.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def list_movies():
    if movies:
        print("Your favorite movies:")
        for i, movie in enumerate(movies):
            print(f"{i}. {movie}")
    else:
        print("No movies in the list.")

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_movie()
    elif choice == '2':
        remove_movie()
    elif choice == '3':
        update_movie()
    elif choice == '4':
        list_movies()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.") 