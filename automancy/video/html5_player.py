""" Contains components related to video player and video caption transcription containers """
from time import sleep

import webvtt

from ..core import Elemental


class HTML5Player(Elemental):
    """ The container object for all video related sub-objects and access point for all controls and other features """
    def __init__(self, locator, name='', container_locator='', viewport_locator='//video', caption_line_locator='', transcript_locator=''):
        super().__init__(locator, name=name)

        self.container = None
        if container_locator:
            self.container = VideoContainer(self.locator + container_locator)
            self.viewport = VideoViewport(self.locator + container_locator + viewport_locator)

        # Captions are the text that appear over a video viewport
        self.caption = None
        if caption_line_locator:
            self.caption = VideoCaptionLine(self.locator + caption_line_locator)

        # Transcripts are components which show the full caption log, usually clickable taking you to the timestamp.
        self.transcript = None
        if transcript_locator:
            self.transcript = VideoTranscript(self.locator + transcript_locator)

        self._current_time = None
        self._stored_id = ''

        self.controls = VideoControls('')
        self.settings = None
        self.length = 0.00
        self.width = 0.0
        self.height = 0.0

    @property
    def current_time(self):
        """
        Returns the current play time position that the video is in.

        Returns:
            (str) The current time that the video is at

        """
        return self.browser.execute_script('return document.getElementById("{0}").currentTime'.format(self.stored_id))

    @current_time.setter
    def current_time(self, value):
        if isinstance(value, float) or isinstance(value, int):
            value = str(value)

        if value:
            self._current_time = self.browser.execute_script('document.getElementById("{0}").currentTime={1}'.format(self.stored_id, value))
        else:
            self._current_time = '0.0'

    @property
    def id(self):
        """
        Getter for the webelement attribute "id"

        Returns:
            (str) The id of the associated webelement

        """
        return self.viewport.element().get_attribute('id')

    @property
    def stored_id(self):
        """
        Getter for a property called stored_id, which stores the
        "id" attribute of the web element.  Doubles as a setter
        if the class property doesn't exist.

        Notes:
            This is sort of a getter and setter method combined into one.

            The purpose of "stored_id" is to hold the last known value for
            the "id" attribute so that the methods performing javascript
            script execution (common to this class) don't have to do the
            expensive work of always interacting with the DOM or WebElement.

            This getter works by creating the class property "stored_id"
            if it doesn't exist, and setting it's value through the Video.id()
            method which looks up the actual web elements "id" attribute in
            real time.

            If the stored_id property already exists for an instance, it is simply
            returned to get around having to do a bunch of other work.

        Returns:
            (str) The last known value for the web elements "id" attribute

        """

        if self._stored_id == '':
            self._stored_id = self.id
            return self._stored_id

        return self._stored_id

    @stored_id.setter
    def stored_id(self, value):
        self._stored_id = value

    def play(self):
        """
        Run's the javascript command to play the video.

        Returns:
            (None) Nothing by the command
        """
        return self.browser.execute_script('document.getElementById("{id}").play();'.format(id=self.stored_id))

    def is_playing(self):
        """
        Every 0.25 seconds for 1 seconds, check to see if the current time is different than the previous checked time.

        Returns:
            (bool) True if video is playing, False if not.

        """
        seconds = 1
        slices = []

        if self.element():
            while seconds > 0:
                slices.append(self.current_time)
                sleep(0.25)
                seconds -= 0.25

        playing = False

        for index, time_slice in enumerate(slices):
            try:
                if time_slice < slices[index + 1]:
                    playing = True
            except IndexError:
                # End of list
                pass

        return playing

    def pause(self):
        """
        Pauses the video using the javascript executor

        Returns:

        """
        return self.browser.execute_script('document.getElementById("{id}").pause()'.format(id=self.stored_id))

    def is_paused(self):
        """
        Tells you if the video is paused using the javascript executor

        Returns:
            (bool) True if paused, False if not.

        """
        return self.browser.execute_script('return document.getElementById("{id}").paused'.format(id=self.stored_id))

    def volume(self, new_level=None):
        """
        Returns the current volume level or sets the volume level if "new_level" is not empty
        :param new_level: Optional parameter, if set and valid is used to change the level of the volume.
        :return:
        """
        if new_level:
            return self.browser.execute_script('document.getElementById("{id}").volume={level};'.format(id=self.stored_id, level=new_level))
        else:
            return self.browser.execute_script('return document.getElementById("{id}").volume'.format(id=self.stored_id))

    def is_muted(self):
        """ Determines if the video is muted with a javascript command """
        return self.browser.execute_script('return document.getElementById("{id}").muted'.format(id=self.stored_id))

    def reload(self):
        """ Reloads the video player with a javascript command """
        return self.browser.execute_script('document.getElementById("{id}").load();'.format(id=self.stored_id))

    def get_height(self):
        """
        Returns the true height dimension of the video itself (not the displayed width on the page) with a javascript command.

        Returns:
            (str) The height of the video.

        """
        self.height = self.browser.execute_script('document.getElementById("{id}").videoHeight;'.format(id=self.stored_id))
        return self.height

    def get_width(self):
        """
        Returns the true width dimension of the video itself (not the displayed width on the page) with a javascript command.

        Returns:
            (str) The width of the video.

        """
        self.width = self.browser.execute_script('document.getElementById("{id}").videoWidth;'.format(id=self.stored_id))
        return self.width

    def get_transcript(self):
        """
        Populates the transcript lines dictionary within the transcript object.

        Returns:
            None

        """
        if self.transcript and self.transcript.exists:
            self.transcript.get_lines()


