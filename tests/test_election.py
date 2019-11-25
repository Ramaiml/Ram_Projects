import unittest

from objects.kingdom import Kingdom
from objects.universe import Universe
from objects.election import Election
from objects.message import Message

kingdoms_names_and_emblems = (
    ('test1', 'test1 emblem'),
    ('test2', 'test2 emblem'),
    ('test3', 'test3 emblem'),
    ('test4', 'test4 emblem'),
    ('test5', 'test5 emblem'),
    ('test6', 'test6 emblem'),
)

class TestElection(unittest.TestCase):
    def _get_messages_stub(self):
        return [Message(content, sender, recepient)
            for (content, sender, recepient)
            in (
                ('test3 emblem', self.candidates[0], self.universe.kingdoms[2]),
                ('test4 emblem', self.candidates[0], self.universe.kingdoms[3]),
                ('test5 emblem', self.candidates[0], self.universe.kingdoms[4]),
                ('test6 emblem', self.candidates[1], self.universe.kingdoms[5])
            )
        ]

    def setUp(self):
        self.kingdoms = [Kingdom(kingdom[0], kingdom[1])
                         for kingdom in kingdoms_names_and_emblems]
        self.universe = Universe(self.kingdoms)
        self.candidates = self.kingdoms[:2]
        Election._get_messages = self._get_messages_stub
        self.election = Election(self.universe, self.candidates)

    def test_execution(self):
        """Assigns the candidate with highest votes as the universe's ruler."""
        self.election.execute()
        self.assertEqual(self.universe.ruler, self.candidates[0])
