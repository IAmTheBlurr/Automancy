import pytest

from automancy import Modal


class TestModel(object):
    def test_model_object_can_be_instantiated(self):
        test_model = Modal('//div', 'Test Model Object', 'test_model')
        assert test_model.locator == '//div'
        assert test_model.name == 'Test Model Object'
        assert test_model.system_name == 'test_model'

    def test_system_name_creation(self):
        pytest.skip('Not implemented yet')

    def test_exception_with_space_in_system_name(self):
        pytest.skip('Not implemented yet')

    def test_overwrite_existing_model_component(self):
        pytest.skip('Not implemented yet')

    def test_cannot_overwrite_existing_model_component_without_overwrite_being_true(self):
        pytest.skip('Not implemented yet')

    def test_added_component_is_concatenated_parent_plus_input(self):
        pytest.skip('Not implemented yet')

    def test_added_component_is_set_as_a_property_of_the_parent(self):
        pytest.skip('Not implemented yet')

    def test_added_component_exists_in_parent_children_property(self):
        pytest.skip('Not implemented yet')

    def test_added_components_properties_are_correct(self):
        pytest.skip('Not implemented yet')
