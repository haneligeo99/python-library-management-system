import pickle
import os 
# We don't strictly need 'os' if we don't clear the console, but it's good practice
# and we'll keep it for utility.

# --- BOOK CLASS ---
class Book:
    """Represents a single book in the library with attributes like title, author, and availability."""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # Books are available by default
        
    def __str__(self):
        """Returns a human-readable string representation of the Book object."""
        status = " (Checked Out)" if self.is_checked_out else " (Available)"
        return f'"{self.title}" by {self.author} (ISBN: {self.isbn}){status}'

# --- LIBRARY CLASS ---
class Library:
    """Manages the collection of Book objects and provides methods for interaction."""
    
    def __init__(self):
        self.books = []
        
    # --- Persistence Methods ---
    def save_data(self):
        """Saves the current list of book objects to a file using pickle."""
        try:
            with open('library_data.pkl', 'wb') as f:
                pickle.dump(self.books, f)
        except Exception as e:
            print(f"\nERROR: Could not save data. {e}")
            
    def load_data(self):
        """Loads book objects from the save file and replaces the current book list."""
        try:
            with open('library_data.pkl', 'rb') as f:
                self.books = pickle.load(f)
            print("\nDATA: Library data loaded successfully.")
        except FileNotFoundError:
            print("\nNOTICE: No existing library data found. Starting fresh.")
        except Exception as e:
            print(f"\nERROR: Could not load data. {e}")
            
    # --- CRUD Methods ---
    def add_book(self, title, author, isbn):
        """Creates a new Book object and adds it to the library's collection."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"\nSUCCESS: Book '{title}' added to the library.")
        
    def display_all_books(self):
        """Prints the details of every book currently in the library."""
        if not self.books:
            print("\nThe library is currently empty.")
            return

        print("\n--- Current Library Collection ---")
        for i, book in enumerate(self.books):
            print(f"[{i+1}] {book}")
        print("----------------------------------")

    def check_out_book(self, isbn):
        """Finds a book by ISBN and marks it as checked out if available."""
        isbn = isbn.strip()
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f"\nSUCCESS: Book '{book.title}' has been checked out.")
                    return
                else:
                    print(f"\nNOTICE: Book '{book.title}' is already checked out.")
                    return
        print(f"\nERROR: Book with ISBN '{isbn}' not found in the library.")

    def return_book(self, isbn):
        """Finds a book by ISBN and marks it as available if checked out."""
        isbn = isbn.strip()
        for book in self.books:
            if book.isbn == isbn:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"\nSUCCESS: Book '{book.title}' has been returned and is now available.")
                    return
                else:
                    print(f"\nNOTICE: Book '{book.title}' was already available (not checked out).")
                    return
        print(f"\nERROR: Book with ISBN '{isbn}' not found in the library.")

    def search_book(self, query):
        """Searches for a book by title or author (case-insensitive)."""
        query = query.strip().lower()
        found_books = []
        
        for book in self.books:
            title_lower = book.title.lower()
            author_lower = book.author.lower()
            
            if query in title_lower or query in author_lower:
                found_books.append(book)

        if found_books:
            print(f"\n--- Found {len(found_books)} Book(s) matching '{query}' ---")
            for i, book in enumerate(found_books):
                print(f"[{i+1}] {book}")
            print("---------------------------------------------------------")
        else:
            print(f"\nNOTICE: No books found matching '{query}'.")
            
    def delete_book(self, isbn):
        """Removes a book from the collection using its ISBN."""
        isbn = isbn.strip()
        
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"\nSUCCESS: Book '{book.title}' (ISBN: {isbn}) has been deleted.")
                return 

        print(f"\nERROR: Book with ISBN '{isbn}' not found in the library. Nothing was deleted.")


# --- MAIN APPLICATION LOOP ---

def main():
    """Initializes the library, loads data, runs the loop, and saves data on exit."""
    
    my_library = Library()
    
    # 1. LOAD DATA AT STARTUP
    my_library.load_data() 
    
    # Optional: If the library is empty after loading, add some starter books for demonstration
    if not my_library.books:
        print("\nAdding initial demo books.")
        my_library.add_book("The Clean Coder", "Robert C. Martin", "978-0137081073")
        my_library.add_book("Python Crash Course", "Eric Matthes", "978-1593279288")
        
    while True:
        print("\n" + "="*40)
        print("  SIMPLE LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Check Out Book (by ISBN)")
        print("4. Return Book (by ISBN)")
        print("5. Search Book (by Title/Author)")
        print("6. Delete Book (by ISBN)")
        print("7. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN (e.g., 123-456): ")
            my_library.add_book(title, author, isbn)
            
        elif choice == '2':
            my_library.display_all_books() 
            
        elif choice == '3':
            isbn = input("Enter ISBN of book to check out: ")
            my_library.check_out_book(isbn)
            
        elif choice == '4':
            isbn = input("Enter ISBN of book to return: ")
            my_library.return_book(isbn)

        elif choice == '5':
            query = input("Enter title or author to search: ")
            my_library.search_book(query)
        
        elif choice == '6':
            isbn = input("Enter ISBN of book to delete: ")
            my_library.delete_book(isbn)
            
        elif choice == '7':
            # 2. SAVE DATA BEFORE EXIT
            my_library.save_data()
            print("\nThank you for using the Library System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()