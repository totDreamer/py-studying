from datetime import datetime

pattern = '%d.%m.%Y'
date_list =  [datetime.strptime(d, pattern) for d in input().split()]
dif_list = []

for i in range(len(date_list)-1):
    dif_list.append(abs((date_list[i+1] - date_list[i]).days))

print(dif_list)