import time
import os
import pytest
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PHONE


BASE_URL = "https://passport.yandex.ru/auth/"


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )
    yield browser
    browser.quit()


def read_phone():
    """Чтение номера телефона из файла."""
    phone = PHONE
    if not phone:
        raise ValueError("Нет номера телефона")
    return phone


def test_phone_auth_screen_change(driver):
    """Проверка изменения экрана после ввода телефона."""

    wait = WebDriverWait(driver, 20)

    # 1. Открываем страницу авторизации
    driver.get(BASE_URL)

    # 2. Находим поле телефона
    phone_field = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[type='tel']")
        )
    )

    # 3. Считываем телефон из файла
    phone = read_phone()

    # 4. Вводим номер
    phone_field.send_keys(phone)

    # 5. Запоминаем исходное состояние
    initial_url = driver.current_url

    # 6. Нажимаем кнопку продолжения
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-action.full-width-button")
        )
    )

    submit_button.click()

    # 7. Проверяем изменение экрана
    wait.until(
        lambda d: (
                d.current_url != initial_url
                or len(d.find_elements(
            By.CSS_SELECTOR, "input[type='tel']"
        )) == 0
        )
    )

    # 8. Проверяем, что исходный экран изменился
    assert (
            driver.current_url != initial_url
            or len(driver.find_elements(
        By.CSS_SELECTOR, "input[type='tel']"
    )) == 0
    ), "Экран авторизации не изменился"