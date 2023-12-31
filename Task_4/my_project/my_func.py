import re
import zipfile
import pandas as pd

def get_data(user_data):
    with zipfile.ZipFile("my_project/archive.zip") as z:
        all_files = set(z.namelist())
        with z.open(f"{user_data}") as f:
            df = pd.read_csv(f, parse_dates=["dt"])
    return df, all_files

def prepare_data(df):
    new_df = df[df['dt'] >= '1950-01-01']
    new_df['Year'] = df['dt'].dt.year

    new_df['Month'] = df['dt'].dt.month
    new_latitude = [float(re.sub(r"\d{1,}\.\d{1,}S", "-" + item[:-1], item).replace("N", "")) for item in new_df['Latitude']]
    new_longitude = [float(re.sub(r"\d{1,}\.\d{1,}W", "-" + item[:-1], item).replace("E", "")) for item in new_df['Longitude']]
    new_df['new_latitude'] = new_latitude
    new_df['new_longitude'] = new_longitude
    return new_df