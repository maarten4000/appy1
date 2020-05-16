import streamlit as sl
from PIL import Image
import pandas as pd





@sl.cache
def Load_data(nrows):
    df = pd.read_csv(r"C:\Users\maart\OneDrive\Bureaublad\Data\airline_passengers.csv",nrows=nrows,index_col=["Month"],parse_dates=["Month"])
    print(df.columns)
    return df


def main():

    # IN THE SIDEBAR
    sl.sidebar.slider("Select the year",0,23,12)
    sl.sidebar.button("Homee!!")
    sl.title("Airline passengers")
    sl.markdown("""Predicting of the airline passengers with Time series forecasting 
                models we used are ARIMA and HOLT WINTER""")


    img = Image.open("download.jpg")
    sl.image(img,width=500)


    df = Load_data(1000)
    sl.write(df)



    sl.line_chart(df["Thousands of Passengers"])

    sl.bar_chart(df["Thousands of Passengers"])

if __name__ =="__main__":
    main()

