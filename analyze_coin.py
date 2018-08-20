import requests
import pandas
import json
import datetime
import matplotlib.pyplot

# Graph embed stuff
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Globals
output = ""

def get_dataframe_of(symbol, track_type, limit=30):
    if track_type == "daily":
        url = "https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit={}".format(symbol, limit)
        response = requests.get(url)
        # Get JSON from the url
        data = json.loads(response.text)

        # Get DataFrame from the JSON Object
        df = pandas.DataFrame.from_dict(data['Data'])
        df['time'] = pandas.to_datetime(df['time'], unit='s')
        df.set_index(['time'], inplace=True)
        df = pandas.DataFrame(df['close'], index=df.index)
        df.columns = [symbol]
        return df
    elif track_type == "minute":
        url = "https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym=USD&limit={}".format(symbol, limit)
        response = requests.get(url)
        # Get JSON from the url
        data = json.loads(response.text)
        df = pandas.DataFrame.from_dict(data['Data'])
        df['time'] = pandas.to_datetime(df['time'], unit='s').dt.time
        df.set_index(['time'], inplace=True)
        df = pandas.DataFrame(df['close'], index=df.index)
        df.columns = [symbol]

        return df

def analyze(maincoin="", othercoin="", window=None, track_type="daily", limit=30 ):
    global output

    # if maincoin == "XEM":
    #     maincoin = "NEM"
    # if othercoin == "XEM":
    #     othercoin = "NEM"

    btc_df = get_dataframe_of('BTC', track_type=track_type, limit=limit)
    bcc_df = get_dataframe_of('BCC', track_type=track_type, limit=limit)
    dash_df = get_dataframe_of('DASH', track_type=track_type, limit=limit)
    doge_df = get_dataframe_of('DOGE', track_type=track_type, limit=limit)
    eth_df = get_dataframe_of('ETH', track_type=track_type, limit=limit)
    ltc_df = get_dataframe_of('LTC', track_type=track_type, limit=limit)
    nxt_df = get_dataframe_of('NXT', track_type=track_type, limit=limit)
    str_df = get_dataframe_of('STR', track_type=track_type, limit=limit)
    nem_df = get_dataframe_of('XEM', track_type=track_type, limit=limit)
    xrp_df = get_dataframe_of('XRP', track_type=track_type, limit=limit)

    maindf = pandas.concat([btc_df, bcc_df, dash_df, doge_df, eth_df, ltc_df, nxt_df, str_df, nem_df, xrp_df], axis=1)
    # maindf.to_csv('CryptocurrenciesDataFrame.csv')

    # maindf = pandas.DataFrame.from_csv('CryptocurrenciesDataFrame.csv')
    # maindfcorr = maindf.corr()
    # maindfcorr.to_csv('CryptocurrenciesCorrelations.csv')
    # maindfcorr = pandas.DataFrame.from_csv('CryptocurrenciesCorrelations.csv')
    maindfcorr = maindf.corr()
    
    days = 1
    for i in range(1, days+1):
        maindf["{}_day{}".format(maincoin, i)] = (maindf[maincoin].shift(-i) - maindf[maincoin])/maindf[maincoin]

    maindf.fillna(0, inplace=True)
    
    corr = maindfcorr[othercoin][maincoin]

    plotdf = pandas.concat([maindf['{}_day1'.format(maincoin)]], axis=1)

    # Draw Graph
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    plotdf.plot(ax=a)

    canvas = FigureCanvasTkAgg(f, window)
    canvas.show()
    canvas.get_tk_widget().grid(row=1, column=5, rowspan=9)

    currentdf = plotdf[-2:-1]
    currentdf_data = currentdf.get_value(index=currentdf.index[-1], col=currentdf.columns[0])

    output = output + "Percent Change = {}".format(str(currentdf_data)) + "\n"
    output = output + "Correlation of {} with {} = {}".format(othercoin, maincoin, corr) + "\n"
    
    if currentdf_data < 0 and corr < 0:
        output = output + "BUY {}".format(othercoin) + "\n"
        confidence = corr * 100
        output = output + "Confidence = {}%".format(str(abs(confidence))) + "\n"
    elif currentdf_data > 0 and corr > 0:
        output = output + "SELL {}".format(othercoin) + "\n"
        confidence = corr * 100
        output = output + "Confidence = {}%".format(str(abs(confidence))) + "\n"
    elif currentdf_data > 0 and corr < 0:
        output = output + "BUY {}".format(othercoin) + "\n"
        confidence = corr * 100
        output = output + "Confidence = {}%".format(str(abs(confidence))) + "\n"
    elif currentdf_data < 0 and corr > 0:
        output = output + "SELL {}".format(othercoin) + "\n"
        confidence = corr * 100
        output = output + "Confidence = {}%".format(str(abs(confidence))) + "\n"

    return output
