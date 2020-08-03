import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
from sklearn import svm, neighbors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

style.use("ggplot")

def save_sp500_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text)
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers=[]
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        if "." in ticker:
            ticker = ticker.replace('.', '-')
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)
    return tickers

# save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers=save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers=pickle.load(f)
    if not os.path.exists("stock_dfs"):
        os.makedirs("stock_dfs")

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2020,5,30)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists("stock_dfs/{}.csv".format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv("stock_dfs/{}.csv".format(ticker))
        else:
            print("Already have {}".format(ticker))

# get_data_from_yahoo()

def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()
    for count,ticker in enumerate(tickers):
        df = pd.read_csv("stock_dfs/{}.csv".format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={"Adj Close": ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], axis=1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how = 'outer')

        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv("sp500_joined_closes.csv")

# compile_data()

def companies_correlation():
    df = pd.read_csv("sp500_joined_closes.csv")
    # df['AAPL'].plot()
    # plt.show()
    df_corr = df.corr()
    print(df_corr.head())
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()

# companies_correlation()

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv("sp500_joined_closes.csv", index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i)/df[ticker]-1)
    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        elif col < -requirement:
            return -1
    return 0

def extract_feature_sets(ticker):
    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)],
                                                ))
    vals = df["{}_target".format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print("Data spread: ", Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], np.nan)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df["{}_target".format(ticker)].values

    return X, y, df

# extract_feature_sets("XOM")

def do_ml(ticker):
    X,y,df = extract_feature_sets(ticker)
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

    # clf = neighbors.KNeighborsClassifier()
    clf=VotingClassifier([('lsvc', svm.LinearSVC()),
                          ('knn', neighbors.KNeighborsClassifier()),
                          ('rfor', RandomForestClassifier(max_depth=20))])
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test,y_test)
    print("Accuracy: ", confidence)
    predictions = clf.predict(X_test)
    print("Predicted spread: ", Counter(predictions))

    return confidence


do_ml("BAC")