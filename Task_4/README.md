## Task_4
Проект позволяет определять среднюю температуру по широте за определенный год и месяц и выводить результаты с помощью streamlit.

Для запуска программы введите команду:
```sh 
% python3 -m streamlit run my_project/app.py user_data user_year user_month
```
* user_data - csv файл с данными;
* user_year - год, начиная с 1950; 
* user_month – номер месяца.

Например:
```sh 
% python3 -m streamlit run my_project/app.py GlobalLandTemperaturesByMajorCity.csv 1970 3
``` 