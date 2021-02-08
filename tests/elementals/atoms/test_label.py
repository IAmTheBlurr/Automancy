from automancy import Label


class TestLabel(object):
    def test_label_object_can_be_instantiated(self):
        test_object = Label('//div', 'Test Object', 'test_object')
        assert test_object.locator == '//div'
        assert test_object.name == 'Test Object'
        assert test_object.system_name == 'test_object'
