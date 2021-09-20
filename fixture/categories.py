from selenium.webdriver.common.by import By
import time

class CategoriesHelper:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def open_category_page(self):
        """ open category page and check title, url and breadcrumb """
        url = "https://apparel-uk.local:9002/ucstorefront/en/Collections/c/collections"
        self.wd.get(url)
        page_check = [('url', 'ucstorefront/en/Collections/c/collections'),
                      ('title', 'Collections | Apparel Site UK'),
                      ('breadcrumb', 'COLLECTIONS')]
        for check in page_check:
            if check[0] == 'url':
                assert self.wd.current_url.endswith(check[1])
            elif check[0] == 'title':
                actual_title = self.wd.title
                assert check[1] == actual_title
            elif check[0] == 'breadcrumb':
                br_crumb = self.wd.find_element(By.CSS_SELECTOR, '.breadcrumb .active').text
                assert check[1] == br_crumb

    def collect_filters(self):
        """
        collect all available fiters on the page
        :return all_filters: List
        """
        el_all_filters = self.wd.find_elements(By.CSS_SELECTOR, '.facet.js-facet')
        # filters_quantity = len(el_all_filters) - could be checked as well
        all_filters = [filter.find_element(By.CSS_SELECTOR, '.facet__name.js-facet-name').text
                       for filter in el_all_filters]
        return all_filters

    def collect_options(self, filter):
        """
        Takes list of available filters and collect options under each filter
        :param filter: List
        :return: options, List
        """
        category_sel = f"//div[contains(@class, 'js-facet') and contains(., '{filter}')]"
        category_el = self.wd.find_element(By.XPATH, category_sel)
        options = (category_el.find_element(By.CLASS_NAME, "js-facet-values").text).split('\n')
        return options
