from automancy import Radio


class TestRadio(object):
    def test_radio_object_can_be_instantiated(self):
        test_object = Radio('//div', 'Test Object', 'test_object')
        assert test_object.locator == '//div'
        assert test_object.name == 'Test Object'
        assert test_object.system_name == 'test_object'
