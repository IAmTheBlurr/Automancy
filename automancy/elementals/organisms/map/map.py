""" ./elementals/organisms/map/map.py """
from selenium.webdriver.common.action_chains import ActionChains

from automancy.core import Elemental


class Map(Elemental):
    """ Represents a geolocation based map """
    def __init__(self, locator, human_name, system_name):
        super().__init__(locator, human_name, system_name)

    def drag_by(self, x: int, y: int) -> None:
        """ Click and drag the map by x and y pixel amounts """
        ActionChains(self.browser).move_to_element(self.element()).click_and_hold().move_by_offset(x, y).release().perform()
