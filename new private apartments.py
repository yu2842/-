# 신규 아파트 데이터

import numpy as np
import pandas as pd




'''  (보류)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


** 신규 민간아파트 가격 예측 머신러닝** 

# 특성(X)와 타겟(y) 분리


# 학습용 데이터와 테스트용 데이터 분리


# 회귀 모델 학습


# 테스트 데이터로 예측

# 예측 성능 평가
print("R^2:", )

'''



# [ '지역명','규모','연도','월','분양가격(제곱미터)' ]
# [   서울  ,'모든면적', '2016 ,3월 ,      6173         ]


# 파일 불러서 data에 저장하는 함수
def load_wdbc_data(filename): #규모는 '모든 면적' 만  저장한다.  지역별 규모별 제곱미터당 평균 분양가격 csv에는 전체 데이터만 존재하기 때문에

    with open(filename) as f:
            for line in f.readlines():
                items = line.split(',')


            









# 메인 함수 동작 
if __name__ == '__main__':
     



    #데이터 로드 ( csv 파일 불러오기)

    #데이터 분류


    # 데이터 시각화 ( 시기별로 변하는가격 그래프 -> matplotlib 등 파이썬 라이브러리 활용 )