
def test_open_best_selling_products(app):
    app.home.open_start_page()
    app.home.scroll_to_best_selling()
    count = app.home.count_best_selling_products()
    for index in range(count):
        name = app.home.get_name_best_selling_product(index)
        app.home.click_on_best_selling_product(index)
        assert app.home.get_text_name() == name
        app.home.click_on_button_home()
