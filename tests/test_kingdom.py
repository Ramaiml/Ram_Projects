import unittest

from objects.kingdom import Kingdom
from objects.message import Message

class TestKingdom(unittest.TestCase):
    def setUp(self):
        self.kingdom = Kingdom('Kingdom Foo', 'Sun')
        self.possible_ally = Kingdom('Kingdom Bar', 'Moon')
        self.possible_ally2 = Kingdom('Kingdom Foobar', 'Star')

    def test_ally_addition(self):
        message = Message('moon', self.kingdom, self.possible_ally)
        self.kingdom.send_ally_invite(message)
        self.assertIn(self.possible_ally, self.kingdom.allies)

    def test_duplicate_ally_addition(self):
        """Duplicates should be neglected."""
        message = Message('moon', self.kingdom, self.possible_ally)
        self.kingdom.send_ally_invite(message)
        self.kingdom.send_ally_invite(message)
        self.assertIn(self.possible_ally, self.kingdom.allies)
        self.assertEqual(len(self.kingdom.allies), 1)

    def test_allies_clearance(self):
        message = Message('moon', self.kingdom, self.possible_ally)
        message2 = Message('star', self.kingdom, self.possible_ally2)
        self.kingdom.send_ally_invite(message)
        self.kingdom.send_ally_invite(message2)
        self.assertIn(self.possible_ally, self.kingdom.allies)
        self.assertIn(self.possible_ally2, self.kingdom.allies)
        self.kingdom.clear_allies()
        self.assertNotIn(self.possible_ally, self.kingdom.allies)
        self.assertNotIn(self.possible_ally2, self.kingdom.allies)
