'''Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
'''

#start coding

class library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
     self.books.append(book)
     self.noBooks=len(self.books)
     
     
    def showInfo(self):
     print(f"The library has {self.noBooks} books. The books are")
     for book in self.books:
      print(book)


l1 = library()
l1.addBook("ram bai")
l1.addBook("the 5 am club")
l1.addBook("veer savarkar")
l1.showInfo()
          