class Message:
    """Defines a Message.

    :param content: Content of the message
    :param sender: Sender of the message
    :param recepient: Recepient of the message
    :type content: str
    :type sender: Kingdom
    :type recepient: Kingdom
    """

    def __init__(self, content, sender, recepient):
        self.content = content
        self.content_lower = self.content.lower()
        self.sender = sender
        self.recepient = recepient

    def _recepient_letters(self):
        return list(self.recepient.emblem.lower())

    def _remove_letter(self, letter):
        content_list = list(self.content_lower)
        content_list.remove(letter)
        self.content_lower = ''.join(content_list)

    def is_valid(self):
        """Returns if a message is valid or not."""
        for letter in self._recepient_letters():
            if letter not in self.content_lower:
                return False
            self._remove_letter(letter)
        return True
