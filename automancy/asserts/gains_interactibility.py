from .assert_core import AssertCore

from .gains_clickability import GainsClickability
from .gains_existence import GainsExistence
from .gains_visibility import GainsVisibility


class GainsInteractability(AssertCore):
    def __init__(self, element):
        super().__init__(element)
        AssertCore.verify_is_elemental_subclass(element)
        self()

    def __call__(self, *args, **kwargs):
        GainsExistence(self.element)
        GainsVisibility(self.element)
        GainsClickability(self.element)
        return self.element
