from bs4 import BeautifulSoup
import urllib3, certifi


# https://hh.ru/search/vacancy?area=1&salary=325000&only_with_salary=true&text=

def search(params): 
    region = '1'
    salary = params['salary']
    if salary == '-':
        salary = ''
    proff = params['proff']

    url = f'https://hh.ru/search/vacancy?area={region}&salary={salary}&only_with_salary=true&text={proff}'

    http = urllib3.PoolManager(ca_certs=certifi.where())
    # создается пул подключения, так же задается сертификат для прохождения TLS/SSL 
    # по протаколу https

    response = http.request('GET', url, redirect=True)
    # ответ от страницы, построенный на get запросе

    meta_resp = http.request('HEAD', url)
    # считываем данные из шапки сайта
    content_type = meta_resp.headers['Content-Type']  # данные о кодировке
    charset = content_type.split('charset=')[1] # кодировка

    data = BeautifulSoup(response.data.decode(charset), 'lxml')
    name = data.find_all('a', attrs={'class': 'bloko-link', 'data-qa': 'vacancy-serp__vacancy-title'})
    pay = data.find_all('span', attrs={'class': "bloko-header-section-3", 'data-qa': "vacancy-serp__vacancy-compensation"})
    reg = data.find_all('div', attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
    #<div data-qa="vacancy-serp__vacancy-address" class="bloko-text">Москва<!-- -->, <span class="metro-station"><span class="metro-point" style="color:#BED12C"></span>Селигерская</span></div>

    description = {}
    c = 0
    for i in range(len(name)):
        if 'удаленно' in name[i].text:
            continue
        c += 1 
        description[c] = (name[i].text, name[i]['href'], pay[i].text, reg[i].text)

    return description