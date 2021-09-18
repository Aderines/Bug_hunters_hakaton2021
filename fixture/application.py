from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://apparel-uk.local:9002/ucstorefront/en")
        wd.find_element_by_css_selector(".page-homepage.pageType-ContentPage")

    def destroy(self):
        self.wd.quit()