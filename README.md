# Skybell

Skybell is a fly scraper that helps the user compare different prices for a given range of possible days for a trip.

## Installation

`$ git clone https://github.com/alejandrocora/skyran`  
`$ cd skyran`  
`$ pip3 install .`  

## Help

Run `skyran --help` for help:
```
usage: skyran [-h] --from FROMP --to TOP --start START --end END [--min-days MIN_DAYS]
              [--max-days MAX_DAYS] [--delay DELAY] [--firefox] [--chrome]

options:
  -h, --help           show this help message and exit
  --from FROMP         Airport code for where you come from.
  --to TOP             Airport code for your destination.
  --start START        Start date (YYYY-MM-DD) for the fly range.
  --end END            End date (YYYY-MM-DD) for the fly range.
  --min-days MIN_DAYS  Minimun quantity of days you wish to stay.
  --max-days MAX_DAYS  Maximun quantity of days you wish to stay.
  --delay DELAY        Delay for search retries.
  --firefox            Use Firefox.
  --chrome             Use Chrome.
```

### Notes

This isn't a serious application, it is just a demonstration. This application uses Skyscanner for scraping, and it usually blocks automated browsers. Author isn't responsible of the given use.
