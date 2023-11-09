# 기존 아파트 데이터
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1평 =  3.305785 m**2
'''
df = pd.read_csv('지역별_규모별_제곱미터당_평균_분양가격.csv', on_bad_lines='skip', delimiter=',', encoding='utf-8', encoding_errors='ignore')

print(df)
'''
'''

'지역명','규모구분','연도','월','분양가격(제곱미터)']
'서울'  , 전체
'인천'  ,
'부산'  , 
'''


def load_data(filename):
    class NaData:
        data = []
        target = []
        target_name = []
        feature_name = ['지역명', '규모구분', '연도', '월', '분양가격(제곱미터)']

    naData = NaData()

    with open(filename, encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            items = line.rstrip('\n').split(',')
            if items[1] == '모든면적':
                naData.data.append(items[0:])
        naData.data = np.array(naData.data)

    return naData


if __name__ == "__main__":
    nadata = load_data('신규 민간아파트 분양가격.csv')
    print(nadata.data)
    df = pd.DataFrame(nadata.data)
    df.columns = ["Region", "Scale", "Year", "Month", "Price"]
    ds = df.drop('Scale', axis=1)
    cols = ['Year', 'Month']
    ds['Period'] = ds[cols].apply(lambda row: '.'.join(row.values.astype(str)), axis=1)
    dz = ds.drop(['Year', 'Month'], axis=1)
    dz['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    dz['Price'] = dz['Price'].astype(float)
    selected_region = '서울'
    region_data = dz[dz['Region'] == selected_region]

    # 그래프 그리기
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['Period'], region_data['Price'], marker='o', linestyle='-')
    plt.title('Price trends by Seoul by period')
    plt.xlabel('Period')
    plt.ylabel('Price')
    y = [3000, 4000, 5000, 6000, 7000, 8000, 9000]
    plt.yticks(y)
    plt.grid(True)
    plt.show()