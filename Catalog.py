from book import Book
from NewWindow import DeleteWindow
import tkinter as tk
from tkinter.simpledialog import askstring, askfloat, Dialog
from tkinter import messagebox

def read_books():
  return books

def getBook():
  # add code to verify strings are actual values
  isbn = askstring('Adding a book', 'Input book ISBN:')
  title = askstring('Adding a book', 'Input books title:')
  author_first_name = askstring("Adding a book", "Input Authors First Name: ")
  author_last_name = askstring('Adding a book', "Input Authors Last Name: ")
  price = askfloat('Adding a book', "Input Books price: ")
  book = Book(isbn, title, author_first_name, author_last_name, price)
  books.append(book)

def sortBooks(books):
  books.sort(key=lambda x: x.price)
  info = ''
  index = 0
  for item in books:
    info = info + str(books[index])
    info = info + "\n\n"
    index = index + 1
  messagebox.showinfo("info", info)

def searchTitle(books):
  titlex = askstring("Find book by title", "Input title of book:").lower()
  info = ''
  book_lower = []
  index = 0
  for book in books:
    book_lower.append(str(books[index]).lower())
    index = index + 1
  
  for x in book_lower:
    if titlex in x:
      index = book_lower.index(x)
      info = info + str(books[index])
      info = info + "\n\n"
  if info == '':
    info = "Book not found"
  messagebox.showinfo("Books found", info)

def findIsbn():
  isbnx = askstring("Find book to delete bv ISBN", "Input ISBN of book:")
  book = []
  info = 'f'
  for x in books:
    if isbnx == x.isbn:
      book.append(x)
      info = x
  if info == 'f':
    info = "Book not found"
    messagebox.showinfo("Books Found", info)
  else:
    return book

def convertStr(book):
  book = book
  info = ""
  for x in book:
    info = info + str(x.isbn) + "\n" + str(x.title) + "\n" + str(x.author_last_name) + str(x.author_first_name) + "\n" + str(x.price)
  return info

def convertList(book):
  book = book
  info = ""
  for x in book:
    info = info + str(x)
    info = info + "\n\n"
  return info

def deleteBook(index):
  index = index
  for x in books:
    if index[0].isbn == x.isbn:
      books.remove(x)

def displayBooks(info):
  info = info
  messagebox.showinfo("Books Found", info)
  

def __init__(root):
    root = root
    def exit_application():
      msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                        icon='warning')
      if msg_box == 'yes':
        root.quit()
        return True
      else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')
    
    choice = askstring('Book Catalog', '''\t--Holmesglen Book Store--\t
    
    1. Add a book
    2. Sort and dsiplay book
    3. Search for a book by title
    4. Delete a book
    5. Display all books
    6. Exit
    
    Enter menu choice''')

    while choice:
      if choice == '1':
        print('1')
        getBook()
      elif choice == '2':
        print('2')
        sortBooks(books)
      elif choice == "3":
        print("3")
        searchTitle(books)
      elif choice == "4":
        print("4")
        book = findIsbn()
        if book != None:
          info = convertStr(book)
          delete = 'null'
          delete = DeleteWindow(root, info)
          if delete.info == 'null':
            messagebox.showinfo("Book not Deleted", "Book was not deleted")
          else:
            deleteBook(book)
            messagebox.showinfo("Book Deleted", "Book was successfully deleted")
      elif choice == "5":
        print("5")
        info = convertList(books)
        displayBooks(info)
      elif choice == '6':
        print("6")
        close = False
        close = exit_application()
        if close == True:
          break        
      else:
        messagebox.showinfo("error", "Not a valid selection, Please try again")
      choice = askstring('Book Catalog', '''--Holmesglen Book Store--
    
    1. Add a book
    2. Sort and dsiplay book
    3. Search for a book by title
    4. Delete a book
    5. Display all books
    6. Exit

    Enter menu choice''')

  # def new_Window(self, _class):
  #   self.new = tk.Toplevel(self.parent)
  #   _class(self.new)

books = []
book1 = Book("0553296981", "The Diary of a Young Girl", "Frank", "Anne", 16.50)
book2 = Book("1400082773", "Dreams from My Father", "Obama", "Barrack", 24.99)
book3 = Book("1400082773", "Dreams from My Father", "Obama", "Barrack", 18.8)
books.append(book1)
books.append(book2)
books.append(book3)

root = tk.Tk()
root.withdraw()
__init__(root)
