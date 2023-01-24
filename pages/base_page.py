class BasePage():

def __init__(self, browser, url):
    self.browser = browser
    self.url = url

def open(self):
    get(link = "http://selenium1py.pythonanywhere.com/")