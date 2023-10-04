from time import sleep

from brain_test.model import checks


def test_brain_e2e():
    checks.open_browser()
    checks.city_select()
    checks.start_page()
    checks.authorization()
    checks.search_text('ноутбуки')
    checks.check_visible()
    checks.start_page()
    checks.choose_goods()
    checks.price_sorting()
    sleep(2)
    checks.verification_price()
    sleep(2)
    checks.filter_by_producer()
    checks.filter_check_note()
    checks.filter_check_show()
    sleep(2)
    checks.choose_one_good()
    checks.add_to_cart()
    checks.check_cart_full()
    sleep(2)
    checks.delete_goods()
    sleep(2)
    checks.check_cart_empty()
    checks.my_cabinet()
    sleep(2)
    checks.logout()
    sleep(5)
    checks.negative_login()
    sleep(2)
    checks.open_browser()
    checks.negative_password()
    sleep(3)

