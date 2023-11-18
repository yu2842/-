import pandas as pd
import numpy as np

def load_data(filename):
    class NaData:
        data = []
        target = []
        target_name = []
        feature_name = ['']

    naData = NaData()

    with open(filename, encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            items = line.rstrip('\n').split(',')
            if items[1] == '모든면적' and items[0]== '서울': 
                naData.data.append(items[0:])
        naData.data = np.array(naData.data)

    return naData
data = load_data('gdp(2015~2022).csv')
print(data.data)
