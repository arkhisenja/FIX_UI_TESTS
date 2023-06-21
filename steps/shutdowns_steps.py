import time

from behave import *

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


@given('открыт сайт')
def open_url(context):
    driver.get("https://open.kzn.ru/shutdowns")


@when('в поле Улица ввели значение Павлюхина и сохранили его')
def enter_street(context):
    street_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "street"))
    )

    street_input.send_keys('Павлюхина')
    time.sleep(2)

    street_input.send_keys(Keys.ARROW_DOWN)
    street_input.send_keys(Keys.ENTER)


@when('в поле Дом ввели значение 100 и сохранили его')
def enter_house(context):
    house_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "house"))
    )
    house_input.send_keys('100')
    time.sleep(2)

    house_input.send_keys(Keys.ARROW_DOWN)
    house_input.send_keys(Keys.ENTER)


@when('в поле Квартира ввели значение 10 и сохранили его')
def enter_flat(context):
    flat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "flat"))
    )
    flat_input.send_keys('10')
    time.sleep(2)

    flat_input.send_keys(Keys.ARROW_DOWN)
    flat_input.send_keys(Keys.ENTER)


@then("В списке результатов появились сообщения об отключениях")
def check_positive_result(context):
    time.sleep(5)
    assert "Объявления управляющей организации" in driver.page_source, "Объявления управляющей организации не найдено"
    assert "Отключение горячего водоснабжения" in driver.page_source, "Отключение горячего водоснабжения не найдено"


@then("В списке результатов не найдены сообщения об отключениях")
def check_negative_result(context):
    time.sleep(5)
    assert "По данному адресу отключений нет" in driver.page_source, "Сообщения нет на странице"


@when("в поле Дом ввели значение 85(УК) и сохранили его")
def step_impl(context):
    house_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "house"))
    )
    house_input.send_keys('85(УК)')
    time.sleep(2)

    house_input.send_keys(Keys.ARROW_DOWN)
    house_input.send_keys(Keys.ENTER)
