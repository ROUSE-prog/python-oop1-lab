#!/usr/bin/env python3

class Book:
    """
    Represents a book with a title and page count.
    """

    def __init__(self, title, page_count):
        """
        Initialize a new Book instance.
        """
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """
        Getter for page_count.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Validates that page_count is an integer.
        """
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """
        Simulates turning a page in the book.
        """
        print("Flipping the page...wow, you read fast!")