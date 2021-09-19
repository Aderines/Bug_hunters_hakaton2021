class RegistrationLoginHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.first_name = 'Cat'
        self.last_name = 'In-Glasses'
        self.password = '123456789'
        self.email = ''
        self.title = 'mrs'

    def email_generator(self):
        self.app.wd.get('https://10minutemail.net/?lang=ru')
        email = self.wd.find_element_by_class_name('mailtext').get_attribute("value")
        self.email = email

    def check_page_availability(self):
        # self.wd.find_element_by_class_name("mobile-menu").click()
        login_button = self.wd.find_element_by_class_name("liOffcanvas")
        login_button.click()
        self.wd.implicitly_wait(10)
        return self.wd.current_url

    def open_registration_page(self):
        self.app.wd.get('https://apparel-uk.local:9002/ucstorefront/en/login')

    def registration_title(self):
        title = self.wd.find_element_by_name("titleCode")
        title.click()
        self.wd.find_element_by_xpath(f'//option[@value="{self.title}"]').click()

    def registration_input_first_name(self):
        name = self.wd.find_element_by_name("firstName")
        name.send_keys(self.first_name)
        signup_name = self.first_name
        return signup_name

    def registration_input_last_name(self):
        last_name = self.wd.find_element_by_name("lastName")
        last_name.send_keys(self.last_name)

    def registration_input_email(self):
        email = self.wd.find_element_by_name("email")
        email.send_keys(self.email)

    def registration_input_password(self):
        password = self.wd.find_element_by_name("pwd")
        password.send_keys(self.password)

    def registration_input_password_confirmation(self):
        password = self.wd.find_element_by_name("checkPwd")
        password.send_keys(self.password)

    def registration_terms_checkbox(self):
        terms_check = self.wd.find_element_by_name("termsCheck")
        terms_check.click()

    def registration_button(self):
        button = self.wd.find_element_by_class_name("btn-default")
        button.click()

    def login_email(self):
        login_email = self.wd.find_element_by_name("j_username")
        login_email.send_keys(self.email)

    def login_password(self):
        login_password = self.wd.find_element_by_name("j_password")
        login_password.send_keys(self.password)

    def login_button(self):
        self.wd.find_element_by_class_name("btn-primary").click()

    def enter_account_check(self):
        message = self.wd.find_element_by_class_name("js-logged_in").get_attribute("textContent")
        # message = self.wd.find_element_by_css_selector(".navigation--top .nav__right .nav__links--account li.logged_in").text
        welcome_message = message[10:]
        return welcome_message

    # TODO пофиксить
    # def close_registration_account(self):
    #     self.wd.find_element_by_class_name("js-myAccount-toggle").click()
    #     self.wd.find_element_by_link_text("Close Account").click()
    #     self.wd.find_element_by_class_name("btn-primary").click()
    #     self.wd.find_element_by_class_name("js - close - account - action").click()
    #     return self.wd.current_url
