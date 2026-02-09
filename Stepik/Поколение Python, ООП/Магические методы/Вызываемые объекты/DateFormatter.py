from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        match self.country_code:
            case "ru" | "fr":
                return d.strftime("%d.%m.%Y")
            case "us":
                return d.strftime("%m-%d-%Y")
            case "ca":
                return d.strftime("%Y-%m-%d")
            case "br":
                return d.strftime("%d/%m/%Y")
            case "pt":
                return d.strftime("%d-%m-%Y")


ru_format = DateFormatter("ru")

print(ru_format(date(2022, 11, 7)))


us_format = DateFormatter("us")

print(us_format(date(2022, 11, 7)))


ca_format = DateFormatter("ca")

print(ca_format(date(2022, 11, 7)))
