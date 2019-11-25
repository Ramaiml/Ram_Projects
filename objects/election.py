import random

from constants import MESSAGES
from objects.message import Message

class Election:
    """Defines an election in a universe.

    :param universe: Universe in which the election is happening
    :param candidates: Candidates competing in the election
    :type universe: Universe
    :type candidates: list of Kingdom
    """
    def __init__(self, universe, candidates):
        self.universe = universe
        self.candidates = candidates
        self._voters = [kingdom for kingdom in universe.kingdoms
            if kingdom not in candidates]

    def _get_messages(self):
        messages = [Message(random.choice(MESSAGES), candidate, voter)
            for candidate in self.candidates for voter in self._voters]
        random.shuffle(messages)
        return messages[:6]

    def execute(self, round=1, further_rounds=False):
        """Executes the election and assigns the winner as the universe's ruler.
        """
        if not further_rounds:
            for kingdom in self.universe.kingdoms:
                kingdom.clear_allies()

        messages = self._get_messages()
        for message in messages:
            message.sender.send_ally_invite(message)
        print("\nResults after round {0} ballot count".format(round))
        for candidate in self.candidates:
            print("\nAllies for {0}: {1}".format(
                candidate.name, [ally.name for ally in candidate.allies]))

        self.candidates.sort(key=lambda candidate: len(candidate.allies),
            reverse=True)
        winner_votes = len(self.candidates[0].allies)
        for index in range(1, len(self.candidates)):
            try:
                if len(self.candidates[index].allies) < winner_votes:
                    self.candidates.pop(index)
            except IndexError:
                pass
        if len(self.candidates) == 1:
            self.universe.ruler = self.candidates[0]
        else:
            self.execute(round + 1, True)
