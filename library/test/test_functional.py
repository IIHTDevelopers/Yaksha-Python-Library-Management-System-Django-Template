from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from library.models import Book, Author

class LibraryFunctionalTest(APITestCase):

    def test_create_author(self):
        """Test if an author is created successfully"""
        test_obj = TestUtils()
        try:
            author = Author.objects.create(name='J.K. Rowling', birth_date='1965-07-31')
            if author:
                test_obj.yakshaAssert("TestCreateAuthor", True, "functional")
                print("TestCreateAuthor = Passed")
            else:
                test_obj.yakshaAssert("TestCreateAuthor", False, "functional")
                print("TestCreateAuthor = Failed")
        except:
            test_obj.yakshaAssert("TestCreateAuthor", False, "functional")
            print("TestCreateAuthor = Failed")

    def test_create_book(self):
        """Test if a book is created successfully with an author"""
        test_obj = TestUtils()
        try:
            author = Author.objects.create(name="George Orwell", birth_date="1903-06-25")
            book = Book.objects.create(
                title="1984", author=author, published_date="1949-06-08", isbn="1234567890123", available_copies=5
            )
            if book:
                test_obj.yakshaAssert("TestCreateBook", True, "functional")
                print("TestCreateBook = Passed")
            else:
                test_obj.yakshaAssert("TestCreateBook", False, "functional")
                print("TestCreateBook = Failed")
        except:
            test_obj.yakshaAssert("TestCreateBook", False, "functional")
            print("TestCreateBook = Failed")

    def test_book_foreignkey_author(self):
        """Test if Book model correctly associates with Author via ForeignKey"""
        test_obj = TestUtils()
        try:
            author = Author.objects.create(name="Agatha Christie")
            book = Book.objects.create(title="Murder on the Orient Express", author=author, published_date="1934-01-01", isbn="9876543210123")
            if book.author == author:
                test_obj.yakshaAssert("TestBookForeignKeyToAuthor", True, "functional")
                print("TestBookForeignKeyToAuthor = Passed")
            else:
                test_obj.yakshaAssert("TestBookForeignKeyToAuthor", False, "functional")
                print("TestBookForeignKeyToAuthor = Failed")
        except:
            test_obj.yakshaAssert("TestBookForeignKeyToAuthor", False, "functional")
            print("TestBookForeignKeyToAuthor = Failed")
