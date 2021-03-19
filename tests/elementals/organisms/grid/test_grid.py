from automancy import Grid
from automancy.elementals.organisms.grid.grid_segments import GridSegments


class TestHTML5VideoPlayer(object):
    def test_grid_object_can_be_instantiated(self):
        test_grid = Grid('//div', 'Test HTML5 Video Player', 'test_html5_video_player', segment_locator='/segment')
        assert test_grid.locator == '//div'
        assert test_grid.name == 'Test HTML5 Video Player'
        assert test_grid.system_name == 'test_html5_video_player'
        assert test_grid.segments_locator == '//div/segment'
        assert type(test_grid.segments) == GridSegments
        assert test_grid.segment_components == {}
