
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.models import Author, Book
from library.test.TestUtils import TestUtils

class LibraryExceptionalTest(APITestCase):

    def test_isbn_unique_constraint(self):
        """Test if ISBN is unique for each book"""
        test_obj = TestUtils()
        try:
            author = Author.objects.create(name="Harper Lee")
            Book.objects.create(title="To Kill a Mockingbird", author=author, published_date="1960-07-11", isbn="1111111111111")
            duplicate_book = None
            try:
                duplicate_book = Book.objects.create(title="Different Book", author=author, published_date="1960-07-11", isbn="1111111111111")
            except:
                pass  # Expected failure
            if duplicate_book is None:
                test_obj.yakshaAssert("TestISBNUniqueConstraint", True, "exceptional")
                print("TestISBNUniqueConstraint = Passed")
            else:
                test_obj.yakshaAssert("TestISBNUniqueConstraint", False, "exceptional")
                print("TestISBNUniqueConstraint = Failed")
        except:
            test_obj.yakshaAssert("TestISBNUniqueConstraint", False, "exceptional")
            print("TestISBNUniqueConstraint = Failed")

    def test_negative_available_copies(self):
        """Test if available_copies cannot be negative"""
        test_obj = TestUtils()
        try:
            author = Author.objects.create(name="Stephen King")
            invalid_book = None
            try:
                invalid_book = Book.objects.create(title="IT", author=author, published_date="1986-09-15", isbn="2222222222222", available_copies=-5)
            except:
                pass  # Expected failure
            if invalid_book is None:
                test_obj.yakshaAssert("TestNegativeAvailableCopies", True, "exceptional")
                print("TestNegativeAvailableCopies = Passed")
            else:
                test_obj.yakshaAssert("TestNegativeAvailableCopies", False, "exceptional")
                print("TestNegativeAvailableCopies = Failed")
        except:
            test_obj.yakshaAssert("TestNegativeAvailableCopies", False, "exceptional")
            print("TestNegativeAvailableCopies = Failed")
