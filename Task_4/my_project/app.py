import argparse
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from my_func import get_data, prepare_data

def main():
    parser = argparse.ArgumentParser(description='Info about temperature')
    parser.add_argument('user_data', type=str, help='Dataframe')
    parser.add_argument('user_year', type=str, help='Year')
    parser.add_argument('user_month', type=str, help='Month')
    args = parser.parse_args()
    user_data = args.user_data
    user_year = int(args.user_year)
    user_month = int(args.user_month)

    df, _ = get_data(user_data)
    new_df = prepare_data(df)

    avg_temp = new_df[['new_latitude', 'AverageTemperature']][(new_df['Year'] == user_year) & (new_df['Month'] == user_month)] \
                .groupby(['new_latitude']).mean()
    res = pd.DataFrame({'average_temperature': avg_temp['AverageTemperature'].values.tolist(),
                        'longitude': avg_temp['AverageTemperature'].index.tolist()}) 

    st.write(f"Зависимость средней температуры от широты города за {user_month} месяц {user_year} года")
    st.line_chart(res, x="longitude", y="average_temperature")
    st.dataframe(res)

if __name__ == "__main__":
    main()