""" ./elementals/molecules/carousel.py """
from automancy.core import Elemental, Model


class Carousel(Elemental, Model):
    """ Organism Carousel used for elements that rotate images, videos, and other elements within it """
    def __init__(self, locator, human_name, system_name):
        """
        Notes:
            Generally has a "next" and "prev" arrow button to manually force a carousel to move to the next slide.

        Args:
            locator (str): xpath string for the lookup
            human_name (str): human-readable name
            system_name (str): system-readable name

        """
        Elemental.__init__(self, locator, human_name, system_name)
        Model.__init__(self)

        self.next_button = None
        self.prev_button = None
        self.current_slide = None
        self.num_of_slides = 0
        self.slide_shortcut_buttons = None
        self.shift_time = 0

    def next(self):
        self.next_button.click()

    def previous(self):
        self.prev_button.click()
