from automancy import Button


class TestButton(object):
    def __init__(self):
        def test_object_instantiates_correctly():
            test_button = Button('//button[@data-tid="test-button"]', 'Test Button', 'test_button')
            assert test_button.locator == '//button[@data-tid="test-button"]'
            assert test_button.name == 'Test Button'
            assert test_button.system_name == 'test_button'

        def test_button_is_located_on_page():
            test_button = Button('//button[@data-tid="test-button"]', 'Test Button', 'test_button')
            assert test_button.exists
            assert test_button.visible
