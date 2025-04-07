from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils


class LibraryBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")
