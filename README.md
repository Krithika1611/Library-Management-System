# Library Management System

## Overview
This Library Management System is a simple desktop application built using Python and Tkinter. It allows users to add books, search for books, borrow books, and return books. The book data is stored in a CSV file (`library.csv`). The graphical interface is intuitive and provides all the necessary functionalities for basic library management.

---

## Features
1. **Add Book:**
   - Add new books to the library by entering the Book ID, Title, and Author.
   - Prevents duplicate Book IDs from being added.

2. **Search Book:**
   - Search for books by any keyword (e.g., Book ID, Title, Author).
   - Displays details of the book including its availability status.

3. **Borrow Book:**
   - Borrow books by providing the Book ID and Customer ID.
   - Marks the book as unavailable once borrowed.

4. **Return Book:**
   - Return borrowed books by providing the Book ID and Customer ID.
   - Marks the book as available and clears the Customer ID.

5. **Graphical User Interface (GUI):**
   - User-friendly interface built with Tkinter.
   - Includes entry fields, buttons, and message dialogs for interaction.

6. **Data Storage:**
   - All book data is stored in a CSV file (`library.csv`).
   - Fields include: `Book ID`, `Title`, `Author`, `Availability (Yes/No)`, and `Customer ID`.

7. **Background Image:**
   - A custom background image enhances the visual appeal.

---

## Prerequisites
1. **Python 3.x**
   - Ensure Python is installed on your system.

2. **Required Libraries:**
   - `tkinter` (pre-installed with Python)
   - `csv` (pre-installed with Python)
   - `Pillow` (for handling images)

   Install `Pillow` by running:
   ```bash
   pip install pillow
   ```

---

## Installation
1. Clone or download this project to your local machine.
2. Ensure that the `library.csv` file exists in the project directory. If not, create it manually with the following columns:
   ```csv
   Book ID,Title,Author,Availability,Customer ID
   ```
3. Place the background image (`pic.jpeg`) in the same directory as the script.

---

## Usage
1. Run the Python script:
   ```bash
   python library_management.py
   ```
2. Use the interface to perform various library operations:
   - **Add Book:** Enter Book ID, Title, and Author, then click the "Add Book" button.
   - **Search Book:** Enter a search term and click the "Search Book" button.
   - **Borrow Book:** Click the "Borrow Book" button, provide Book ID and Customer ID, and confirm borrowing.
   - **Return Book:** Click the "Return Book" button, provide Book ID and Customer ID, and confirm return.

---

## File Structure
- `library_management.py`: Main Python script for the application.
- `library.csv`: CSV file storing book data.
- `pic.jpeg`: Background image for the application.

---

## Notes
- Ensure unique Book IDs for proper functionality.
- The `Customer ID` is only required for borrowing and returning books.
- Handle the `library.csv` file carefully to avoid data corruption.
- Resize or replace the background image (`pic.jpeg`) as needed for better UI aesthetics.

---

## Future Improvements
1. Add user authentication for library staff and customers.
2. Enhance the UI with more modern styling (e.g., using `ttk` widgets or a web-based interface).
3. Implement additional features such as late fee calculations or book reservations.
4. Integrate a database (e.g., SQLite or MySQL) for better scalability.

---

## License
This project is open-source and free to use for educational and personal purposes. For commercial use, please contact the author.




