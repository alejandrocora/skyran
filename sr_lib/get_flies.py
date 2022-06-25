import numpy as np
from time import sleep

from sr_lib.retry import *
from sr_lib.selaux import *
from sr_lib.skyscanner import *

def get_flies(browser, site, fromp, top, dep, arrival, priceline, delay):
    dep = str(dep.strftime("%y%m%d"))
    arrival = str(arrival.strftime("%y%m%d"))
    prices = []
    attempts = 0
    while attempts < 10:
        try:
            if not browser:
                driver = headless_firefox()
            else:
                driver = headless_chrome()
            retry_func(site.search, [driver, fromp, top, dep, arrival], 5, 2)
            sleep(1)
            retry_func(site.consent_cookies, driver, 5, 2)
            sleep(1)
            retry_func(site.get_cheap_first, driver, 5, 2)
            sleep(1)
            site.check_load(driver)
            sleep(1)
            elems = site.get_prices(driver)
            if not elems:
                site.get_cheap_first(driver)
            for elem in elems:
                prices.append(int(elem.text[:-2].replace('.', '')))
            attempts = 10
        except Exception as E:
            if ("https://www.skyscanner.es/sttc/px/captcha-v2/index.html?" in driver.current_url):
                driver.close()
                driver = None
                attempts += 1
                sleep(delay)
            else:
                print(E)
    if prices:
        return str(np.array(prices).min())
    else:
        return ""
