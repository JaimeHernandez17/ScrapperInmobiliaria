import os
import time

from celery import chord, group, chain
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.core.mail import send_mail

from ScrapperInmobiliaria.celery import app as celery_app
from apps.scrapperInmobiliaria_app.credentials import EMAIL_FROM


@celery_app.task
def searcher_inmobiliaria_1(route, sector):
    browser = webdriver.Firefox(executable_path=route)

    browser.get('https://www.inmobiliariacartagena.com/arriendo-de-inmuebles-en-cartagena-colombia')
    time.sleep(1)

    browser.find_elements_by_class_name('zelected')[3].click()
    time.sleep(1)
    search_input = browser.find_elements_by_class_name('zearch')[3]
    time.sleep(2)
    search_input.send_keys(sector)
    time.sleep(2)
    browser.find_elements_by_class_name('current')[3].click()
    time.sleep(2)
    browser.find_elements_by_tag_name('button')[1].click()
    time.sleep(2)
    div_list = browser.execute_script("return document.getElementsByClassName('feature_item heading_space')")
    info = ""
    for divv in div_list:
        info += f"{divv.text}\n"
    print(info)
    return info


@celery_app.task
def searcher_inmobiliaria_2(route, sector):
    browser = webdriver.Firefox(executable_path=route)
    try:
        browser.get(
            'https://www.araujoysegovia.com/inmuebles-arriendo/apartamento-en-arriendo-en-cartagena/48/2#/\
            ?page=1&nuevos=0&order_by=destacados&codigo=&ciudad=48&tipo_inmueble=2&tipo_publicacion=arriendo')
        time.sleep(1)

        browser.find_elements_by_class_name('btn dropdown-toggle bs-placeholder btn-default')[0].click()
        time.sleep(1)
        search_input = browser.find_elements_by_class_name('form-control')[0]
        search_input.send_keys(sector)
        time.sleep(1)

        test_list = ['***']
        return test_list
    except:
        pass


@celery_app.task
def searcher_inmobiliaria_3(route, sector):
    browser = webdriver.Firefox(executable_path=route)
    try:
        browser.get('http://bozzimbett.com/inmuebles/negocio/arriendo-5/tipo/apartamento-1/ubicacion/cartagena-20')
        time.sleep(1)

        browser.find_element_by_xpath(f"//select[@name='facets']/option[text()='{sector}']").click()

        test_list = ['***']
        return test_list
    except:
        pass


@celery_app.task
def send_email(apto_list, email):
    message = f'The next apartments has been found:\n'
    for i in apto_list:
        message += f'* {i}\n'
    send_mail(
        'Found apartments',
        message,
        EMAIL_FROM,
        [email],
    )


@celery_app.task
def main(email, sector):
    path = os.path.dirname(os.path.abspath(__file__)).split('apps')
    route = f'{path[0]}Driver/geckodriver'
    tasks_group = [searcher_inmobiliaria_1.s(route, sector), ]
    chord(group(tasks_group), send_email.s(email)).delay()
