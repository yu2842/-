# 기존 아파트 데이터
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1평 =  3.305785 m**2



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






def graph(data, region):
    selected_region = region
    region_data = dz[dz['Region'] == selected_region]
    # 그래프 그리기
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['Period'], region_data['Price'], marker='o', linestyle='-')
    plt.title('Price trends by ' +region+ ' by period')
    plt.xlabel('Period')
    plt.ylabel('Price')
    x = data['Period']
    y = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    plt.yticks(y)
    plt.xticks(x[::60])
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

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
    
    # 한번에 그리기
    mregion = ['서울','인천','경기']
    fregion = ['부산','대구','광주','대전','울산','세종']
    pregion = ['강원','충북','충남','전북','전남','경북','경남','제주']
    # 수도권
    s_data = dz[dz['Region'] == '서울']
    plt.figure(figsize=(10, 6))
    in_data = dz[dz['Region'] == '인천']
    plt.figure(figsize=(10, 6))
    gy_data = dz[dz['Region'] == '경기']
    plt.figure(figsize=(10, 6))
    for i in mregion:
        if i == '서울':
            plt.subplot(311)
            plt.plot(s_data['Period'], s_data['Price'], color='blue', linestyle='-', label='Seoul')
            plt.title('Price trends by Metropolitan area by period')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '인천':
            plt.subplot(312)
            plt.plot(in_data['Period'], in_data['Price'], color='red', linestyle='-', label='Incheon')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '경기':
            plt.subplot(313)
            plt.plot(gy_data['Period'], gy_data['Price'], color='green', linestyle='-', label='Gyeonggi')
        plt.ylabel('Price')
        x = dz['Period']
        y = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        plt.yticks(y)
        plt.xticks(x[::60])
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
    plt.show()
    # 5대광역시 및 세종특별자치시
    bu_data = dz[dz['Region'] == '부산']
    plt.figure(figsize=(10, 6))
    dae_data = dz[dz['Region'] == '대구']
    plt.figure(figsize=(10, 6))
    gw_data = dz[dz['Region'] == '광주']
    plt.figure(figsize=(10, 6))
    dj_data = dz[dz['Region'] == '대전']
    plt.figure(figsize=(10, 6))
    ul_data = dz[dz['Region'] == '울산']
    plt.figure(figsize=(10, 6))
    sg_data = dz[dz['Region'] == '세종']
    plt.figure(figsize=(10, 6))
    for i in fregion:
        if i == '부산':
            plt.subplot(231)
            plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.4)
            plt.plot(bu_data['Period'], bu_data['Price'], color='blue', linestyle='-', label='Busan')
            plt.title('Price trends by megalopolis ans Sejong by period')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '대구':
            plt.subplot(232)
            plt.plot(dae_data['Period'], dae_data['Price'], color='red', linestyle='-', label='Daegu')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '광주':
            plt.subplot(233)
            plt.plot(gw_data['Period'], gw_data['Price'], color='green', linestyle='-', label='Gwangju')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '대전':
            plt.subplot(234)
            plt.plot(dj_data['Period'], dj_data['Price'], color='orange', linestyle='-', label='Daejeon')
        elif i == '울산':
            plt.subplot(235)
            plt.plot(ul_data['Period'], ul_data['Price'], color='purple', linestyle='-', label='Ulsan')
        elif i == '세종':
            plt.subplot(236)
            plt.plot(sg_data['Period'], sg_data['Price'], color='cyan', linestyle='-', label='Sejong')    
        plt.ylabel('Price')
        x = dz['Period']
        y = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        plt.yticks(y)
        plt.xticks(x[::200])
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
    plt.show()
    # 지방
    gan_data = dz[dz['Region'] == '강원']
    plt.figure(figsize=(10, 4))
    cb_data = dz[dz['Region'] == '충북']
    plt.figure(figsize=(10, 4))
    cn_data = dz[dz['Region'] == '충남']
    plt.figure(figsize=(10, 4))
    jb_data = dz[dz['Region'] == '전북']
    plt.figure(figsize=(10, 4))
    jn_data = dz[dz['Region'] == '전남']
    plt.figure(figsize=(10, 4))
    gb_data = dz[dz['Region'] == '경북']
    plt.figure(figsize=(10, 4))
    gn_data = dz[dz['Region'] == '경남']
    plt.figure(figsize=(10, 4))
    jj_data = dz[dz['Region'] == '제주']
    plt.figure(figsize=(10, 4))
    for i in pregion:
        if i == '강원':
            plt.subplot(241)
            plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.54)
            plt.plot(gan_data['Period'], gan_data['Price'], color='blue', linestyle='-', label='Gangwon')
            plt.title('Price trends by the provinces by period')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '충북':
            plt.subplot(242)
            plt.plot(cb_data['Period'], cb_data['Price'], color='red', linestyle='-', label='Chungbuk')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '충남':
            plt.subplot(243)
            plt.plot(cn_data['Period'], cn_data['Price'], color='green', linestyle='-', label='Chungnam')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '전북':
            plt.subplot(244)
            plt.plot(jb_data['Period'], jb_data['Price'], color='orange', linestyle='-', label='Jeonbuk')
            ax = plt.gca()
            ax.axes.xaxis.set_ticklabels([])
        elif i == '전남':
            plt.subplot(245)
            plt.plot(jn_data['Period'], jn_data['Price'], color='purple', linestyle='-', label='Jeonnam')
        elif i == '경북':
            plt.subplot(246)
            plt.plot(gb_data['Period'], gb_data['Price'], color='cyan', linestyle='-', label='Gyeongbuk') 
        elif i == '경남':
            plt.subplot(247)
            plt.plot(gn_data['Period'], gn_data['Price'], color='pink', linestyle='-', label='Gyeongnam')  
        elif i == '제주':
            plt.subplot(248)
            plt.plot(jj_data['Period'], jj_data['Price'], color='gray', linestyle='-', label='Jeju')  
        plt.ylabel('Price')
        x = dz['Period']
        y = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        plt.yticks(y)
        plt.xticks(x[::200])
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
    plt.show()
    