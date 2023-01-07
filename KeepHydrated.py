import math
def litres(time):
    liters_per_min = (60 * time) * (1 / 2)
    litres_per_hr = liters_per_min / 60
    liters_per_hr_round = math.floor(litres_per_hr)
    return liters_per_hr_round

for i in [3, 6.7, 11.8]:
    print(litres(i))

def litres(time):
    return int(time // 2)

for i in [3, 6.7, 11.8]:
    print(litres(i))