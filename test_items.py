link = "http://selenium1py.pythonanywhere.com/"
import pytest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    # добавлено для отладки
    # time.sleep(30)

    # Проверяем наличие кнопки "Добавить в корзину"
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button is not None, "Кнопка 'Добавить в корзину' не найдена"