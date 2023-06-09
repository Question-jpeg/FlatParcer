# from configparser import ConfigParser
# from requests.models import PreparedRequest
# from utils import getResponse, retrieveCount
# from bs4 import BeautifulSoup
# import math

# config = ConfigParser()
# config.read('cache.ini', encoding="utf-8")
# print(config['МОСКВА']['до метро (мин)'])

# multipleOptionMappings = [
#     {'urlParam': 'a', 'values': ['a', 'b']}, 
#     {'urlParam': 'b', 'values': ['b', 'c']},
#     {'urlParam': 'c', 'values': ['c', 'd']},
# ]
# opts = []
# trace = [{'urlParam': 'test', 'value': 'test'}]
# def rec(j):

#     if j >= len(multipleOptionMappings):
#         opts.append([] + trace)
#         return

#     for i in range(len(multipleOptionMappings[j]['values'])):
#         trace.append({'urlParam': multipleOptionMappings[j]['urlParam'], 'value': multipleOptionMappings[j]['values'][i]})
#         rec(j+1)
#         trace.pop()

# rec(0)
# print(opts)
# print(len(opts))

# print('да'.split(' '))
# print(list(filter(lambda l: l == 1, [1, 2, 3]))[0])

# urlParam = 'repair%5B0%5D'
# request = PreparedRequest()
# request.prepare_url('https://google.com', {'': 'chicha'})

# print({'': 'passed'}[''])
# print(request.url)
# print(5000*71)

# print({request.url: 'test'})

# url = 'https://irkutsk.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4774&type=4&sort=price_object_order'
# soup = BeautifulSoup(getResponse(url, {}).text, 'html.parser')
# summary = soup.select_one('div[data-name="SummaryHeader"]')
# total_count = retrieveCount(summary.text)
# target_listing = math.ceil(total_count / 2)
# listings = soup.select('article[data-name="CardComponent"]')
# count_on_page_avg = len(listings)
# target_page = math.ceil(target_listing / count_on_page_avg)
# print(f'Объявлений на странице: {count_on_page_avg}')
# print(f'Искомая цена на странице № {target_page}\n' )

# if target_page != 1:
#     soup = BeautifulSoup(getResponse(url, {'p': target_page}).text, 'html.parser')
#     listings = soup.select('article[data-name="CardComponent"]')

# count_on_page = len(listings)
# target_listing_index = target_listing - 1
# min_index_of_total_on_page = count_on_page_avg * (target_page-1)
# to_pick_index = target_listing_index - min_index_of_total_on_page

# price_text = listings[to_pick_index].select_one('span[data-mark="MainPrice"]').text
# print(f'Искомая цена найдена: {retrieveCount(f"Цена: {price_text}")}')

print(list({'a': 1, 'b': 2}.values()))