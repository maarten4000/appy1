import streamlit as sl
from PIL import Image
import pandas as pd



@sl.cache
def Load_data(nrows, ticker):

    df = pd.read_csv(r"https://query1.finance.yahoo.com/v7/finance/download/"+ticker+"?period1=488764800&period2=1589587200&interval=1d&events=history",nrows=nrows, index_col=["Date"], parse_dates=["Date"])

    df = df.dropna()

    print(df.columns)
    return df





def main():

    # IN THE SIDEBAR
    ticker =sl.sidebar.text_input("Voeg company TICKER toe!!")

    sl.title("Stockdata analyzer")
    sl.markdown("""Predicting of stocks based on machine learning techniques, like SVR and stuff (Made by Maarten)
                """)

    sl.write()

    img = Image.open("stocks-market.jpg")
    sl.image(img,width=350)

    if sl.sidebar.button("Click to analyze"):



        df = Load_data(1000000, ticker=ticker)
        sl.write(df,width =1000)


        sl.line_chart(df[["Adj Close","Close"]])
        sl.line_chart(df["Close"])




if __name__ =="__main__":
    main()

