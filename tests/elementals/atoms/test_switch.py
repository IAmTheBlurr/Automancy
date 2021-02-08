from automancy import Switch


class TestSwitch(object):
    def test_switch_object_can_be_instantiated(self):
        test_object = Switch('//div', 'Test Object', 'test_object')
        assert test_object.locator == '//div'
        assert test_object.name == 'Test Object'
        assert test_object.system_name == 'test_object'
