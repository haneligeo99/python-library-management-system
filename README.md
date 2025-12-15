# 📚 Python CLI Library Management System

A full-featured command-line interface (CLI) application for managing a small library's book collection. This project demonstrates core Python Object-Oriented Programming (OOP) principles, data serialization, and complete CRUD operations.

## ✨ Project Features

This system goes beyond basic data handling by including:

* **Object-Oriented Design (OOP):** Uses two main classes, `Book` and `Library`, to encapsulate data and logic cleanly.
* **Data Persistence:** Uses the `pickle` module to serialize and save the entire list of `Book` objects to a file (`library_data.pkl`), ensuring data is preserved even after the application closes and restarts. 
* **Full CRUD Operations:** Includes methods for **C**reate, **R**ead, **U**pdate, and **D**elete functions.
* **Search Functionality:** Allows users to search the collection by Title or Author (case-insensitive).
* **Status Tracking:** Books track their availability via an `is_checked_out` boolean, which is updated by the Check Out and Return functions.

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Modules:** * `pickle`: Used for object serialization (saving/loading data).
    * `os`: Used for console utility (like clearing the screen).

## 🚀 How to Run the Application

### Prerequisites

You must have Python 3 installed on your system.

### Steps

1.  **Clone the Repository**
    Open your terminal and clone the project:
    ```bash
    git clone [https://github.com/](https://github.com/)<Your-GitHub-Username>/python-library-management-system.git
    cd python-library-management-system
    ```

2.  **Execute the Script**
    Run the main Python file directly:
    ```bash
    python3 library_system.py
    ```
    *(The system will automatically create a `library_data.pkl` file after the first run.)*

### Application Menu

The application provides the following options upon startup:
1.  Add New Book
2.  Display All Books
3.  Check Out Book (by ISBN)
4.  Return Book (by ISBN)
5.  Search Book (by Title/Author)
6.  Delete Book (by ISBN)
7.  Exit (Saves data before quitting)

## 💡 Future Enhancements

* **Error Handling:** Implement more robust input validation (e.g., ensuring ISBN is formatted correctly).
* **User Management:** Add a system for tracking user IDs and associating checked-out books with a specific borrower.
* **Sorting Options:** Allow users to display the collection sorted by Title, Author, or ISBN.

## 👤 Author

**Hannah George** - *Computer Science Major*

* **GitHub:** [[Link to your GitHub Profile](https://github.com/haneligeo99)]
* **LinkedIn:** [[Link to your LinkedIn Profile](www.linkedin.com/in/hannah-george-775a17188/)]
