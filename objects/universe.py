class Universe:
    """Defines a universe.

    A universe consists of it's kingdoms and the ruler.

    :param name: Name of the universe
    :param kingdoms: Kingdoms in the universe
    :type name: str
    :type kingdoms: list of Kingdom
    """

    def __init__(self, kingdoms):
        self.kingdoms = kingdoms
        self.ruler = None
