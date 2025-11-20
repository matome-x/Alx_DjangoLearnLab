# Django Admin Setup for Book Model

## Objective
Configure the Django admin interface to manage the `Book` model and enhance the visibility and usability of book records.

---

## 1. Register the Book Model

In `bookshelf/admin.py`, add the following:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")
