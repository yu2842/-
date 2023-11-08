# 신규 아파트 데이터
import pandas as pd

df = pd.read_csv('신규 민간아파트 분양가격.csv', on_bad_lines='skip', delimiter=',', encoding='utf-8', encoding_errors='ignore')
print(df)
