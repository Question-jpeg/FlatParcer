from utils import editConfig, ExcelWorker
from executor import makeRow
import configparser
import traceback

try:

    # DECLARATION
    config = configparser.ConfigParser()
    config.read('cache.ini', encoding="utf-8")

    iterations = [
        {
            'common': {
                'sheetName': 'Москва', 
                'cacheSection': 'МОСКВА',
                'selectionSection': 'МОСКВА-ШАГИ'
            }, 
            'steps': [
                {
                    'url': 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=1&sort=price_square_order',
                    'fileName': 'Купить',
                    'select': 'москва продажа',
                    'type': 'buy',
                    'cacheSection': 'МОСКВА-КУПИТЬ',
                    'oldCacheSection': 'МОСКВА-КУПИТЬ-СТАРЫЕ',
                    'middleCacheSection': 'МОСКВА-КУПИТЬ-СРЕДНИЕ',
                    'newCacheSection': 'МОСКВА-КУПИТЬ-НОВЫЕ'
                }, 
                {
                    'url': 'https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=1&type=4&sort=price_object_order',
                    'fileName': 'Снять',
                    'select': 'москва аренда',
                    'type': 'rent',
                    'cacheSection': 'МОСКВА-СНЯТЬ',
                    'oldCacheSection': 'МОСКВА-СНЯТЬ-СТАРЫЕ',
                    'middleCacheSection': 'МОСКВА-СНЯТЬ-СРЕДНИЕ',
                    'newCacheSection': 'МОСКВА-СНЯТЬ-НОВЫЕ'
                }
            ]
        },
        {
            'common': {
                'sheetName': 'Петербург', 
                'cacheSection': 'ПЕТЕРБУРГ',
                'selectionSection': 'ПЕТЕРБУРГ-ШАГИ',
            }, 
            'steps': [
                {
                    'url': 'https://spb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=2&sort=price_square_order',
                    'fileName': 'Купить',
                    'select': 'петербург продажа',
                    'type': 'buy',
                    'cacheSection': 'ПЕТЕРБУРГ-КУПИТЬ',
                    'oldCacheSection': 'ПЕТЕРБУРГ-КУПИТЬ-СТАРЫЕ',
                    'middleCacheSection': 'ПЕТЕРБУРГ-КУПИТЬ-СРЕДНИЕ',
                    'newCacheSection': 'ПЕТЕРБУРГ-КУПИТЬ-НОВЫЕ'
                }, 
                {
                    'url': 'https://spb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=2&type=4&sort=price_object_order',
                    'fileName': 'Снять',
                    'select': 'петербург аренда',
                    'type': 'rent',
                    'cacheSection': 'ПЕТЕРБУРГ-СНЯТЬ',
                    'oldCacheSection': 'ПЕТЕРБУРГ-СНЯТЬ-СТАРЫЕ',
                    'middleCacheSection': 'ПЕТЕРБУРГ-СНЯТЬ-СРЕДНИЕ',
                    'newCacheSection': 'ПЕТЕРБУРГ-СНЯТЬ-НОВЫЕ'
                }
            ]
        },
        {
            'common': {
                'sheetName': 'Сочи', 
                'cacheSection': 'СОЧИ',
                'selectionSection': 'СОЧИ-ШАГИ',
                'districtSection': 'СОЧИ--РАЙОНЫ'
            }, 
            'steps': [
                {
                    'url': 'https://sochi.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=4998&sort=price_square_order',
                    'fileName': 'Купить',
                    'select': 'сочи продажа',
                    'type': 'buy',
                    'cacheSection': 'СОЧИ-КУПИТЬ',
                    'oldCacheSection': 'СОЧИ-КУПИТЬ-СТАРЫЕ',
                    'middleCacheSection': 'СОЧИ-КУПИТЬ-СРЕДНИЕ',
                    'newCacheSection': 'СОЧИ-КУПИТЬ-НОВЫЕ'
                }, 
                {
                    'url': 'https://sochi.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4998&type=4&sort=price_object_order',
                    'fileName': 'Снять',
                    'select': 'сочи аренда',
                    'type': 'rent',
                    'cacheSection': 'СОЧИ-СНЯТЬ',
                    'oldCacheSection': 'СОЧИ-СНЯТЬ-СТАРЫЕ',
                    'middleCacheSection': 'СОЧИ-СНЯТЬ-СРЕДНИЕ',
                    'newCacheSection': 'СОЧИ-СНЯТЬ-НОВЫЕ'
                }
            ]
        },
        {
            'common': {
                'sheetName': 'Иркутск', 
                'cacheSection': 'ИРКУТСК',
                'selectionSection': 'ИРКУТСК-ШАГИ',
                'districtSection': 'ИРКУТСК--РАЙОНЫ'
            }, 
            'steps': [
                {
                    'url': 'https://irkutsk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=4774&sort=price_square_order',
                    'fileName': 'Купить',
                    'select': 'иркутск продажа',
                    'type': 'buy',
                    'cacheSection': 'ИРКУТСК-КУПИТЬ',
                    'oldCacheSection': 'ИРКУТСК-КУПИТЬ-СТАРЫЕ',
                    'middleCacheSection': 'ИРКУТСК-КУПИТЬ-СРЕДНИЕ',
                    'newCacheSection': 'ИРКУТСК-КУПИТЬ-НОВЫЕ'
                }, 
                {
                    'url': 'https://irkutsk.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4774&type=4&sort=price_object_order',
                    'fileName': 'Снять',
                    'select': 'иркутск аренда',
                    'type': 'rent',
                    'cacheSection': 'ИРКУТСК-СНЯТЬ',
                    'oldCacheSection': 'ИРКУТСК-СНЯТЬ-СТАРЫЕ',
                    'middleCacheSection': 'ИРКУТСК-СНЯТЬ-СРЕДНИЕ',
                    'newCacheSection': 'ИРКУТСК-СНЯТЬ-НОВЫЕ'
                }
            ]
        },
        {
            'common': {
                'sheetName': 'Краснодар', 
                'cacheSection': 'КРАСНОДАР',
                'selectionSection': 'КРАСНОДАР-ШАГИ',
                'districtSection': 'КРАСНОДАР--РАЙОНЫ'
            }, 
            'steps': [
                {
                    'url': 'https://krasnodar.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=4820&sort=price_square_order',
                    'fileName': 'Купить',
                    'select': 'краснодар продажа',
                    'type': 'buy',
                    'cacheSection': 'КРАСНОДАР-КУПИТЬ',
                    'oldCacheSection': 'КРАСНОДАР-КУПИТЬ-СТАРЫЕ',
                    'middleCacheSection': 'КРАСНОДАР-КУПИТЬ-СРЕДНИЕ',
                    'newCacheSection': 'КРАСНОДАР-КУПИТЬ-НОВЫЕ'
                }, 
                {
                    'url': 'https://krasnodar.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4820&type=4&sort=price_object_order',
                    'fileName': 'Снять',
                    'select': 'краснодар аренда',
                    'type': 'rent',
                    'cacheSection': 'КРАСНОДАР-СНЯТЬ',
                    'oldCacheSection': 'КРАСНОДАР-СНЯТЬ-СТАРЫЕ',
                    'middleCacheSection': 'КРАСНОДАР-СНЯТЬ-СРЕДНИЕ',
                    'newCacheSection': 'КРАСНОДАР-СНЯТЬ-НОВЫЕ'
                }
            ]
        },
    ]

    # CONFIGURATION
    editConfig(config)

    saleExcelWorker = ExcelWorker('Купить')
    rentExcelWorker = ExcelWorker('Снять')

    for iteration in iterations:
        makeRow(config, iteration, saleExcelWorker, rentExcelWorker)

    saleExcelWorker.close()
    rentExcelWorker.close()

except Exception:
    traceback.print_exc()
input('\nРабота завершена. Нажмите enter чтобы выйти\n')

