import time
from selenium.webdriver.common.keys import Keys
from lettuce import step
from lettuce import world
from datetime import datetime
from lettuce_webdriver.util import assert_true
from selenium.webdriver.support.color import Color
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from lettuce_webdriver.util import find_button
from lettuce_webdriver.util import find_field
from lettuce_webdriver.util import find_option
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

@step('the sentence "([^"]*)"')
def have_the_sentence(step, expected):
	world.browser.get("http://127.0.0.1:5000")
	text_field = world.browser.find_element_by_id("textArea")
	text_field.send_keys(expected)
	assert True, text_field.get_attribute('value') == expected

@step('I press in button reset')
def press_reset_button(step):
	reset_button = world.browser.find_element_by_id("reset")
	reset_button.click()
	assert True, reset_button.get_attribute('value') == True

@step('I see the textfield in blank')
def have_the_sentence(step):
	reset_button = world.browser.find_element_by_id("reset")
	assert True, text_field.get_attribute('value') == ""
