""" ./asserts/assert_core.py """
import unittest

from time import sleep

from ..core import Elemental


class AssertCore(unittest.TestCase()):
    def __init__(self, element, sleep_time: float = 0.25, max_timeouts: int = 10):
        self.element = element
        self.max_timeouts = max_timeouts
        self.sleep_time = sleep_time
        self.timeout_count = 0
        self.sleep = sleep

    @staticmethod
    def verify_is_elemental(element):
        if not issubclass(element, Elemental):
            raise TypeError('Input element must be a subclass of Elemental, found: {}'.format(type(element)))
