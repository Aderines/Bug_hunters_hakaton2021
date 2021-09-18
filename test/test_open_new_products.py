
def test_open_new_products(app):
    app.home.open_start_page()
    app.home.scroll_to_new_selling()
    count = app.home.count_new_products()
    for index in range(count):
        name = app.home.get_name_new_product(index)
        app.home.click_on_new_product(index)
        assert app.home.get_text_name() == name
        app.home.click_on_button_home()
