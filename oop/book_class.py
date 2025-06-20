# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging/re-creation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (for testing purposes):
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))      # Expected: 1984 by George Orwell, published in 1949
    print(repr(book1))     # Expected: Book('1984', 'George Orwell', 1949)

    del book1              # Expected: Deleting 1984
