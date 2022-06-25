import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class skyscanner:
    def search(driver, f, t, d, a):
        driver.get('https://www.skyscanner.es/transport/flights/'+f+'/'+t+'/'+d+'/'+a+'/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2')

    def consent_cookies(driver):
        elem = driver.find_element(By.XPATH, '//button[@id="acceptCookieButton"]')
        elem.click()

    def get_cheap_first(driver):
        elem = driver.find_element(By.XPATH, '//button[@class="DangerouslyUnstyledButton_container__NGM5Y DangerouslyUnstyledButton_enabled__ZDg1M FqsTabs_fqsTabWithSparkle__ZjA2Z"]')
        elem.click()

    def check_load(driver):
        try:
            retry_func(driver.find_element, [By.XPATH, '//span[@class="BpkText_bpk-text__YWQwM BpkText_bpk-text--body-default__NGZhN ProgressText_searchingProviderMessage__NjcwY ProgressText_providerName__MjljN"]'], 2, 3)
        except:
            pass


    def get_prices(driver):
        elems = driver.find_elements(By.XPATH, '//span[@class="BpkText_bpk-text__YWQwM BpkText_bpk-text--lg__ODFjM"]')
        return elems
