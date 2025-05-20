from time import sleep
import pytest
from playwright.sync_api import Page, expect

def test_conf_registration(page: Page):

    registration_data = {
        "lastName": "Иванов",
        "firstName": "Иван",
        "middleName": "Иванович",
        "phone": "1234567890",  # Будет преобразовано в маску (123) 456-7890
        "email-reg": "test@test2.com",
        "password-reg": "12345678",
        "confirmedPassword": "12345678"
    }

    page.goto('https://conf-demo.nntu.ru')
    page.get_by_role('button', name='Регистрация').click()

    # Заполняем поля
    page.locator("#lastName").fill(registration_data["lastName"])
    page.locator("#firstName").fill(registration_data["firstName"])
    page.locator("#middleName").fill(registration_data["middleName"])

    # Для телефона учитываем маску (000) 000-0000
    page.locator("#phone").fill("2345678900")  # Playwright автоматически применит маску
    page.locator("#email-reg").fill(registration_data["email-reg"])
    # Заполняем пароли
    password_input = page.locator('p-password#password-reg input[type="password"]')
    password_input.fill(registration_data["password-reg"])
    confirm_password_input = page.locator('p-password#confirmedPassword input[type="password"]')
    confirm_password_input.fill(registration_data["password-reg"])
    # Локатор для кнопки "Регистрация"
    submit_button = page.locator('p-button[label="Регистрация"] button[type="submit"]')
    # Клик
    submit_button.click()
    # Проверка всплывающего сообщения
    success_alert = page.get_by_role("alert").filter(has_text="Регистрация прошла успешно" )
    # Ожидание появления и проверка текста
    expect(success_alert).to_be_visible()
    expect(success_alert).to_contain_text("На вашу почту отправлено письмо с подтверждением")


def test_login(page: Page):
    login_data = {
        "email": "yaroslavstepanov2018@gmail.com",
        "password": "12345678"
    }

    # Переход на страницу
    page.goto("https://conf-demo.nntu.ru")

    # Открытие формы входа
    page.get_by_role("button", name="Вход").click()

    # Заполнение полей
    page.locator("#email-log").fill(login_data["email"])
    password_input = page.locator('p-password#password-log input[type="password"]')
    password_input.fill(login_data["password"])

    # Ожидание активации кнопки
    login_button = page.locator('p-button[label="Вход"] button[type="submit"]')


    # Клик
    login_button.click()

    # Проверка успешной авторизации
    expect(page.locator('a.nav-link.px-2.text-white.head-text:has-text("Мои статьи")')).to_be_visible()
from time import sleep
import pytest
from playwright.sync_api import Page, expect

def test_conf_registration(page: Page):

    registration_data = {
        "lastName": "Иванов",
        "firstName": "Иван",
        "middleName": "Иванович",
        "phone": "1234567890",  # Будет преобразовано в маску (123) 456-7890
        "email-reg": "test@test2.com",
        "password-reg": "12345678",
        "confirmedPassword": "12345678"
    }

    page.goto('https://conf-demo.nntu.ru')
    page.get_by_role('button', name='Регистрация').click()

    # Заполняем поля
    page.locator("#lastName").fill(registration_data["lastName"])
    page.locator("#firstName").fill(registration_data["firstName"])
    page.locator("#middleName").fill(registration_data["middleName"])

    # Для телефона учитываем маску (000) 000-0000
    page.locator("#phone").fill("2345678900")  # Playwright автоматически применит маску
    page.locator("#email-reg").fill(registration_data["email-reg"])
    # Заполняем пароли
    password_input = page.locator('p-password#password-reg input[type="password"]')
    password_input.fill(registration_data["password-reg"])
    confirm_password_input = page.locator('p-password#confirmedPassword input[type="password"]')
    confirm_password_input.fill(registration_data["password-reg"])
    # Локатор для кнопки "Регистрация"
    submit_button = page.locator('p-button[label="Регистрация"] button[type="submit"]')
    # Клик
    submit_button.click()
    # Проверка всплывающего сообщения
    success_alert = page.get_by_role("alert").filter(has_text="Регистрация прошла успешно" )
    # Ожидание появления и проверка текста
    expect(success_alert).to_be_visible()
    expect(success_alert).to_contain_text("На вашу почту отправлено письмо с подтверждением")


def test_login(page: Page):
    login_data = {
        "email": "yaroslavstepanov2018@gmail.com",
        "password": "12345678"
    }

    # Переход на страницу
    page.goto("https://conf-demo.nntu.ru")

    # Открытие формы входа
    page.get_by_role("button", name="Вход").click()

    # Заполнение полей
    page.locator("#email-log").fill(login_data["email"])
    password_input = page.locator('p-password#password-log input[type="password"]')
    password_input.fill(login_data["password"])

    # Ожидание активации кнопки
    login_button = page.locator('p-button[label="Вход"] button[type="submit"]')


    # Клик
    login_button.click()

    # Проверка успешной авторизации
    expect(page.locator('a.nav-link.px-2.text-white.head-text:has-text("Мои статьи")')).to_be_visible()
