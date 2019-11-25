from objects.message import Message

class Conquest:
    """Defines a conquest of a universe by a Kingdom.

    :param universe: Universe to be conquered
    :param conquerer: Conquering kingdom
    :type universe: Universe
    :type conquerer: Kingdom
    """

    def __init__(self, universe, conquerer):
        self.universe = universe
        self.conquerer = conquerer
        conquerer_index = self.universe.kingdoms.index(self.conquerer)
        possible_allies_list = self.universe.kingdoms[:conquerer_index] + \
            self.universe.kingdoms[conquerer_index + 1:]
        self._possible_allies = { possible_ally.name: possible_ally
                                  for possible_ally in possible_allies_list }
        self._possible_allies_names = [ally.name for ally
                                       in possible_allies_list]

    def _get_messages(self):
        messages = []
        while True:
            recepient_name = input(
                "\nWhom do you want to send the message to? ")
            try:
                recepient = self._possible_allies[recepient_name.lower()]
                content = input("Enter the content: ")
                messages.append(Message(content, self.conquerer, recepient))
                choice = input("Input 1 to send another message ")
                if choice != "1":
                    return messages
            except KeyError:
                print("Invalid recepient. Valid options are: {0}".format(
                    self._possible_allies_names))

    def conquer(self):
        self.conquerer.clear_allies()
        self.universe.ruler = None
        messages = self._get_messages()
        for message in messages:
            self.conquerer.send_ally_invite(message)
        if len(self.conquerer.allies) >= 3:
            self.universe.ruler = self.conquerer
