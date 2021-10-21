""" ./core/tactical_asserts.py """
from time import sleep

import chronomancy
import inspect

from automancy.core import Elemental

from selenium.common.exceptions import WebDriverException


class TacticalAsserts(object):
    def __init__(self, sleep_time: float = 0.25, max_timeout: int = 10):
        super().__init__()
        self.max_timeout = max_timeout
        self.sleep_time = sleep_time
        self.timeout_count = 0
        self.sleep = sleep

    @staticmethod
    def __verify_is_elemental(element):
        if not issubclass(element.__class__, Elemental):
            raise TypeError('Input element must be a subclass of Elemental, found: {}'.format(type(element)))

    def becomes_interactable(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        self.gains_existence(element)
        self.gains_visibility(element)
        self.gains_clickability(element)
        return element

    def becomes_true(self, element: Elemental) -> Elemental:
        """
        Tactically asserts the `Elemental` passed in will become `True` within the time expected.

        Args:
            element (Elemental): an Automancy `Elemental` object able to be resolved to `True` or `False`

        Returns:
            Elemental: The same Elemental object which was passed in.

        """
        calling_frame = inspect.stack()[1]

        while self.timeout_count < self.max_timeout:
            try:
                assert element is True
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                element = chronomancy.arcane_recall(calling_frame)
                self.timeout_count += self.sleep_time

        raise AssertionError(f'Assertion Error: The element named {element.name} did not become True within {self.max_timeout} seconds')

    def gains_clickability(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeout:
            try:
                assert element.clickable
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError('Assertion Error: The element named "{}" did not gain clickability within the timeout limit ({} seconds)'.format(element.name, self.max_timeout))

    def gains_existence(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeout:
            try:
                assert element.exists
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError('Assertion Error: The element named "{}" did not come into existence within the timeout limit ({} seconds)'.format(element.name, self.max_timeout))

    def gains_visibility(self, element: Elemental) -> Elemental:
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeout:
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

        raise AssertionError('Assertion Error: The element named "{}" did not gain visibility within the timeout limit ({} seconds)'.format(element.name, self.max_timeout))

    def text_becomes_equal(self, element: Elemental, expected_text: str) -> Elemental:
        """
        Tactically asserts the value of the `.text` property for the passed in Elemental will become equal to the expected text.

        Args:
            element (Elemental): the `Elemental` which `.text` will be inspected for
            expected_text (str): the string you expect to match element.text

        Returns:
            Elemental: The same Elemental object which was passed in.

        """
        while self.timeout_count < self.max_timeout:
            try:
                assert element.text == expected_text
                self.timeout_count = 0
                return element
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError(f'Assertion Error: Target elements\' text did not become equal to the expected text within {self.max_timeout} seconds, {element} != {expected_text}')

    def text_becomes_found_in(self, element: Elemental, expected_text: str) -> Elemental:
        """

        Args:
            element ():
            expected_text ():

        Returns:

        """
        sleep_time = 0.25
        timeout = 0

        while timeout < self.max_timeout:
            try:
                assert expected_text in element.text
                return element
            except AssertionError:
                sleep(sleep_time)
                timeout += sleep_time

        raise AssertionError(f'Assertion Error: The expected text was not found within the text of the element named ({element.name}) text within {self.max_timeout} seconds.  {expected_text} not in {element.text}')

    def video_begins_playing(self, element):
        self.__verify_is_elemental(element)
        while self.timeout_count < self.max_timeout:
            try:
                assert element.is_playing()
                return element
            except AssertionError:
                sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError('Assertion Error: Video did not begin playing within {} seconds'.format(self.max_timeout * self.sleep_time))
