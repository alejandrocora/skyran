#!/usr/bin/env python3

# Skybell

import os
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sr_lib.get_flies import *
from sr_lib.get_dates import *

global driver
driver = None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from', dest='fromp', type=str, help='Airport code for where you come from.', required=True)
    parser.add_argument('--to', dest='top', type=str, help='Airport code for your destination.', required=True)
    parser.add_argument('--start', type=str, help='Start date (YYYY-MM-DD) for the fly range.', required=True)
    parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD) for the fly range.', required=True)
    parser.add_argument('--min-days', type=int, default=1, help='Minimun quantity of days you wish to stay.')
    parser.add_argument('--max-days', type=int, default=False, help='Maximun quantity of days you wish to stay.')
    parser.add_argument('--delay', type=int, default=60, help='Delay for search retries.')
    parser.add_argument('--firefox', dest='browser', default=False, action='store_false', help='Use Firefox.')
    parser.add_argument('--chrome', dest='browser', action='store_true', help='Use Chrome.')
    args = parser.parse_args()
    frompl = args.fromp.split(',')
    topl = args.top.split(',')
    start_date = args.start
    end_date = args.end
    min_days = args.min_days
    max_days = args.max_days
    delay = args.delay
    browser = args.browser
    priceline = 100
    if not max_days:
        max_days = (date.fromisoformat(end_date) - date.fromisoformat(start_date)).days
    dates = get_dates(date.fromisoformat(start_date), date.fromisoformat(end_date), min_days, max_days)
    for fromp in frompl:
        for top in topl:
            for dep_date in dates:
                for arrival_date in dates[dep_date]:
                    print('Departure Airport -> ' + fromp + ' - Arrival Airport -> ' + top + ', Departure Date -> ' + str(dep_date), '- Arrival Date -> ' + str(arrival_date) + " | Cheapest price -> " + get_flies(browser, skyscanner, fromp, top, dep_date, arrival_date, priceline, delay))

if __name__ == '__main__':
    main()
