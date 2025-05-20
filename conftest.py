# conftest.py
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, expect


@pytest.fixture(scope="session")
def authenticated_context(browser: Browser) -> BrowserContext:
    # Создаем новый контекст
    context = browser.new_context()
    page = context.new_page()

    # Выполняем шаги из вашего теста test_login
    login_data = {
        "email": "yaroslavstepanov2018@gmail.com",
        "password": "12345678"
    }
    page.goto("https://conf-demo.nntu.ru")
    page.get_by_role("button", name="Вход").click()
    page.locator("#email-log").fill(login_data["email"])
    password_input = page.locator('p-password#password-log input[type="password"]')
    password_input.fill(login_data["password"])
    login_button = page.locator('p-button[label="Вход"] button[type="submit"]')
    login_button.click()

    # Проверяем успешность авторизации
    expect(page.locator('a.nav-link.px-2.text-white.head-text:has-text("Мои статьи")')).to_be_visible()

    # Сохраняем состояние контекста
    context.storage_state(path="auth_state.json")
    return context


@pytest.fixture
def authenticated_page(authenticated_context: BrowserContext) -> Page:
    # Создаем новую страницу в аутентифицированном контексте
    page = authenticated_context.new_page()
    yield page
    page.close()
