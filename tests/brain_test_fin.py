import time

from brain_test.model import checks


def test_brain_e2e():
    checks.maximize_window()
    checks.open_browser()
    checks.city_select()
    checks.start_page()
    checks.authorization()
    checks.search_text('Ноутбуки')
    checks.start_page()
    checks.price_sorting()
    checks.filter_by_price()
    checks.filter_check()
    checks.choose_goods()
    checks.add_to_cart()
    checks.check_cart_full()
    checks.delete_goods()
    checks.check_cart_empty()
    checks.my_cabinet()
    checks.change_name()
    checks.verification_name()
    checks.logout()
    time.sleep(2)
    checks.negative_login()
    checks.negative_password()


