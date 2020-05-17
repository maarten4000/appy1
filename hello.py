import streamlit as sl
from PIL import Image
import pandas as pd
import altair as alt
import datetime
import numpy as np

from statsmodels.graphics.tsaplots import month_plot, quarter_plot
from statsmodels.tsa.seasonal import seasonal_decompose





@sl.cache
def Load_data(nrows, ticker):

    df = pd.read_csv(r"https://query1.finance.yahoo.com/v7/finance/download/"+ticker+"?period1=488764800&period2=1589587200&interval=1d&events=history",nrows=nrows, index_col=["Date"], parse_dates=["Date"])
    df["year"]= df.index
    df["year"]= pd.to_datetime(df["year"])
    df["jaar"] = df["year"].dt.year
    df["change"] = df["Adj Close"].pct_change()



    df = df.dropna()

    print(df.columns)
    return df



def main():

    # IN THE SIDEBAR
    ticker =sl.sidebar.text_input("Ticker:")
    input = sl.sidebar.date_input("Startdatum:", datetime.datetime.now())
    output = sl.sidebar.date_input("Einddatum:", datetime.datetime.now())
    try:
        df = Load_data(1000000, ticker=ticker)
        df = df.loc[str(input):  str(output)]
        df1 = df.copy()

    except Exception as e:
        sl.write("Please typ in a ticker")



    sl.title("Stockdata analyzer")

    sl.write("___________________________________________")






    multi = sl.multiselect("Choose your graph", ("Close", "Open", "Adj Close", "High", "Low"))
    print(multi)
    sl.write("___________________________________________")

    img = Image.open("machine-learning-840x485.png")
    sl.image(img, width=650,caption="Machine learning")









    sl.markdown("""
                    """)




    sl.markdown("""
                    """)
    sl.markdown("""
                       """)
    sl.markdown("""
                       """)




    sl.markdown("""
                           """)
    sl.markdown("""
                           """)

    sl.subheader("Graphs")
    sl.write("___________________________________________")

    sl.write("Line chart of "+ticker)
    if not sl.line_chart(df[multi]):
        sl.error("please select a ticker")

    sl.write("Bar chart of " + ticker)
    sl.bar_chart(df[multi])

    df1=df1.resample("M").mean()

    sl.write("Month chart of " + ticker)

    plot=month_plot(df1["change"])
    sl.write(plot)

    sl.subheader("Data")
    sl.write("___________________________________________")


    sl.write(df, width=1000)



if __name__ =="__main__":
    main()