class VideoContainer(TestObject):
    """ The container objects for surrounding element which holds a VideoViewport plus other elements """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)
        self.width = 0.0
        self.height = 0.0


class VideoViewport(TestObject):
    """ The container object for the video feed itself """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)


class VideoControls(TestObject):
    """ The container object for playback and volume controls """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)
        self.play_button = None
        self.pause_button = None
        self.stop_button = None
        self.mute_button = None
        self.volume_button = None
        self.volume_slider = None
        self.settings_button = None
        self.captions_button = None
        self.progress_slider = None
        self.time_indicator = None
        self.full_screen_button = None


class VideoTranscript(TestObject):
    """ Container for caption/transcription elements and controls """
    def __init__(self, locator, name='', line_locator='', selector_locator='', line_time_locator='', line_text_locator=''):
        super().__init__(locator, name=name)
        self.line_locator = self.locator + line_locator
        self.selector_locator = self.locator + selector_locator
        self.line_time_locator = line_time_locator
        self.line_text_locator = line_text_locator
        self.time_from_data_begin = False

        # Line elements should be dictionaries that look like this {'time': 0.00, 'text': ''}
        self.lines = []

        # Selection key/values should look something like 'english': '//option' ( <- xpath )
        self.selections = {}
        self.transcript_file = None

    def get_lines(self):
        """ Actively populates the Transcript.lines object with the text and time """
        lines = []

        if self.line_locator:
            line_elements = self.find_elements(self.line_locator)

            for index, line in enumerate(line_elements, start=1):

                line_name = 'line{0}'.format(index)
                specific_line_locator = '{0}[{1}]'.format(self.line_locator, index)

                # Construct the actual transcript line object
                line_object = VideoTranscriptLine(
                    specific_line_locator,
                    name=line_name,
                    text_locator=self.line_text_locator,
                    time_locator=self.line_time_locator,
                    time_from_data_begin=self.time_from_data_begin
                )

                line_object.scroll_to()

                # Get the content data of the line and append it to lines[]
                lines.append(line_object)

        self.lines = lines

    def read_from_file(self, file_path):
        """
        Processes the contents of a VTT file and stores the output in
        VideoTranscript.transcript_file.

        Args:
            file_path (str): The path to the file the target VTT file

        """
        self.transcript_file = webvtt.read(file_path)

    def text_matches_file(self, file_path):
        """
        Compares the transcript line text against a source webvtt file.

        Notes:
            VideoTranscript.get_line() will be called if VideoTranscript.lines
            is empty

        Args:
            file_path (str): The path to the file the target VTT file

        """
        lines_match = []

        transcript_file = webvtt.read(file_path)

        for from_web, from_file in zip(self.lines, transcript_file.captions):
            lines_match.append(True if from_web.text == from_file.text else False)

        return False if False in lines_match else True

    def time_matches_file(self, file_path):
        """
        Compares the transcript line times against a source webvtt file.

        Notes:
            VideoTranscript.get_line() will be called if VideoTranscript.lines
            is empty

        Args:
            file_path (str): The path to the file the target VTT file

        """
        lines_match = []

        transcript_file = webvtt.read(file_path)

        for from_web, from_file in zip(self.lines, transcript_file.captions):
            lines_match.append(True if float(from_web.time) == from_file.start_in_seconds else False)

        return False if False in lines_match else True


class VideoTranscriptLine(TestObject):
    """ Container for a single transcription line """
    def __init__(self, locator, name='', time_locator='', text_locator='', time_from_data_begin=False):
        super().__init__(locator, name=name)
        self.line_text = VideoTranscriptLineText(locator + text_locator)
        self.line_time = VideoTranscriptLineTime(locator + time_locator)
        self.time_from_data_begin = time_from_data_begin

    @property
    def text(self):
        """
        Inspects the WebElement that contains the text value for the transcript line

        Returns:
            (str) The displayed text value for the line

        """
        self.scroll_to()
        return self.line_text.text

    @text.setter
    def text(self, value):
        self.line_text = value

    @property
    def time(self):
        """
        Inspects the WebElement that contains the time value for the transcript line

        Returns:
            (str) the displayed time value for the line

        """
        self.scroll_to()

        if self.time_from_data_begin:
            value = self.element().get_attribute('data-begin')
        else:
            value = self.line_time.text

            # Replace colon with a period where colon is used delineate minutes from seconds.
            if value and ':' in value:
                value = value.replace(':', '.')

        return value

    @time.setter
    def time(self, value):
        self.line_time = value


class VideoTranscriptLineText(TestObject):
    """ Container for the text for a transcript line """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)


class VideoTranscriptLineTime(TestObject):
    """ Container for the time for a transcript line """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)


class VideoCaptionLine(TestObject):
    """ Container for the captions that will appear over the video viewport """
    def __init__(self, locator, name=''):
        super().__init__(locator, name=name)
