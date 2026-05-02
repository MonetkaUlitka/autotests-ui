from playwright.sync_api import Page, expect 

def test_keyboard_actions(page:Page):
     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

     email_input = page.get_by_test_id('login-form-email-input').locator('input')
    #  email_input.focus()
    # По символу имитируем нажатия клавиш для ввода текста
    #  for character in 'user@gmail.com':
    #     # Добавляем задержку 300 мс для имитации реального ввода
    #     page.keyboard.press(character, delay=300)

    # # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    #  page.keyboard.press("ControlOrMeta+A")
    
    # # Ждём 5 секунд для наглядности результата
    #  page.wait_for_timeout(5000)


# Мой альтернативный вариант:
     email_input.type('user@gmail.com', delay=300)
     page.keyboard.press("ControlOrMeta+A")