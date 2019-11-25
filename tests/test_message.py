import unittest

from objects.kingdom import Kingdom
from objects.message import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.sender = Kingdom('Kingdom Foo', 'Sun')
        self.recepient = Kingdom('Kingdom Bar', 'Moon')

    def test_ally_addition_on_valid_content(self):
        content = 'iMiOiOiN'
        message = Message(content, self.sender, self.recepient)
        self.assertTrue(message.is_valid())

    def test_ally_addition_on_invalid_content(self):
        content = 'iMiOiN'
        message = Message(content, self.sender, self.recepient)
        self.assertFalse(message.is_valid())
