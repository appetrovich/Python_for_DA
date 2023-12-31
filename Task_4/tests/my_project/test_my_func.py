import zipfile
import pandas as pd

from my_project.my_func import get_data, prepare_data

def test_get_data():
    user_data = 'GlobalLandTemperaturesByMajorCity.csv'
    _, all_files = get_data(user_data)
    assert user_data in all_files

def test_prepare_data():
    df = pd.DataFrame({})
    user_data = 'GlobalLandTemperaturesByMajorCity.csv'
    with zipfile.ZipFile("my_project/archive.zip") as z:
        with z.open(f"{user_data}") as f:
            df = pd.read_csv(f, parse_dates=["dt"])

    assert type(prepare_data(df)) is pd.core.frame.DataFrame