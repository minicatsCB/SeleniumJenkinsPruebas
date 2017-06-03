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

@step('The textfield in blank')
def have_the_textfield_in_blank(step):
	world.browser.get("http://127.0.0.1:5000")
	text_field = world.browser.find_element_by_id("textArea")
	assert True, text_field.get_attribute('value') == ""
	

@step('I enter the sentence "([^"]*)"')
def enter_the_sentence(step, expected):
	text_field = world.browser.find_element_by_id("textArea")
	text_field.send_keys(expected)

@step('I see "([^"]*)" in the textfield')
def check_sentence(step, expected):
	if(len(expected) > 100):
		expected = str(expected[0:99])
	text_field = world.browser.find_element_by_id("textArea")
    	assert True, text_field.get_attribute('value') == expected

