import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

Shenzhen_windspeed = pd.read_csv("./2281305.csv", low_memory=False)

wnd = Shenzhen_windspeed['WND'].tolist()
windspeed = pd.DataFrame(columns=('SR', 'SQC'))

date = pd.to_datetime(Shenzhen_windspeed['DATE'])

sr = []
sqc = []
for i in range(len(wnd)):
    temp = wnd[i].split(',')
    sr.append(temp[3])
    sqc.append(temp[4])
windspeed['SR'] = sr
windspeed['SQC'] = sqc

monthly_avg_wind_speed = pd.DataFrame(columns=('DATE', 'AVG_WIND_SPEED'))
scale = 10
cnt = 0
speed_sum = 0
old_mo = date[0].month
old_year = date[0].year
row = 0
for i in range(date.size):
    if windspeed.iloc[i]['SQC'] == '9' and windspeed.iloc[i]['SR'] == '9999':
        continue
    cur_year = date[i].year
    cur_mo = date[i].month
    if cur_year == old_year and cur_mo == old_mo:
        cnt += 1
        speed_sum += int(windspeed.iloc[i]['SR']) / scale
    else:
        avg_speed = speed_sum / cnt
        monthly_avg_wind_speed.loc[row] = [datetime.datetime.strptime(str(old_year)+str(old_mo), "%Y%m"), avg_speed]
        row += 1
        cnt = 1
        speed_sum = int(windspeed.iloc[i]['SR']) / scale
        old_mo = cur_mo
        old_year = cur_year
if cnt != 1:
    avg_speed = speed_sum / cnt
    monthly_avg_wind_speed.loc[row] = [datetime.datetime.strptime(str(old_year) + str(old_mo), "%Y%m"), avg_speed]


plt.title('Shenzhen Monthly Avg Wind Speed')
plt.plot(monthly_avg_wind_speed['DATE'], monthly_avg_wind_speed['AVG_WIND_SPEED'],'o-')
plt.xlabel('Date')
plt.ylabel('Avg wind speed')
plt.show()

