# test_registration.py
import re
from time import sleep

from playwright.sync_api import expect, Page


def test_my_articles(authenticated_page: Page):
    # Переходим на страницу "Мои статьи"
    authenticated_page.goto("https://conf-demo.nntu.ru/jobs")
    # Проверяем, что список статей виден
    heading_locator = authenticated_page.locator('h2.h3.text-black.mb-0.flex-grow-1:has-text("Мои статьи")')
    # Проверка видимости заголовка
    expect(heading_locator).to_be_visible()

def test_my_articles_from_conference(authenticated_page: Page):
    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 2. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

    # 3. Клик на кнопку "Мои работы" (находим сразу, без привязки к блоку)
    my_articles_button = authenticated_page.locator("button.btn.btn-outline-primary.px-4.ng-star-inserted:has-text('Мои работы')")
    my_articles_button.click()

    # 4. Проверяем наличие элемента с классами (без привязки к тексту)
    conference_span = authenticated_page.locator("span.d-block.d-md-inline.text-truncate.ng-star-inserted")
    expect(conference_span).to_be_visible()

def test_logout(authenticated_page: Page):
    # Переходим на страницу, где доступно меню пользователя
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 1. Кликаем на элемент, открывающий выпадающее меню
    user_menu_button = authenticated_page.locator("a.dropdown-toggle[data-bs-toggle='dropdown']")
    user_menu_button.click()

    # 2. Кликаем на пункт "Выход" в выпадающем меню
    logout_link = authenticated_page.locator("a.dropdown-item.text-danger:has-text('Выход')")
    logout_link.click()

    # 3. Проверяем, что выход выполнен успешно
    # Например, проверяем наличие кнопки "Вход" на главной странице
    expect(authenticated_page.get_by_role("button", name="Вход")).to_be_visible()


def test_conference_details(authenticated_page: Page):
    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 3. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

    # Вариант 2: Проверка наличия заголовка конференции
    expect(authenticated_page.locator(".conference-title")).to_be_visible()


def test_add_article_button(authenticated_page: Page):
    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 3. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

from playwright.sync_api import Page, expect

def test_add_article_button(authenticated_page: Page):
    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 2. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

    # 4. Клик на кнопку "Добавить работу"
    add_button = authenticated_page.locator(".btn.btn-primary:has-text('Добавить работу')")
    add_button.click()

    # 5. Проверка появления заголовка "Добавление работы"
    expect(authenticated_page.locator("h5.mb-0:has-text('Добавление работы')")).to_be_visible()

def test_add_article_button2(authenticated_page: Page):
    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 2. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

    # 3. Клик на кнопку "Добавить работу"
    add_button = authenticated_page.locator(".btn.btn-primary:has-text('Добавить работу')")
    add_button.click()

    # 4. Проверка, что заголовок "Добавление работы" появился
    add_heading = authenticated_page.locator("h5.mb-0:has-text('Добавление работы')")
    #expect(add_heading).to_be_visible()

    # 5. Клик на кнопку "Отмена"
    cancel_button = authenticated_page.locator("button.btn.btn-secondary:has-text('Отмена')")
    cancel_button.click()

    # 6. Проверка, что заголовок "Добавление работы" скрыт
    expect(add_heading).not_to_be_visible()

def test_add_article(authenticated_page: Page):
    # Конфигурация тестовых данных
    article_data = {
        "title": "Автоматизированное тестирование веб-интерфейсов",
        "description": "Исследование методов автоматизации тестирования с использованием Playwright",
        #"phone": "+7 (999) 123-4567",  # Готовый формат с маской, скорее всего предзаполнен
        #"organization": "НГТУ", # Готовый формат с маской, скорее всего предзаполнен
        "section": "Секция 1. «Графические информационные технологии и системы»", # Готовый формат с маской, скорее всего предзаполнен
        "file": "articles/test_article.pdf",

        # Опциональные поля (можно раскомментировать)
        # "orcid": "0000-0001-2345-6789",
        # "academicDegree": "Кандидат технических наук",
        # "academicTitle": "Доцент"
    }

    # 1. Переход на страницу конференций
    authenticated_page.goto("https://conf-demo.nntu.ru/conferences")

    # 2. Клик на первую кнопку "Подробнее"
    details_button = authenticated_page.locator(".conf-item .btn-outline-primary:has-text('Подробнее')").first
    details_button.click()

    # 3. Клик на кнопку "Добавить работу"
    add_button = authenticated_page.locator(".btn.btn-primary:has-text('Добавить работу')")
    add_button.click()

    # 4. Заполнение основных полей
    authenticated_page.locator("input[formcontrolname='title']").fill(article_data["title"])
    authenticated_page.locator("textarea[formcontrolname='description']").fill(article_data["description"])
    sleep(5)
    #authenticated_page.locator("input[formcontrolname='phone']").fill(article_data["phone"])
    #authenticated_page.locator("input[formcontrolname='organization']").fill(article_data["organization"])

    # 5. Заполнение опциональных полей
    # if "orcid" in article_data:
    #     authenticated_page.locator("input[formcontrolname='orcid']").fill(article_data["orcid"])

    # 6. Выбор секции с явным открытием списка
    # 6. Выбор секции без клика, напрямую устанавливаем значение
    select_section = authenticated_page.locator("select[formcontrolname='section']")

    # Выбираем нужную секцию, используя атрибут value или текст
    select_section.select_option(label="Секция 1. «Графические информационные технологии и системы»")
    sleep(5)

    # 7. Загрузка файла
    authenticated_page.locator("input[type='file'][formcontrolname='files']").set_input_files(article_data["file"])

    # 8-10. Отправка и проверки
    submit_button = authenticated_page.locator("button:has-text('Сохранить работу')")
    authenticated_page.wait_for_selector("button:has-text('Сохранить работу'):not([disabled])")

    with authenticated_page.expect_navigation():
        submit_button.click()

    assert authenticated_page.locator(".alert-success").is_visible(), "Ошибка добавления работы"
