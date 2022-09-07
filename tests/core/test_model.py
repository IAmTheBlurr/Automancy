import pytest

from automancy import Button, Dropdown, DropdownOptions, Modal

test_model = Modal('//div', 'Test Model Object', 'test_model')


class TestModel(object):
    def test_model_object_can_be_instantiated(self):
        assert test_model.locator == '//div'
        assert test_model.name == 'Test Model Object'
        assert test_model.system_name == 'test_model'

    def test_simple_add_elemental_to_model(self):
        test_model.add(Button, '//button[contains(text(), "Super Cool Button")]', 'Super Cool Button', 'super_cool_button')

        assert hasattr(test_model, 'super_cool_button')
        assert isinstance(test_model.super_cool_button, Button)
        assert test_model.super_cool_button.locator == '//div//button[contains(text(), "Super Cool Button")]'
        assert test_model.super_cool_button.name == 'Super Cool Button'

    def test_complex_add_element_to_model_with_kwargs(self):
        dropdown_options = DropdownOptions(
            option_locator='//div[contains(text(), "Options Locator")]',
            option_type='//div[contains(text(), "Option Type")]',
            static_options='//div[contains(text(), "Static Options")]',
            disconnected_options='//div[contains(text(), "Disconnected Options")]',
            option_selector_extension='//div[contains(text(), "Option Selector Extension")]',
            option_label_extension='//div[contains(text(), "Option Label Extension")]',
        )
        test_model.add(Dropdown, '//dropdown', 'Test Cool Dropdown', 'test_dropdown', options=dropdown_options)

        assert hasattr(test_model, 'test_dropdown')
        assert isinstance(test_model.test_dropdown, Dropdown)
        assert test_model.test_dropdown.locator == '//div//dropdown'
        assert test_model.test_dropdown.name == 'Test Cool Dropdown'
        assert test_model.test_dropdown.options_locator == dropdown_options.option_locator
        assert test_model.test_dropdown.options_type == dropdown_options.option_type
        assert test_model.test_dropdown.static_options == dropdown_options.static_options
        assert test_model.test_dropdown.disconnected_options == dropdown_options.disconnected_options
        assert test_model.test_dropdown.option_selector_extension == dropdown_options.option_selector_extension
        assert test_model.test_dropdown.option_label_extension == dropdown_options.option_label_extension
