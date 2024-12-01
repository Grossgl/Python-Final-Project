from array import array
from book import Book
from member import Member
from datetime import date

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.book_ids = array('i')  # Using an array to store book IDs
    
    def add_book(self, book):
        self.books[book.isbn] = book
        self.book_ids.append(int(book.isbn))  # Adding the book's ISBN to the array

    # Originally tried to use the pop command to remove it, but that didn't work so I'm swapping it out for the del command
    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            self.book_ids.remove(int(isbn))
            print("Book", isbn, "has been removed from the array")
        else:
            print("Book not found")
    
    def add_member(self, member):
        self.members[member.member_id] = member

    # I pretty much did the same exact thing as remove book but member_id wasn't stored in an array like it
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member", member_id, "has been removed.")
        else:
            print("Member not found")
