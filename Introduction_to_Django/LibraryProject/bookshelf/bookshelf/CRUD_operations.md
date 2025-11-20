# CRUD Operations Summary

This file documents the full set of CRUD operations performed on the `Book` model using the Django shell.

---

## 1. CREATE
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book