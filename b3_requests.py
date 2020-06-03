

from selenium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
import requests
import os
import time


url_list_companies = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?idioma=pt-br"
url_search_companies = 'http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Nome={text}&idioma=pt-br'


def get_companies_by_letter(letter):
    global driver

    driver = webdriver.Chrome()
    driver.get(url_list_companies)

    _click_on_letter_menu(letter)
    table_html = _get_table_from_page()
    companies = _get_companies_from_table(table_html)

    driver.close()
    return companies


def search_companies(search):
    global driver

    driver = webdriver.Chrome()
    driver.get(url_search_companies.format(text=search))

    table_html = _get_table_from_page()
    companies = _get_companies_from_table(table_html)

    driver.close()
    return companies


def _click_on_letter_menu(letter):
    letter = letter.upper()
    letter_elem_id = f"ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_lnkCaracter{letter}"

    tries = 0
    while(tries < 2):
        try:

            letter_element = driver.find_element_by_id(letter_elem_id)
            letter_element.click()
            time.sleep(5)

            break
        except exceptions.StaleElementReferenceException:
            tries += 1


def _get_table_from_page():

    table_html = ""

    try:
        table_element = driver.find_element_by_tag_name('table')
        table_html = table_element.get_attribute("innerHTML")
    except exceptions.NoSuchElementException:
        pass

    return table_html


def _get_companies_from_table(table_html):

    table_element = BeautifulSoup(table_html, 'html.parser')
    companies = []

    for tr in table_element.select('tbody tr'):
        company = {}
        company['razao_social'] = tr.select_one('td:first-child a').text
        company['nome_pregao'] = tr.select_one('td:nth-child(2) a').text
        company['segmento'] = tr.select_one('td:last-child').text.strip()
        companies.append(company)

    return companies
