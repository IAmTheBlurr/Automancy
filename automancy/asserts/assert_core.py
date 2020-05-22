""" ./asserts/assert_core.py """
import unittest


class AssertCore(unittest.TestCase()):
    def __init__(self, sleep_time, timeout_count, max_timeouts):
        self.sleep_time = sleep_time
        self.timeout_count = timeout_count
        self.max_timeouts = max_timeouts
