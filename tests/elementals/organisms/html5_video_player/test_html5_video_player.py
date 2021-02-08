from automancy import HTML5VideoPlayer


class TestHTML5VideoPlayer(object):
    def test_html5player_object_can_be_instantiated(self):
        test_html5player = HTML5VideoPlayer('//div', 'Test HTML5 Video Player', 'test_html5_video_player')
        assert test_html5player.locator == '//div'
        assert test_html5player.name == 'Test HTML5 Video Player'
        assert test_html5player.system_name == 'test_html5_video_player'
