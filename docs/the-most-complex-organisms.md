# The Most Complex _Organisms_
This readme provides and brief outline of the craziest and most amazing Elementals within Automancy.

Simple code examples for each will be provided here for illustration, and further discussions for each and their usages will (eventually) be found in readme files for each of the modules

Seriously, these things are wild.  You won't believe just how crazy and amazing they are.

My favorites are the Clock and HTML5 Video Player modules.  The way the Clock module can be used to select the time on a round clock face is kind of insane.  I had to write some nutty trigonometry in order to make it as simple as it is.

I'm rather proud of it if I do say so myself!

The HTML5 Video Player, well... that's something completely different.

Enjoy!

## Calendar
How many web apps can you think of which use some sort of date picker in the form of a monthly calendar?  It's a hell of a lot, right?

Have you ever tried to interact programmatically and dynamically in some automated sense?  It really sucks; there are a TON of conditionals on a month by month basis, it's awful most of the time and code to support automating calendar actions tends to be very difficult to maintain.  Everyone knows it but no one does anything about it.  Well, Automancy does something about it.

    self.event_date_options = CalendarOptions(
        current_month_locator='/div[1]/div[2]//p',
        day_cell_locator='/div',
        week_row_locator='/div[1]/div[3]/div/div',
        month_next_locator='/div[1]/div[2]//button[2]',
        month_prev_locator='/div[1]/div[2]//button[1]',
        save_button_locator='/div/button/span[contains(text(), "OK")]/parent::button',
        cancel_button_locator='/div/button/span[contains(text(), "Cancel")]/parent::button'
    )

    self.event_date_calendar = Calendar('//h6[contains(text(), "{year}")]/parent::div/parent::div/parent::div'.format(year=datetime.datetime.today().year), options=self.event_date_options)
    
    self.home.create_event.event_date_calendar.next_month()
    self.home.create_event.event_date_calendar.select_day(schedule_date)
    assertLosesExistence(self.home.create_event.event_date_calendar)

## Clock

## Dropdown

## Grid

## HTML5 Video Player

## Option Tree

## Table