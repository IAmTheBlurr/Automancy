from automancy import FileInput


class TestFileInput(object):
    def test_file_input_object_can_be_instantiated(self):
        test_object = FileInput('//div', 'Test Object', 'test_object')
        assert test_object.locator == '//div'
        assert test_object.name == 'Test Object'
        assert test_object.system_name == 'test_object'
