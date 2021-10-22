import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

Sig_Eqs = pd.read_csv("./earthquakes-2021-10-13_20-48-52_+0800.tsv", sep="\t")
Sig_Eqs = Sig_Eqs.drop([0])
Sig_Eqs = Sig_Eqs.reset_index(drop=True)

Eqs_total_deaths_top10 = Sig_Eqs.groupby(['Country']).sum().sort_values('Deaths', ascending=False).head(10)

# print(Eqs_total_deaths_top10[['Deaths']])

Sig_Eqs.loc[Sig_Eqs['Mag'] >= 6.0].groupby(['Year']).size().plot(subplots=True)


# plt.show()

def CountEq_LargestEq(country):
    eqs_cnt = Sig_Eqs.loc[Sig_Eqs['Country'] == country].groupby(['Country']).size()
    eqs_cnt = eqs_cnt[0]

    index = Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Mag'].idxmax()

    if np.isnan(index):
        year = str(int(Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Year'].tolist()[0]))
        month = str(int(Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Mo'].tolist()[0])) if np.isnan(
            Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Mo'].tolist()[0]) == False else 'nan'
        day = str(int(Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Dy'].tolist()[0])) if np.isnan(
            Sig_Eqs.loc[Sig_Eqs['Country'] == country]['Dy'].tolist()[0]) == False else 'nan'
    else:
        year = str(int(Sig_Eqs.iloc[index]['Year']))
        month = str(int(Sig_Eqs.iloc[index]['Mo'])) if np.isnan(Sig_Eqs.iloc[index]['Mo']) == False else 'nan'
        day = str(int(Sig_Eqs.iloc[index]['Dy'])) if np.isnan(Sig_Eqs.iloc[index]['Dy']) == False else 'nan'

    date = year+'-'+month+'-'+day
    return eqs_cnt, date


countries = Sig_Eqs.drop_duplicates(subset=['Country'], keep='first')['Country'].tolist()
cnts = []
dates = []
for country in countries:
    cnt, date = CountEq_LargestEq(country)
    cnts.append(cnt)
    dates.append(date)

mag_df = pd.DataFrame({'Country': countries, 'total_eqs': cnts, 'maxMag_date': dates}).sort_values('total_eqs', ascending=False)

mag_df.to_csv('mag_df.csv')
