# 기존 아파트 데이터
import pandas as pd


# 1평 =  3.305785 m**2

df = pd.read_csv('지역별_규모별_제곱미터당_평균_분양가격.csv', on_bad_lines='skip', delimiter=',', encoding='utf-8', encoding_errors='ignore')

print(df)
'''
'지역명','규모구분','연도','월','분양가격(제곱미터)']
'서울'  , 전체
'인천'  ,
'부산'  , 
'''