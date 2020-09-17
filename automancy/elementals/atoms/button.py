""" ./atoms/button.py"""
from automancy.core import Elemental


class Button(Elemental):
    """ Object model for a button web element """
    def __init__(self, locator: str, human_name: str, system_name: str):
        """
        Represents a basic button DOM element of any kind which could exist on a page.

        Args:
            locator (str): xpath string for the lookup
            human_name (str): human-readable name
            system_name (str): system-readable name

        """
        super().__init__(locator, human_name, system_name)
