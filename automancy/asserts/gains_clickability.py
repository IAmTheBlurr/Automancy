from .assert_core import AssertCore


class GainsClickability(AssertCore):
    def __init__(self, element):
        super().__init__(element)
        AssertCore.verify_is_elemental_subclass(element)
        self()

    def __call__(self, *args, **kwargs):
        while self.timeout_count < self.max_timeouts:
            try:
                self.assertTrue(self.element.clickable)
                return self
            except AssertionError:
                self.sleep(self.sleep_time)
                self.timeout_count += self.sleep_time

        raise AssertionError(
            'Assertion Error: The element named "{0}" did not gain clickability within the timeout limit ({1} seconds)'.format(
                self.element.name, self.max_timeouts))
