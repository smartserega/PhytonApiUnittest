import unittest

import requests


class TestUrl1(unittest.TestCase):

    # Testing url № 1 '/'
    def testUrl1Positive(self):
        response = requests.get('http://localhost:6000/')
        self.assertEqual(({'key': 'value'}), response.json())
        self.assertEqual((200), response.status_code)

    def testUrl1Negative(self):
        response = requests.get('http://localhost:6000/1')
        self.assertEqual((404), response.status_code)


class TestUrl2(unittest.TestCase):

    # Testing url № 2 '/user/<username>'
    def testUrl2Positive(self):
        response = requests.get('http://localhost:6000/user/<username>')
        self.assertEqual(({'User': '<username>'}), response.json())

    def testUrl2Negative(self):
        response = requests.get('http://localhost:6000/use/<usernae>')
        self.assertEqual((404), response.status_code)


class TestUrl3(unittest.TestCase):

    # Testing url № 3 '/post/<int: post id>'
    def testUrl3Positive(self):
        response = requests.get('http://0.0.0.0:6000/post/0')
        self.assertEqual(({'post': 0}), response.json())
        self.assertEqual((200), response.status_code)

    def testUrl3Negative(self):
        response = requests.get('http://0.0.0.0:6000/post/text')
        self.assertEqual((404), response.status_code)



