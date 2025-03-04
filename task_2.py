from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO, handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ])
logger = logging.getLogger(__name__)
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year
        
    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.year})'

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass
    
    @abstractmethod
    def show_books(self) -> None:
        pass

class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []
        
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f"Book '{title}' removed.")
                return
        logger.info(f"Book '{title}' not found.")
        
    def show_books(self) -> None:
        if not self.books:
            logger.info("Library is empty.")
        for book in self.books:
            logger.info(str(book))

class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        if not year.isdigit():
            logger.info("Invalid year. Please enter a numeric value.")
            return
        
        year_int: int = int(year)
        if year_int < 1900 or year_int > 2025:
            logger.info("Invalid year. Please enter a realistic year (e.g., between 1900 and 2025).")
            return
        
        book = Book(title, author, year_int)
        self.library.add_book(book)
        logger.info(f"Book '{title}' added.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
