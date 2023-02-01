class Book:
  def __init__(self, isbn, title, author_last_name, author_first_name, price):
    self.isbn = isbn
    self.title = title
    self.author_last_name = author_last_name
    self.author_first_name = author_first_name
    self.price = price
  
  def __str__(self):
    return f"{self.isbn} {self.title} {self.author_last_name}, {self.author_first_name} ${self.price:.2f}"
