"""
Usage: automate.py [options]

--max           Maximum typing speed.
--wpm=<speed>   Specify a WPM as typing speed.
--instant        Types(dumps) everything in one go(instantly).
-h --help       Show this message.
"""
import os
from time import sleep
from docopt import docopt
from selenium import webdriver

URL = "https://10fastfingers.com/typing-test/english"
BASEDIR = os.path.dirname(os.path.realpath(__file__))


def calculate_sleep_time(wpm):
    return 60/wpm


class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(BASEDIR, "drivers", "chromedriver"))
        self.driver.get(URL)
        # Wait 6 sec for page to load and animations to finish
        sleep(6)
        self._close_cookie_prompt()

    def _close_cookie_prompt(self):
        button_id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"
        self.driver.find_element_by_id(button_id).click()

    def _find_relevant_text(self):
        return self.driver.find_element_by_id("wordlist").get_attribute("innerHTML").split("|")

    @property
    def text(self):
        return self._find_relevant_text()

    def type(self, instant=False, wpm=None, max_speed=False):
        text = self.text
        max_wpm = len(text)
        if (not max_speed) and wpm is None:
            wpm = max_wpm
        if wpm and wpm > max_wpm:
            print(f"Maximum WPM can only be {max_wpm}")
            return
        if wpm and max_wpm <= 0:
            print("WPM must be greater than 0")
            return
        if wpm:
            text = text[:wpm]
            # Considering sometime is taken to process and fill in the word
            sleep_duration = calculate_sleep_time(wpm) - 0.13
        else:
            sleep_duration = 0
        input_field = self.driver.find_element_by_id("inputfield")
        input_field.click()
        if instant:
            text_to_dump = " ".join(text)
            print(f"Adding text: '{text_to_dump}'")
            input_field.send_keys(text_to_dump)
        else:
            for word in text:
                print(f"typing {word}")
                input_field.send_keys(word + " ")
                sleep(sleep_duration)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments["--wpm"]:
        arguments["--wpm"] = int(arguments["--wpm"])
    automation = Automation()
    automation.type(instant=arguments["--instant"],
                    wpm=arguments["--wpm"],
                    max_speed=arguments["--max"])
