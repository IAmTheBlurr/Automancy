from selenium.common.exceptions import WebDriverException

from .assert_core import AssertCore
from .gains_existence import GainsExistence


class GainsVisibility(AssertCore):
    def __init__(self, element):
        super().__init__(element)
        AssertCore.verify_is_elemental_subclass(element)
        self()

    def __call__(self, *args, **kwargs):
        while self.timeout_count < self.max_timeouts:
            try:
                self.assertTrue(self.element.visible)
                return self
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time
            except WebDriverException:
                # In some rare edge cases Selenium will raise this exception without a message.
                # In all use cases this has been due to the element not existing even if it has
                # already been detected to exist (through the element.exists property).  This is
                # a double check for existence a repeat of asserting that the element is visible.
                GainsExistence(self.element)
                self.assertTrue(self.element.visible)
                return self.element

        raise AssertionError(
            'Assertion Error: The element named "{0}" did not gain visibility within the timeout limit ({1} seconds)'.format(
                self.element.name, self.max_timeouts))
