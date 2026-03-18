class EasyDict(dict):
    def __getattr__(self, attr):
        if attr not in self.__dict__:
            try:
                return self[f"{attr}"]
            except Exception:
                raise


easydict = EasyDict({"name": "Timur", "city": "Moscow"})

print(easydict["name"])
print(easydict.city)
print()


easydict = EasyDict({"name": "Timur", "city": "Moscow"})

easydict["city"] = "Dubai"
easydict["age"] = 30
print(easydict.city)
print(easydict.age)
print()


easydict = EasyDict({"name": "Artur", "city": "Almetevsk"})

easydict.age = 21
print(easydict)
