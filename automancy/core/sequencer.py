from selenium.common.exceptions import ElementNotInteractableException


class Sequencer(object):
    def __init__(self, *args):
        """
        :param args: Any number of Elemental subclassed objects of clickable or input types
        """
        self.object_sequence = args
        self.action_sequence = self.create_action_sequence()

    def __call__(self):
        """
        Calling an object of this class type runs my_sequence.perform() instead of needing
        to call .perform() manually on the object.
        """
        self.perform()

    @staticmethod
    def determine_action(elemental):
        """
        This method figures out what kind of action to perform based on the type of object that it is
        and returns a pointer to that objects class method based on the action.

        This method is called on instantiation of the class so the actions sequence should be
        available to the test author as soon as the object is created without additional work

        Args:
            elemental (): A Elemental subclassed object

        Returns:
            () A pointer for the bound method that will be called later

        """
        elemental_type = elemental.__class__.__name__

        clickable = ['Button', 'Dropdown', 'Checkbox', 'Image', 'Link', 'OptionTreeBranch', 'Radio', 'Row', 'Tab']
        openable = ['Dropdown']
        writeable = ['FileInput', 'TextInput']

        if callable(elemental):
            return elemental

        if elemental_type in clickable:
            return elemental.click

        if elemental_type in openable:
            return elemental.open

        if elemental_type in writeable:
            return elemental.write

    def create_action_sequence(self):
        """
        This method is called on class instantiation and creates a list of pointers to the bound
        methods which will be called when .perform() is called

        Returns:
            (list): A list of the pointers for the action that will be performed for the sequence.

        """
        return [self.determine_action(elemental) for elemental in self.object_sequence]

    def perform(self):
        """
        Runs through the actions defined on instantiation and performs the related action based on
        the type of action that it is.

        This implementation relies on the Sequencer.determine_action() method which returns a pointer
        to the method of the instance that will be acted upon.

        The second part of this process is determining if the action is of a writable type (E.g, TextInput)
        by looking for the string 'write' within the __name__ of the bound method.  If it detects that this
        is the case then the "text" property is looked up through invoking ".__self__" on the bound method
        to reference back to self of the the same method.

        This is simply a super sneaky way of getting what you're looking for (magic sparkles and unicorns, etc).
        """
        for action in self.action_sequence:
            try:
                action()
            except ElementNotInteractableException:
                action.__self__.browser.execute_script("arguments[0].click();", action.__self__.element())
                action()
