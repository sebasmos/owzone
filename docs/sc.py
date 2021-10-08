# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
rate, ozone concentration, battery level, and oxygen level. 

i.e: flow(Gr/h), 
time ((1 ppbv)), 
volume (1 ppbv - parts per billion by volume),
ozone (Dobson (U.D.)). 
"""

import pandas as pd 
import random
import datetime

def norm_factors(x):
    norm = []
    minimo = min(x)
    maximo = max(x)
    norm = (maximo - minimo)/ (maximo + minimo)
    return minimo, maximo, norm


tday = datetime.datetime(2021, 1, 1, 00, 00, 00)
# Fecha: 
Fecha = []
#  flow(Gr/h)
flujo = []
# Volume ppbv
volume = []
# O2 level
o2 = []
# Batery level
battery = []
# Temperature
temp = []
# Risk target value 
target = []
prob = [1,2,3,4,5,6]

deltameasure=datetime.timedelta(minutes=5)

for i in range(100):
    #Flujo
    f = random.uniform(60,70)
    flujo.append(f)
    #Volumen
    v = random.uniform(0,80)
    volume.append(v)
    #Volumen
    ox = random.uniform(60,70)
    o2.append(ox)
    #batery
    bat = random.uniform(1,10)
    battery.append(bat)
    #Temperatura
    t = random.uniform(10,40)
    temp.append(t)
    # Variable objetivo: 
    a = random.choice(prob)
    target.append(a)
    # Fecha
    Fecha.append(tday)
    tday += deltameasure
    print(tday)

columns_names = {'fecha':Fecha, 
                 'flujo': flujo,
                 'Volume':volume,
                 'Oxygen_level':o2,
                 'Battery':battery,
                 'Temp': temp,
                 'riesgo':target}
# Save to csv file
import os
if not os.path.exists("../data"):
    os.makedirs("../data")
df = pd.DataFrame(data=columns_names)
df.to_csv('../data/owzone.csv', sep=',', index=False)
print(df)
