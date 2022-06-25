from datetime import date
from datetime import timedelta

def get_dates(min_depdate, max_arrivaldate, min_dayrange, max_dayrange):
    max_depdate = None
    if not max_depdate:
        max_depdate = max_arrivaldate - timedelta(min_dayrange)
    if (min_depdate > max_depdate):
        print("There is no possible range of days for the set dates of departure and arrival dates.")
    i_depdate = min_depdate
    dates = {}
    while i_depdate <= max_depdate:
        dates[i_depdate] = []
        for days in range(min_dayrange-1, max_dayrange):
            i_arrivaldate = i_depdate + timedelta(days)
            if i_arrivaldate <= max_arrivaldate:
                dates[i_depdate].append(i_arrivaldate)
        i_depdate += timedelta(1)
    return dates
