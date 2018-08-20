# Importing Modules
import requests
import json
import pandas
from matplotlib import style
from collections import Counter
import numpy

from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

# Graph embed stuff
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

style.use('ggplot')

# Global Variables
main_df = None
output = ''


#
# Function Declarations
# #####################

# Get data from the data source, and convert the data to dataframe
def get_dataframe_of(symbol):
    url = "https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit=2000".format(symbol)
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


# Create Data labels for machine learning stuff
def create_labels_for(symbol):
    global main_df
    days = 1
    df = main_df
    symbols = df.columns
    df.fillna(0, inplace=True)

    for i in range(1, (days + 1)):
        df["{}_{}".format(symbol, i)] = (df[symbol].shift(-i) - df[symbol]) / df[symbol]

    df.fillna(0, inplace=True)
    return symbols, df


def create_targets_for(*symbolArguments):
    # Buy, Sell or Hold values
    buy = 1
    sell = -1
    hold = 0

    symbols = [symbol for symbol in symbolArguments]
    percent_threshold = 0.02
    for symbol in symbols:
        if symbol > percent_threshold:
            return buy
        if symbol < -0.012:
            return sell
        return hold


def get_features_for(symbol):
    global output
    symbols, df = create_labels_for(symbol)
    df['{}_target'.format(symbol)] = list(
        map(
            create_targets_for,
            df['{}_1'.format(symbol)]
        )
    )

    df_values = df['{}_target'.format(symbol)].values
    labels = df_values

    string_values = [str(index) for index in df_values]
    output = output + str("Data Distribution = {}".format(Counter(string_values))) + "\n"
    df.fillna(0, inplace=True)

    df_values = df[[symbol for symbol in symbols]].pct_change()
    df_values = df_values.replace([numpy.inf, -numpy.inf], 0)
    df_values.fillna(0, inplace=True)

    features = df_values.values
    # labels = df['{}_target'.format(symbol)].values
    return features, labels, df


def predict_stock(symbol):
    global output
    features, labels, df = get_features_for(symbol)

    train_features, testing_features, train_labels, testing_labels = cross_validation.train_test_split(
        features, labels, test_size=0.50
    )

    # Creating Classifier
    classifier = neighbors.KNeighborsClassifier()

    classifier.fit(train_features, train_labels)

    confidence = classifier.score(testing_features, testing_labels)
    output = output + str("Percent Confidence of Stock Prediction = {}".format((confidence * 100))) + "\n"
    # data = testing_features[0]
    data = features[len(features)-1]

    # predictions = classifier.predict(testing_features)
    predictions = classifier.predict(data.reshape(1,-1))
    output = output + str("Predicted Distribution = {}".format(Counter(predictions))) + "\n"
    output = output + str("Predicted Distribution = ") + "\n"
    output = output + str(predictions) + "\n"
    return predictions


def make_graph(symbol, window):
    global main_df

    if symbol == "XEM":
        symbol = "NEM"

    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    main_df.plot(ax=a)

    canvas = FigureCanvasTkAgg(f, window)
    canvas.show()
    canvas.get_tk_widget().grid(row=1, column=4, rowspan=9)

    # toolbar = NavigationToolbar2TkAgg(canvas, window)
    # toolbar.update()
    # canvas._tkcanvas.grid(row=10, column=4)


#
# The main module
# ###############
def analyze(symbol, window):
    global main_df

    # main_df = pandas.DataFrame.from_csv('CryptocurrenciesDataFrame.csv')
    main_df = pandas.read_csv('CryptocurrenciesDataFrame.csv', index_col=0)
    main_df.fillna(0, inplace=True)

    make_graph(symbol, window)

    predict = predict_stock(symbol)
    global output
    return output, predict
