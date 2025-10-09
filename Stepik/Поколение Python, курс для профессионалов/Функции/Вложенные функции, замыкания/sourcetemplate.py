def sourcetemplate(url: str):
    def params(**kwargs):
        if kwargs:
            return url + '?' + '&'.join(f"{key}={value}" for key, value in sorted(kwargs.items()))
        return url
    return params



url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))