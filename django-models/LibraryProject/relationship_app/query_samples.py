import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation (run once)
def create_sample_data():
    # Authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    # Books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)

    # Libraries
    library1 = Library.objects.create(name="Central Library")
    library1.books.set([book1, book3])

    library2 = Library.objects.create(name="Community Library")
    library2.books.set([book2])

    # Librarians
    Librarian.objects.create(name="Alice", library=library1)
    Librarian.objects.create(name="Bob", library=library2)

# Query examples
def run_queries():
    # 1. Query all books by a specific author using objects.filter()
    author_name = "J.K. Rowling"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)

    # 2. List all books in a specific library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print("-", book.title)

    # 3. Retrieve the librarian for a library
    print(f"\nLibrarian for {library_name}:")
    print(library.librarian.name)

if __name__ == "__main__":
    # Uncomment this line the first time to create sample data
    # create_sample_data()
    run_queries()
