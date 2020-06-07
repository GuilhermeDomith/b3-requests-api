import requests
from bs4 import BeautifulSoup


url = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx"


def get_companies_by_letter(letter):

    query = f'?Letra={letter}&idioma=pt-br'
    resp = requests.get(url + query)

    companies = _get_companies_from_page(resp.content)

    return companies


def search_companies(search):

    query = f'?Nome={search}&idioma=pt-br'
    resp = requests.get(url + query)

    companies = _get_companies_from_page(resp.content)

    return companies


def _get_companies_from_page(page_html):

    companies = []

    soup = BeautifulSoup(page_html, 'html.parser')
    table_companies = soup.select_one('table')

    if(table_companies):
        for tr in table_companies.select('tbody tr'):
            company = {
                'razao_social': tr.select_one('td:first-child a').text,
                'nome_pregao': tr.select_one('td:nth-child(2) a').text,
                'segmento': tr.select_one('td:last-child').text.strip()
            }

            companies.append(company)

    return companies
