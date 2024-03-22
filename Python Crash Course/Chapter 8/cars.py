def cars(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

tesla = cars('tesla', 'Model X', year="2024", color="Purple", price="$1000000")
print("\nTESLA\n")
for key,value in tesla.items():
    print(f"\t{key.title()}: {value.title()}")