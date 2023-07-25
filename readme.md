# Willhaben and Bazos parser connected to telegram bot

- [x] The bot can parse needed announces from the sites willhaben.at and bazos.cz.
- [ ] The bot waits for new announces and notify the user about the new ones.

Developer: [DobbiKov](dobbikov.com)

## Installation 
1. Make sure that you have selenium installed: `python -m pip install -U Selenium  `
2. Install all the dependencies: `pip install -r requirements.txt`
3. Make sure that you have the FireFox browser on your device (Here is how to use chrome instead: [click](#chrome-selenium-usage))
4. Set your own bot token in **variables.py** in variable `TOKEN=""`
5. Write `python3 main.py` in order to start the bot


## Chrome Selenium Usage
- In the file **au_parse_search_site.py** find this code:
```python
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920,1080")

class Willhaben:
    def __init__(self):
        self.browser = webdriver.Firefox(options=firefox_options)
```

- You have to change used methods to the chrome's one so the code looks like that:
```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

class Willhaben:
    def __init__(self):
        self.browser = webdriver.Chrome(options=chrome_options)
```