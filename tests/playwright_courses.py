from playwright.sync_api import Page, expect 

def test_registration(page:Page, context):
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input= page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user_email@gmail.com')

    username_input= page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('someUser')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    courses_text = page.get_by_test_id('courses-list-empty-view-title-text')

    context.storage_state(path='browser-state.json')

    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text('Courses')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('There is no results')




# from playwright.sync_api import Page, expect 

# def test_registration_and_courses(page: Page, context):
#     # --- Шаг 1: Регистрация ---
#     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

#     page.get_by_test_id('registration-form-email-input').locator('input').fill('user_email@gmail.com')
#     page.get_by_test_id('registration-form-username-input').locator('input').fill('someUser')
#     page.get_by_test_id('registration-form-password-input').locator('input').fill('password')
    
#     page.get_by_test_id('registration-page-registration-button').click()

#     # --- Шаг 2: Сохранение состояния ---
#     # Сохраняем куки и локальное хранилище в файл
#     context.storage_state(path='browser-state.json')

#     # --- Шаг 3: Создание НОВОЙ сессии с сохраненным состоянием ---
#     # Это ключевой момент задания. Мы создаем новый изолированный контекст,
#     # но "скармливаем" ему файл с куками, чтобы он был авторизован.
#     new_context = context.browser.new_context(storage_state='browser-state.json')
#     new_page = new_context.new_page()

#     # --- Шаг 4: Работа в новой сессии ---
#     new_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

#     courses_header = new_page.get_by_test_id('courses-list-toolbar-title-text')
#     courses_text = new_page.get_by_test_id('courses-list-empty-view-title-text')

#     # --- Шаг 5: Проверки ---
#     expect(courses_header).to_be_visible()
#     expect(courses_header).to_have_text('Courses')
    
#     expect(courses_text).to_be_visible()
#     expect(courses_text).to_have_text('There is no results')

#     # Хорошая практика: закрываем созданный вручную контекст
#     new_context.close()