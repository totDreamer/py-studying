from datetime import date


class WeatherWarning:
    def rain(self):
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print("Ожидается снег и усиление ветра")

    def low_temperature(self):
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, day):
        print(f"{day.strftime('%d.%m.%Y')}\nОжидаются сильные дожди и ливни с грозой")

    def snow(self, day):
        print(f"{day.strftime('%d.%m.%Y')}\nОжидается снег и усиление ветра")

    def low_temperature(self, day):
        print(f"{day.strftime('%d.%m.%Y')}\nОжидается сильное понижение температуры")


print(issubclass(WeatherWarningWithDate, WeatherWarning))
print()


weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()
print()


weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)
