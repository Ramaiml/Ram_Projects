import unittest

from objects.kingdom import Kingdom
from objects.universe import Universe
from objects.conquest import Conquest
from objects.message import Message

kingdoms_names_and_emblems = (
    ('test1', 'test1 emblem'),
    ('test2', 'test2 emblem'),
    ('test3', 'test3 emblem'),
    ('test4', 'test4 emblem')
)

class TestConquest(unittest.TestCase):
    def _get_adequate_messages(self):
        """returns 3 messages which makes the condition ">= 3" True"""
        return [Message(content, sender, recepient)
            for (content, sender, recepient)
            in (
                ('test2 emblem', self.conquerer, self.universe.kingdoms[1]),
                ('test3 emblem', self.conquerer, self.universe.kingdoms[2]),
                ('test4 emblem', self.conquerer, self.universe.kingdoms[3])
            )
        ]

    def _get_adequate_but_invalid_messages(self):
        """returns 3 messages in which 1 is invalid making the condition ">= 3" False"""
        return [Message(content, sender, recepient)
            for (content, sender, recepient)
            in (
                ('test2 emblem', self.conquerer, self.universe.kingdoms[1]),
                ('test3 emblem', self.conquerer, self.universe.kingdoms[2]),
                ('test3 emblem', self.conquerer, self.universe.kingdoms[3]) # Should have had 'test4 emblem' in content
            )
        ]

    def _get_inadequate_messages(self):
        """returns 2 messages which makes the condition ">= 3" False"""
        return [Message(content, sender, recepient)
            for (content, sender, recepient)
            in (
                ('test2 emblem', self.conquerer, self.universe.kingdoms[1]),
                ('test3 emblem', self.conquerer, self.universe.kingdoms[2]),
            )
        ]

    def setUp(self):
        self.kingdoms = [Kingdom(kingdom[0], kingdom[1])
                         for kingdom in kingdoms_names_and_emblems]
        self.universe = Universe(self.kingdoms)
        self.conquerer = self.kingdoms[0]

    def test_successful_conquest(self):
        Conquest._get_messages = self._get_adequate_messages
        conquest = Conquest(self.universe, self.conquerer)
        conquest.conquer()
        self.assertEqual(self.universe.ruler, self.conquerer)

    def test_unsuccessful_conquest_due_to_valid_messages(self):
        Conquest._get_messages = self._get_adequate_but_invalid_messages
        conquest = Conquest(self.universe, self.conquerer)
        conquest.conquer()
        self.assertNotEqual(self.universe.ruler, self.conquerer)

    def test_unsuccessful_conquest_due_to_insufficient_messages(self):
        Conquest._get_messages = self._get_inadequate_messages
        conquest = Conquest(self.universe, self.conquerer)
        conquest.conquer()
        self.assertNotEqual(self.universe.ruler, self.conquerer)
