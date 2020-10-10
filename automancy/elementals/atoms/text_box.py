""" ./atoms/text_box.py """
from automancy.core import Elemental
from automancy.decorators.interaction import interaction


class TextBox(Elemental):
    """ Atom Elemental for textbox form DOM objects """
    def __init__(self, locator: str, human_name: str, system_name: str, text: str = ''):
        """
        A TextBox object differs from a TextInput object in that TextBoxes are of
        the multi-line form input variety.

        Notes:
            The optional "text" parameter is meant to store a sting value to be written
            at a later time after instantiation.

        Args:
            locator (str): xpath string for the lookup
            human_name (str): human-readable name
            system_name (str): system-readable name

        """
        super().__init__(locator, human_name, system_name)
        self.__text = text

    @property
    def text(self) -> str:
        """
        Override for the Elemental base class .text property because
        we don't want TextInput form elements to use the base class
        getter to override the value that we define as the input value.

        Returns:
            (str) Value to be entered into the text input form element.

        """
        if not self.__text:
            return super().text

        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value

    @interaction
    def write(self, text: str = ''):
        """
        Writes text to the input field from the self.text property if the optional
        text argument isn't set.

        Notes:
            Proxy for sending keys to an element.

        Args:
            text (str): Optional, a specific string value that could be written to
            the input field.

        Returns:
            None

        """
        if not text:
            text = self.text

        self.element().send_keys(text)
