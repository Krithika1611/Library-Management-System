import csv
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to add a book to the library
def add_book():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()
    
    if book_id == "" or book_title == "" or book_author == "":
        messagebox.showerror("Error", "Please fill all the fields!")
        return

    try:
        with open("library.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and row[0] == book_id:
                    messagebox.showerror("Error", "Book already exists!")
                    return
    
        with open("library.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_title, book_author, "Yes", ""])  # "" is for customer_id
        
        messagebox.showinfo("Success", "Book added successfully!")
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search for a book
def search_book():
    search_value = search_entry.get()
    
    try:
        with open("library.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and search_value in row:
                    status = "Available" if row[3] == "Yes" else "Not Available"
                    messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}\nStatus: {status}")
                    search_entry.delete(0, END)
                    return
            messagebox.showerror("Error", "Book not found!")
            search_entry.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open the borrow window
def open_borrow_window():
    borrow_window = Toplevel(root)
    borrow_window.title("Borrow Book")
    borrow_window.geometry("300x200")

    Label(borrow_window, text="Book ID:").pack(pady=5)
    book_id_entry = Entry(borrow_window)
    book_id_entry.pack(pady=5)

    Label(borrow_window, text="Customer ID:").pack(pady=5)
    customer_id_entry = Entry(borrow_window)
    customer_id_entry.pack(pady=5)

    def borrow_book():
        book_id = book_id_entry.get()
        customer_id = customer_id_entry.get()

        try:
            rows = []
            book_found = False
            with open("library.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] == book_id:
                        book_found = True
                        if row[3] == "Yes":
                            row[3] = "No"  # Mark as borrowed
                            row[4] = customer_id  # Store customer_id
                            messagebox.showinfo("Success", "Book borrowed successfully!")
                        else:
                            messagebox.showerror("Error", "Book currently unavailable!")
                    rows.append(row)

            if book_found:
                with open("library.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

            borrow_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    Button(borrow_window, text="Borrow Book", command=borrow_book).pack(pady=10)

# Function to open the return window
def open_return_window():
    return_window = Toplevel(root)
    return_window.title("Return Book")
    return_window.geometry("300x200")

    Label(return_window, text="Book ID:").pack(pady=5)
    book_id_entry = Entry(return_window)
    book_id_entry.pack(pady=5)

    Label(return_window, text="Customer ID:").pack(pady=5)
    customer_id_entry = Entry(return_window)
    customer_id_entry.pack(pady=5)

    def return_book():
        book_id = book_id_entry.get()
        customer_id = customer_id_entry.get()

        try:
            rows = []
            book_found = False
            with open("library.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] == book_id:
                        book_found = True
                        if row[3] == "No" and row[4] == customer_id:  # Check customer_id
                            row[3] = "Yes"  # Mark as returned
                            row[4] = ""  # Clear customer_id
                            messagebox.showinfo("Success", "Book returned successfully!")
                        elif row[4] != customer_id:
                            messagebox.showerror("Error", "Incorrect customer ID!")
                        else:
                            messagebox.showerror("Error", "Book was not borrowed!")
                    rows.append(row)

            if book_found:
                with open("library.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

            return_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    Button(return_window, text="Return Book", command=return_book).pack(pady=10)

# Function to center the window
def center_window(window, width=400, height=300):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate the center position
    x = (screen_width//2 ) - (width//2 )
    y = (screen_height//2 ) - (height)//2
    # Set the window size and position
    window.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
root = Tk()
root.title("Library Management System")

# Load and resize the background image 
image = Image.open(r"E:\VSCODE\Library Managment System\pic.jpeg")
resized_image = image.resize((700, 500), Image.Resampling.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make the image cover the entire window

# Configure the grid layout for the root window
root.grid_rowconfigure(0, weight=0)  # No extra space needed for the title row
root.grid_rowconfigure(1, weight=1)  # The content frame will expand
root.grid_columnconfigure(0, weight=1)

# Add the title at the top center
title_label = Label(root, text="ABC LIBRARY", font=("Arial", 24, "bold"), bg="white")
title_label.grid(row=0, column=0, sticky="n", pady=10)

# Create a frame for the grid layout and place it in the second row
content_frame = Frame(root)
content_frame.grid(row=1, column=0)

# Configure the grid layout for the content frame
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1)
content_frame.grid_rowconfigure(2, weight=1)
content_frame.grid_rowconfigure(3, weight=1)
content_frame.grid_rowconfigure(4, weight=1)
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)

# Create the labels and entry boxes inside the content frame
Label(content_frame, text="Book ID:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
book_id_entry = Entry(content_frame)
book_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

Label(content_frame, text="Title:").grid(row=1, column=0, padx=10, pady=10, sticky=E)
book_title_entry = Entry(content_frame)
book_title_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

Label(content_frame, text="Author:").grid(row=2, column=0, padx=10, pady=10, sticky=E)
book_author_entry = Entry(content_frame)
book_author_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

Label(content_frame, text="Search:").grid(row=3, column=0, padx=10, pady=10, sticky=E)
search_entry = Entry(content_frame)
search_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# Create the buttons inside the content frame
add_button = Button(content_frame, text="Add Book", command=add_book)
add_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

search_button = Button(content_frame, text="Search Book", command=search_book)
search_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

borrow_button = Button(content_frame, text="Borrow Book", command=open_borrow_window)
borrow_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

return_button = Button(content_frame, text="Return Book", command=open_return_window)
return_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

center_window(root, width=500, height=500)
root.geometry("700x500")
root.mainloop()
