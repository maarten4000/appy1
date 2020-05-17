import streamlit as sl
from PIL import Image
import pandas as pd
import altair as alt
import datetime
import numpy as np



@sl.cache
def Load_data(nrows, ticker):

    df = pd.read_csv(r"https://query1.finance.yahoo.com/v7/finance/download/"+ticker+"?period1=488764800&period2=1589587200&interval=1d&events=history",nrows=nrows, index_col=["Date"], parse_dates=["Date"])
    df["year"]= df.index


    df = df.dropna()

    print(df.columns)
    return df



def main():

    # IN THE SIDEBAR
    ticker =sl.sidebar.text_input("Ticker:")


    sl.title("  "+"Stockdata analyzer")

    sl.write("___________________________________________")




    sl.markdown("""
                    """)

    sl.markdown("""
                    """)
    img = Image.open("machine-learning-840x485.png")
    sl.image(img, width=650)




    sl.markdown("""
                    """)




    sl.markdown("""
                    """)
    sl.markdown("""
                       """)
    sl.markdown("""
                       """)

    sl.write("Stap 1: Voeg een ticker toe")
    sl.write("Stap 2: Zet de datum correct")

    sl.write("___________________________________________")

    sl.markdown("""
                           """)
    sl.markdown("""
                           """)

    input = sl.sidebar.date_input("Startdatum:", datetime.datetime.now())
    output = sl.sidebar.date_input("Einddatum:", datetime.datetime.now())

    if sl.sidebar.button("Oke!"):
        df = Load_data(1000000, ticker=ticker)
        df = df.loc[str(input):  str(output)]



        sl.line_chart(df[["Adj Close","Close"]])

        sl.write("___________________________________________")
        sl.write(df, width=1000)


if __name__ =="__main__":
    main()

