import arrow, sys

dates = [arrow.get(date, 'DD.MM.YYYY') for date in sys.stdin]
asc_dates = sorted(dates)
desc_dates = sorted(dates, reverse=True)

if dates == asc_dates and len(dates)==len(set(asc_dates)):
    print('ASC')
elif dates == desc_dates and len(dates)==len(set(desc_dates)):
    print('DESC')
else:
    print('MIX')