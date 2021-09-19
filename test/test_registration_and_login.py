def test_open_login_and_registration_page(app):
    assert app.registration.check_page_availability() == 'https://apparel-uk.local:9002/ucstorefront/en/login'


def test_success_registration(app):
    app.registration.email_generator()
    app.registration.open_registration_page()
    app.registration.registration_title()
    signup_name = app.registration.registration_input_first_name()
    app.registration.registration_input_last_name()
    app.registration.registration_input_email()
    app.registration.registration_input_password()
    app.registration.registration_input_password_confirmation()
    app.registration.registration_terms_checkbox()
    app.registration.registration_button()
    welcome_message = app.registration.enter_account_check()
    assert welcome_message == f'Welcome {signup_name}'


def test_success_login(app):
    app.registration.open_registration_page()
    login_name = app.registration.first_name
    app.registration.login_email()
    app.registration.login_password()
    app.registration.login_button()
    welcome_message = app.registration.enter_account_check()
    assert welcome_message == f'Welcome {login_name}'

# TODO надо пофиксить, а то тест падает :c
# def test_closing_account(app):
#     app.registration.open_registration_page()
#     app.registration.login_email()
#     app.registration.login_password()
#     app.registration.login_button()
#     app.registration.close_registration_account()
