from constants import *
from objects.kingdom import Kingdom
from objects.universe import Universe
from objects.message import Message
from objects.election import Election
from objects.conquest import Conquest

class Controller:
    """Controls the Tame of Thrones!"""

    def __init__(self):
        self._kingdom_names_and_emblems = [
            [SPACE, GORILLA],
            [LAND, PANDA],
            [WATER, OCTOPUS],
            [ICE, MAMMOTH],
            [AIR, OWL],
            [FIRE, DRAGON]
        ]
        self.kingdoms = { name: Kingdom(name, emblem)
            for [name, emblem] in self._kingdom_names_and_emblems }
        self.universe = Universe(list(self.kingdoms.values()))

    def _valid_candidate_names(self):
        return [kingdom_name_and_emblem[0] for kingdom_name_and_emblem
            in self._kingdom_names_and_emblems]

    def _get_candidates(self):
        candidate_names = set()
        while True:
            candidate_name = input("\nEnter a candidate ")
            if candidate_name.lower() in self._valid_candidate_names():
                candidate_names.add(candidate_name)
                choice = input("Input 1 to add another candidate ")
                if len(candidate_names) == 5 or choice != "1":
                    return [self.kingdoms[candidate_name] for candidate_name
                        in candidate_names]
            else:
                print("Invalid kingdom. Valid options are: {0}".format(
                    self._valid_candidate_names()))

    def _elect_ruler(self):
        candidates = self._get_candidates()
        Election(self.universe, candidates).execute()

    def _print_allies(self):
        print(",".join(
            [ally.name.capitalize()for ally in self.universe.ruler.allies]
        ) if self.universe.ruler and self.universe.ruler.allies else None)

    def _print_ruler(self):
        print(self.universe.ruler.name.capitalize() if self.universe.ruler
            else None)

    def _get_choice(self, query):
        print("\nPlease choose 1 of the below choices\n")
        print("1: Who is the ruler of Southeros?")
        print("2: Allies of Ruler?")
        print("3: {0}".format(query))
        print("4: Exit\n")
        return input("? ")

    def _help_conquer(self, kingdom):
        conquest = Conquest(self.universe, kingdom)
        conquest.conquer()

    def _execute(self, choice_query, logic_handler, *args):
        choice = self._get_choice(choice_query)
        if choice == "1":
            self._print_ruler()
        elif choice == "2":
            self._print_allies()
        elif choice == "3":
            logic_handler(*args)
        elif choice == "4":
            return
        else:
            print("Invalid choice")
        self._execute(choice_query, logic_handler, *args)

    def golden_crown(self):
        """Starts/continues an instance of Golden Crown."""
        self._execute("Input Messages to kingdoms from King Shan: ",
            self._help_conquer, self.kingdoms[SPACE]);

    def breaker_of_chains(self):
        """Starts/continues an instance of Breaker of Chains."""
        self._execute("Enter kingdoms competing to be the ruler: ",
            self._elect_ruler);
