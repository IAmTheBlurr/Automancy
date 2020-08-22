""" ./asserts/assert_core.py """
from time import sleep

from ..core import Elemental
from ..video.html5_player import HTML5Player

from selenium.common.exceptions import WebDriverException


class TacticalAsserts(object):
    def __init__(self, sleep_time: float = 0.25, max_timeouts: int = 10):
        super().__init__()
        self.max_timeouts = max_timeouts
        self.sleep_time = sleep_time
        self.timeout_count = 0
        self.sleep = sleep

    @staticmethod
    def __verify_is_elemental(element):
        if not issubclass(element.__class__, Elemental):
            raise TypeError(f'Input element must be a subclass of Elemental, found: {type(element)}')

    def becomes_interactable(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        self.gains_existence(element)
        self.gains_visibility(element)
        self.gains_clickability(element)
        return element

    def gains_clickability(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeouts:
            try:
                assert element.clickable
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError(f'Assertion Error: The element named "{element.name}" did not gain clickability within the timeout limit ({self.max_timeouts} seconds)')

    def gains_existence(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeouts:
            try:
                assert element.exists
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError(f'Assertion Error: The element named "{element.name}" did not come into existence within the timeout limit ({self.max_timeouts} seconds)')

    def gains_visibility(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeouts:
            try:
                assert element.visible
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time
            except WebDriverException:
                # In some rare edge cases Selenium will raise this exception without a message.
                # In all use cases this has been due to the element not existing even if it has
                # already been detected to exist (through the element.exists property).  This is
                # a double check for existence a repeat of asserting that the element is visible.
                self.gains_existence(element)
                assert element.visible
                self.timeout_count = 0
                return element

        raise AssertionError(f'Assertion Error: The element named "{element.name}" did not gain visibility within the timeout limit ({self.max_timeouts} seconds)')

    def video_begins_playing(self, element: HTML5Player) -> HTML5Player:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeouts:
            try:
                assert element.is_playing()
                return element
            except AssertionError:
                sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError(f'Assertion Error: Video did not begin playing within {self.max_timeouts * self.sleep_time} seconds')
