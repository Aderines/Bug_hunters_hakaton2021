def test_click_on_banner_women(app):
    app.home.open_start_page()
    app.home.click_on_banners("Women")
    assert app.home.get_text_cataloge_name() == "WOMEN"


def test_click_on_banner_men(app):
    app.home.open_start_page()
    app.home.click_on_banners("Men")
    assert app.home.get_text_cataloge_name() == "MEN"


def test_click_on_banner_youth(app):
    app.home.open_start_page()
    app.home.click_on_banners("Youth")
    assert app.home.get_text_cataloge_name() == "STREETWEAR YOUTH"


def test_click_on_banner_brand(app):
    app.home.open_start_page()
    app.home.click_on_banners("Our brand range")
    assert app.home.get_text_cataloge_name() == "BRANDS"
