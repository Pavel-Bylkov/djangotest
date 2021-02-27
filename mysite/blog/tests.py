from django.test import TestCase

from .models import Author


class AuthorTests(TestCase):
    """Author model tests."""

    def test_str(self):
        author = Author(name='John', email='john@god.com')
        self.assertEquals(
            str(author),
            'John',
        )
