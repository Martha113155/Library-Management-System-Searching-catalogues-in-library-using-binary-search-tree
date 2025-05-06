# Library Management System using Binary Search Tree
# This system implements a book catalogue with search functionality

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class LibraryCatalogue:
    def __init__(self):
        self.root = None

    def insert(self, book):
        """Insert a book into the BST based on title"""
        if not self.root:
            self.root = BSTNode(book)
        else:
            self._insert_recursive(self.root, book)

    def _insert_recursive(self, node, book):
        """Helper method for recursive insertion"""
        if book.title.lower() < node.book.title.lower():
            if node.left is None:
                node.left = BSTNode(book)
            else:
                self._insert_recursive(node.left, book)
        else:
            if node.right is None:
                node.right = BSTNode(book)
            else:
                self._insert_recursive(node.right, book)

    def search(self, title):
        """Search for a book by title"""
        return self._search_recursive(self.root, title.lower())

    def _search_recursive(self, node, title):
        """Helper method for recursive search"""
        if node is None or node.book.title.lower() == title:
            return node

        if title < node.book.title.lower():
            return self._search_recursive(node.left, title)
        return self._search_recursive(node.right, title)

    def inorder_traversal(self):
        """Display all books in sorted order"""
        books = []
        self._inorder_recursive(self.root, books)
        return books

    def _inorder_recursive(self, node, books):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, books)
            books.append(node.book)
            self._inorder_recursive(node.right, books)


def main():
    # Create library catalogue
    catalogue = LibraryCatalogue()

    # Add sample books
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
        Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789"),
        Book("1984", "George Orwell", "978-0451524935"),
        Book("Pride and Prejudice", "Jane Austen", "978-0141439518"),
        Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769488")
    ]

    for book in books:
        catalogue.insert(book)

    while True:
        print("\nLibrary Management System")
        print("1. Search for a book")
        print("2. Display all books")
        print("3. Exit")
        try:
            choice = input("Enter your choice (1-3): ")
        except EOFError:
            print("Input terminated. Exiting system...")
            break

        if choice == "1":
            try:
                title = input("Enter book title to search: ")
                result = catalogue.search(title)
                if result:
                    print("Book found:", result.book)
                else:
                    print("Book not found")
            except EOFError:
                print("Input terminated. Continuing...")
                continue

        elif choice == "2":
            books = catalogue.inorder_traversal()
            print("\nAll Books in Catalogue:")
            for book in books:
                print(book)

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()