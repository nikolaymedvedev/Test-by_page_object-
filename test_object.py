import pytest
from page_object import PageObject


@pytest.mark.parametrize("text, w", [pytest.param("Погода в гомеле", "Картинки", id="Images"),
                                     pytest.param("Курс валют", "Видео", id="Video"),
                                     pytest.param("Вконтакте", "Карты", id="Karts")
                                     ])
def test_yandex(browser, text, w):
    run = PageObject(browser)
    run.go_on_url()
    run.write_in_field(text)
    run.click_buttom()
    result = run.view_elements()
    assert w in result
