""" ./asserts/video_begins_playing.py """
from time import sleep
from .assert_core import AssertCore

from ..video import HTML5Player


class VideoBeginsPlaying(AssertCore):
    def __init__(self, element: HTML5Player):
        super().__init__(element)

        if not isinstance(element, HTML5Player):
            raise TypeError('This assert class requires the input element to be type HTML5Element, found {}'.format(type(element)))

        self()

    def __call__(self, *args, **kwargs):
        while self.timeout_count < self.max_timeouts:
            try:
                self.assertTrue(self.element.is_playing())
                return self
            except AssertionError:
                sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError('Assertion Error: Video did not begin playing within {} seconds'.format(self.max_timeouts * self.sleep_time))
