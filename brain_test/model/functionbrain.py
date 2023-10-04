from selene import Browser, by, have, be
from selene.support.shared import browser
from time import sleep
from selene.support.shared.jquery_style import s, ss


class BrainFin:
    def __init__(self):
        self.my_URL = 'https://brain.com.ua/ukr/'

    def open_browser(self):
        browser.open('https://brain.com.ua/ukr/')
        browser.driver.maximize_window()
        return self

    def city_select(self, *todos: str):
        s('.mycity_container.mycity.mycityname[data-cityid="23562"]').click()
        sleep(1)
        s(by.text('Кременчук')).click()
        sleep(1)
        return self

    def start_page(self):
        s('[href="/"]').click()
        return self

    def authorization(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14')
        sleep(1)
        ss('#modal-login-password-field')[0].type('769f3858b5').press_enter()
        s('.user-panel-button.active').should(have.exact_text('Едуард'))
        return self

    def search_text(self, checks: str):
        ss('input.quick-search-input')[1].type(checks).press_enter()
        return self

    def check_visible(self):
        element = s('.search-products-count')
        element.should(be.visible)
        return self

    def price_sorting(self):
        ss(by.text('Сортування за ціною'))[0].click()
        s('[href="/ukr/category/Noutbuky-c1191/order=asc;sortby=price/"]').click()
        return self

    def verification_price(self):
        ss(by.text('Ціна: Від дешевих до дорогих'))[0].click()
        return self
    def filter_by_producer(self):
        ss('div.filter__title')[2].click()
        return self

    def filter_check_note(self):
        s('[data-filter="3-75002600000"]').click()
        return self

    def filter_check_show(self):
        ss('.use_filter_link')[0].click()
        return self

    def choose_goods(self):
        s(by.text("Ноутбуки і комп'ютери")).click()
        ss(by.text('Перейти'))[0].click()
        return self

    def choose_one_good(self):
        s('[href="/ukr/Noutbuk_Lenovo_V15_82KB0006RA-p827070.html"]').click()
        s('[data-articul="82KB0006RA"]').click()
        return self

    def add_to_cart(self):
        s('//*[@id="br-pr-2"]/a').click()
        ss('//button[@class="br-checkout modal-checkout"]')[0].click()
        return self

    def check_cart_full(self):
        s('.cart-button.user-cart-count.cart_custom_styles.not_empty').should(have.exact_text('1'))
        return self

    def delete_goods(self):
        s('.cart-button.user-cart-count.cart_custom_styles.not_empty').click()
        ss('//button[@class="br-ci-remove"]')[1].click()
        s(by.text('Видалити не зберігаючи')).click()
        return self

    def check_cart_empty(self):
        s('.br-ch-block.br-cart-empty').should(have.exact_text('Ваш кошик порожній.'))
        return self

    def my_cabinet(self):
        s(by.text('Едуард')).click()
        ss(by.text('Персональні дані'))[0].click()
        s('input#profile-firstname-input.br-prof-form-item').clear()
        sleep(1)
        s('input#profile-firstname-input.br-prof-form-item').type('Едгар')
        sleep(1)
        s('[value="1971"]').click()
        s('.br-prof-form-submit.update-profile-btn').click()
        ss('//button[@class="close"][@data-dismiss="modal"]')[8].click()
        return self

    def logout(self):
        s('.user-panel-button.active').click()
        s('.logout').click()
        return self

    def negative_login(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-')
        ss('#modal-login-password-field')[0].type('769f3858b5').press_enter()
        s('div.login-error').should(have.exact_text('Некоректний телефон'))
        sleep(2)
        browser.quit()


    def negative_password(self):
        ss(by.text('Увійти'))[0].click()
        ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14')
        ss('#modal-login-password-field')[0].type('769f3858').press_enter()
        s('.login-error').should(have.exact_text('Некоректний пароль'))
        sleep(2)
        browser.close()
