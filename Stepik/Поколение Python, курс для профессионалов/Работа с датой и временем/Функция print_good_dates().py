from datetime import date

def print_good_dates(dates):
    good_dates = []

    for d in sorted(dates):
        if d.year == 1992 and d.day + d.month == 29:
            good_dates.append(d.strftime('%B %d, %Y'))
    
    return good_dates

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print(*print_good_dates(dates), sep='\n')
