from selene import Browser, by, have
from selene.support.shared import browser
import time
from selene.support.shared.jquery_style import s, ss


class BrainFin:
    def __init__(self):
        self.my_URL = 'https://brain.com.ua/ukr/'

    def open_browser(self):
        browser.open('https://brain.com.ua/ukr/')
        return self

    def maximize_window(self):
        browser.driver.maximize_window()
        return self

    def city_select(self, *todos: str):
        s('.mycity.container').click()
        time.sleep(1)
        s('.city_selector').click()
        time.sleep(1)
        return self

    def start_page(self):
        s('[href="/"]').click()
        return self

    def authorization(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14')
        ss('#modal-login-password-field')[0].type('769f3858b5').press_enter()
        s('user-panel-button.active').should(have.exact_text('Едуард'))
        return self

    def search_text(self, checks: str):
        s('#search').type(checks).press_enter()
        return self

    def price_sorting(self):
        s('.price').click()
        s('.price').click()
        return self

    def filter_by_price(self):
        s('.filter').click()
        return self

    def filter_check(self):
        s('.filter').should(have.exact_text('Показати'))
        return self

    def choose_goods(self):
        s(by.text("Ноутбуки і комп'ютери")).click()
        ss(by.text('Перейти'))[0].click()
        s('[data-articul="82KB0006RA"]').click()
        return self

    def add_to_cart(self):
        s('//*[@id="br-pr-2"]/a').click()
        ss('//button[@class="br-checkout modal-checkout"]')[0].click()
        return self

    def check_cart_full(self):
        s('[data-articul="82KB0006RA"]').should(have.exact_text('1'))
        return self

    def delete_goods(self):
        ss('//button[@class="br-ci-remove"]')[1].click()
        s(by.text('Видалити не зберігаючи')).click()
        return self

    def check_cart_empty(self):
        s('[data-articul="82KB0006RA"]').should(have.exact_text('Кошик порожній'))
        return self

    def my_cabinet(self):
        s('user-panel-button.active').click()
        return self

    def change_name(self):
        s('#modal-user-name-field')[0].type('Едуард').press_enter()
        return self

    def verification_name(self):
        s('user-panel-button.active').click()
        return self

    def logout(self):
        s('user-panel-button.active').click()
        return self

    def negative_login(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14').press_tab()
        ss('#modal-login-password-field')[0].type('769f3858b5').press_enter()
        s('.login-error').should(have.exact_text('Некоректний логін'))
        time.sleep(2)
        browser.close()
        return self

    def negative_password(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14').press_enter()
        s('.login-error').should(have.exact_text('Некоректний пароль'))
        time.sleep(2)
        browser.close()
        return self




    # def test_brain():
    #     # відкриваю браузер
    #     browser.open('https://brain.com.ua/ukr/')
    #     # роблю повний екран
    #     browser.driver.maximize_window()
    #     # перехожу для авторизації по кнопці Увійти
    #     ss(by.text('Увійти'))[0].click()
    #     time.sleep(2)
    #     # ввожу в поле телефон номер телефону в повному форматі
    #     ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14').press_tab()
    #     time.sleep(2)
    #     # ввожу в поле пароль
    #     ss('#modal-login-password-field')[0].type('769f3858b5')
    #     time.sleep(2)
    #     # натискаю кнопку Увійти в авторизації
    #     ss(by.text('Увійти'))[2].click()
    #     time.sleep(2)
    #     # обираю категорію товарів Ноутбуки
    #     s(by.text("Ноутбуки і комп'ютери")).click()
    #     time.sleep(2)
    #     # натискаю кнопку Перейти
    #     ss(by.text('Перейти'))[0].click()
    #     time.sleep(2)
    #     # обираю обраний Ноутбук
    #     s('[href="/ukr/Noutbuk_Lenovo_V15_82KB0006RA-p827070.html"]').click()
    #     time.sleep(2)
    #     # захожу в сам ноутбук
    #     s('[data-articul="82KB0006RA"]').click()
    #     time.sleep(1)
    #     # додаю його в кошик
    #     s('//*[@id="br-pr-2"]/a').click()
    #     # заходжу в кошик
    #     ss('//button[@class="br-checkout modal-checkout"]')[0].click()
    #     time.sleep(1)
    #     # збільшую на 1 товар
    #     ss('.increment')[1].click()
    #     time.sleep(1)
    #     # видаляю з кошика товар
    #     ss('//button[@class="br-ci-remove"]')[1].click()
    #     time.sleep(2)
    #     # підтверджую видалення
    #     s(by.text('Видалити не зберігаючи')).click()
    #     time.sleep(2)
    #     # закриваю браузер
    #     browser.quit()
