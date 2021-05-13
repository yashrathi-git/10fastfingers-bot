
# 10fastfingers-bot
A fun python script using selenium, to achieve any score in typing test at [10fastfingers](https://10fastfingers.com/typing-test/english) with adjustable typing speed.

https://user-images.githubusercontent.com/57002207/118098607-bcbe2400-b3f1-11eb-8684-b1f26b61e4a8.mp4


## Installation
First make sure you have the following:
* [Python 3](https://www.python.org/downloads/)
* [Chrome Browser](https://www.google.com/intl/en_in/chrome/)
* [git](https://git-scm.com/downloads)
* Clone repo and install dependencies
  ```sh
  $ git clone https://github.com/yashrathi-git/10fastfingers-bot
  $ cd 10fastfingers-bot
  $ pip install -r requirements.txt
  ```
* Download the [chrome webdriver](https://chromedriver.chromium.org/downloads) and extract the file in "10fastfingers-bot/drivers" directory

## Usage
Navigate to project directory-
```sh
$ python ./automate.py
```
This will open up Chrome window, and automatically start the typing test with maximum typing speed.

## Options
```sh
Usage: automate.py [options]

--max           Maximum typing speed.
--wpm=<speed>   Specify a WPM as typing speed.
--instant        Types(dumps) everything in one go(instantly).
-h --help       Show this message.
```

## Example
Get result of approximately 200 WPM
```sh
$ python ./automate.py --wpm 200
```