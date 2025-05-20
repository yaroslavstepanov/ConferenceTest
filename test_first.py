from time import sleep

from playwright.sync_api import Page, expect


def test_conf_registration_title(page: Page):
    page.goto('https://conf-demo.nntu.ru')

    # Кликаем по кнопке "Регистрация"
    page.get_by_role('button', name='Регистрация').click()

    # Ожидаем появление заголовка (используем CSS-селектор)
    registration_header = page.locator('h2.fw-bold:has-text("Регистрация")')
    expect(registration_header).to_be_visible()

def test_conf_enter_title(page: Page):
    page.goto('https://conf-demo.nntu.ru')

    # Кликаем по кнопке "Вход"
    page.get_by_role('button', name='Вход').click()

    # Ожидаем появление заголовка (используем CSS-селектор)
    registration_header = page.locator('h2.fw-bold:has-text("Вход в аккаунт")')
    expect(registration_header).to_be_visible()

