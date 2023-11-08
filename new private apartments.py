# 신규 아파트 데이터

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# [ '지역명','연도','월','분양가격(제곱미터)' ]
# [   서울   ,2016 ,3월 ,      6173         ] 
import pandas as pd

data = pd.read_csv('신규 민간아파트 분양가격.csv', on_bad_lines='skip', delimiter=',', encoding='utf-8', encoding_errors='ignore')

# 특성(X)와 타겟(y) 분리
X = data[["Region","Year", "Month", "Price_per_square meter", "Price" ]]
y = data["price"]



# 학습용 데이터와 테스트용 데이터 분리


# 회귀 모델 학습


# 테스트 데이터로 예측

# 예측 성능 평가
print("R^2:", )




# 메인 함수 동작 : 머신러닝 이용
if __name__ == '__main__':
    #데이터 로드



    #데이터 분류
    



    # 데이터 시각화