def test_verify_id_basket(app):
    app.basket.add_to_basket()
    app.basket.verify_id_basket()
    assert len(app.basket.verify_id_basket(id)) == 8


def test_help_popup(app):
    assert app.basket.help_popup()
