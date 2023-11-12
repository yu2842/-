import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load_data(filename):
    class NaData:
        data = []
        feature_name = ['지역명', '규모구분', '연도', '월', '분양가격(제곱미터)']

    naData = NaData()
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            items = line.rstrip('\n').split(',')
            if items[1] == '모든면적':
                naData.data.append(items[0:])
        naData.data = np.array(naData.data)
    return naData

if __name__ == "__main__":
    nadata = load_data('신규 민간아파트 분양가격.csv')
    df = pd.DataFrame(nadata.data)
    df.columns = ["Region", "Scale", "Year", "Month", "Price"]

    # 누락된 값을 가진 행 제거
    df = df.dropna()

    # 숫자형 데이터로 변환
    df["Year"] = pd.to_numeric(df["Year"])
    df["Month"] = pd.to_numeric(df["Month"])
    df["Price"] = pd.to_numeric(df["Price"])

    regions = df["Region"].unique()
    
    print("예측 가격을 알고 싶은 지역, 연도, 월을 입력해주십시오.")
    region, year, month = input().split() # 서울,2023,4

    for rg in regions:
        if rg==region :
            features = df.loc[df["Region"] == region,["Year", "Month"]]
            target = df.loc[df["Region"] == region,"Price"]

            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

            # K-최근접 이웃 회귀 모델 초기화 (K=5, 예시로 설정)
            model = KNeighborsRegressor(n_neighbors=5)

            # 모델 학습
            model.fit(X_train, y_train)

            # 테스트 데이터에 대한 예측
            predictions = model.predict(X_test)

            # 모델 평가 (R-squared 계산)
            r2 = r2_score(y_test, predictions)

            # 새로운 데이터에 대한 예측
            new_data = pd.DataFrame({'Year':[year], 'Month':[month]})
            new_prediction = model.predict(new_data)
            print(" {}년 {}월 {}지역 예측 분양가격  : {} (정확도 {}%) ".format(year,month,region,round(new_prediction[0]),round(r2*100)))
    