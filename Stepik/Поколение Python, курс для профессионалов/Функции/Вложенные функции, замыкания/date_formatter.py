from datetime import date
def date_formatter(country_code: str):
    def formatter(d: date):
        locale = {
            'ru': '%d.%m.%Y',
            'us': '%m-%d-%Y',
            'ca': '%Y-%m-%d',
            'br': '%d/%m/%Y',
            'fr': '%d.%m.%Y',
            'pt': '%d-%m-%Y'
                }
        return d.strftime(locale[country_code])
    return formatter

date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))

date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))