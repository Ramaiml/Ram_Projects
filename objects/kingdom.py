class Kingdom:
    """Defines a Kingdom.

    :param name: Name of the kingdom
    :param emblem: Emblem of the kingdom
    :type name: str
    :type emblem: str
    """

    def __init__(self, name, emblem):
        self.name = name
        self.emblem = emblem
        self._allies = set()

    def send_ally_invite(self, message):
        """Sents an ally invite to another kingdom.

        The particular kingdom is added as an ally given the message is valid.

        :param message: Message to be sent
        :type message: Message
        """
        if message.is_valid():
            self._allies.add(message.recepient)

    def clear_allies(self):
        """Clears kingdom's ally list."""
        self._allies = set()

    @property
    def allies(self):
        """Returns the list of allies of the kingdom.

        :return: The list of allies
        :rtype: list of Kingdom
        """
        return self._allies
