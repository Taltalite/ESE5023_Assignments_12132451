import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def extractDPData():
    df = pd.read_csv("./gsoy.csv", low_memory=False)

    dp_df = df[['STATION', 'DATE', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'NAME', 'DP01', 'DP01_ATTRIBUTES', 'DP10',
                'DP10_ATTRIBUTES', 'DP1X', 'DP1X_ATTRIBUTES', 'EMXP', 'EMXP_ATTRIBUTES', 'PRCP', 'PRCP_ATTRIBUTES']]

    dp_df.to_csv('./dp_gsoy.csv')


if __name__ == "__main__":
    # extractDPData() runs once is enough
    extractDPData()

    dp_df = pd.read_csv("./dp_gsoy.csv")
    dp_df.dropna(inplace=True)

    station = "ASN00077034"

    station_dp_df = dp_df.loc[dp_df['STATION'] == station]

    plt.figure(1)
    plt.title('Station: %s PRCP Plot' % station)
    plt.plot(station_dp_df['DATE'], station_dp_df['PRCP'], 'o-')
    plt.xlabel('Date')
    plt.ylabel('PRCP')
    plt.plot()

    # 2020 rain fall statistic
    year = '2020'

    year_dp_df = dp_df.loc[dp_df['DATE'] == year]

    year_longibase_avg_dp_df = dp_df.groupby(['LONGITUDE']).mean().reset_index()
    year_latibase_avg_dp_df = dp_df.groupby(['LATITUDE']).mean().reset_index()

    plt.figure(2)
    plt.title('year: %s Longitude Based DP10 with Polyfit Plot' % year)
    plt.scatter(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP10'])
    data_x = np.array(year_longibase_avg_dp_df['LONGITUDE'].to_list())
    data_y = np.array(year_longibase_avg_dp_df['DP10'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Longitude')
    plt.ylabel('DP10')
    plt.plot(data_x, y_value, c='red')

    plt.figure(3)
    plt.title('year: %s Longitude Based DP1X with Polyfit Plot' % year)
    plt.scatter(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP1X'])
    data_x = np.array(year_longibase_avg_dp_df['LONGITUDE'].to_list())
    data_y = np.array(year_longibase_avg_dp_df['DP1X'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Longitude')
    plt.ylabel('DP1X')
    plt.plot(data_x, y_value, c='red')

    plt.figure(4)
    plt.title('year: %s Longitude Based PRCP with Polyfit Plot' % year)
    # plt.plot(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP10'], 'o-')
    plt.scatter(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['PRCP'])
    data_x = np.array(year_longibase_avg_dp_df['LONGITUDE'].to_list())
    data_y = np.array(year_longibase_avg_dp_df['PRCP'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Longitude')
    plt.ylabel('PRCP')
    plt.plot(data_x, y_value, c='red')

    plt.figure(5)
    plt.title('year: %s Latitude Based DP10 with Polyfit Plot' % year)
    # plt.plot(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP10'], 'o-')
    plt.scatter(year_latibase_avg_dp_df['LATITUDE'], year_latibase_avg_dp_df['DP10'])
    data_x = np.array(year_latibase_avg_dp_df['LATITUDE'].to_list())
    data_y = np.array(year_latibase_avg_dp_df['DP10'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Latitude')
    plt.ylabel('DP10')
    plt.plot(data_x, y_value, c='red')

    plt.figure(6)
    plt.title('year: %s Latitude Based DP1X with Polyfit Plot' % year)
    # plt.plot(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP10'], 'o-')
    plt.scatter(year_latibase_avg_dp_df['LATITUDE'], year_latibase_avg_dp_df['DP1X'])
    data_x = np.array(year_latibase_avg_dp_df['LATITUDE'].to_list())
    data_y = np.array(year_latibase_avg_dp_df['DP1X'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Latitude')
    plt.ylabel('DP1X')
    plt.plot(data_x, y_value, c='red')

    plt.figure(7)
    plt.title('year: %s Latitude Based PRCP with Polyfit Plot' % year)
    # plt.plot(year_longibase_avg_dp_df['LONGITUDE'], year_longibase_avg_dp_df['DP10'], 'o-')
    plt.scatter(year_latibase_avg_dp_df['LATITUDE'], year_latibase_avg_dp_df['PRCP'])
    data_x = np.array(year_latibase_avg_dp_df['LATITUDE'].to_list())
    data_y = np.array(year_latibase_avg_dp_df['PRCP'].to_list())
    poly = np.polyfit(data_x, data_y, deg=15)
    y_value = np.polyval(poly, data_x)

    plt.xlabel('Latitude')
    plt.ylabel('PRCP')
    plt.plot(data_x, y_value, c='red')

    plt.show()
