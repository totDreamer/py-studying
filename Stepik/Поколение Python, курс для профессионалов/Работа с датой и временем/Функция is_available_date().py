from datetime import datetime, timedelta

def unpack_dates(days_list):
    all_days = []

    for d in days_list:
        if '-' in d:
            start_str, end_str = d.split('-')
            start_date = datetime.strptime(start_str, '%d.%m.%Y').date()
            end_date = datetime.strptime(end_str, '%d.%m.%Y').date()

            while start_date <= end_date:
                all_days.append(start_date)
                start_date += timedelta(days=1)

        else:
            day = datetime.strptime(d, '%d.%m.%Y').date()
            all_days.append(day)

    return set(all_days)

def is_available_date(booked_dates, date_for_booking):
    if isinstance(date_for_booking, str):
        date_for_booking = [date_for_booking]

    booked = unpack_dates(booked_dates)
    required_dates = unpack_dates(date_for_booking)
    return all(day not in booked for day in required_dates)

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))