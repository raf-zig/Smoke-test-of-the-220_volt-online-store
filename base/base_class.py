class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word under login symbol"""

    def assert_word_under_login_symbol(self, word):
        value_word = word.text
        assert value_word != "Вход"
        print("Input button hasn`t 'Вход'")


