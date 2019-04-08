import numpy as np
import pandas as pd


def follow_split(df):
    # 从“发布信息”列拆分出“关注数”, “带看数”和“发布时间”
    df['关注数'] = df['发布信息'].str.split('/').str[0]
    df['关注数'] = df['关注数'].replace('[^0-9]', '', regex=True)  # 去除非数字字符
    df['关注数'] = df['关注数'].astype(int)  # 转换为数字

    df['带看数'] = df['发布信息'].str.split('/').str[1]
    df['带看数'] = df['带看数'].replace('[^0-9]', '', regex=True)  # 去除非数字字符
    df['带看数'] = df['带看数'].astype(int)  # 转换为数字

    df['发布时间'] = df['发布信息'].str.split('/').str[2]
    df['发布时间'] = df['发布时间'].str.replace('以前发布', '')  # 去除字符串

    # 删除“发布信息”列
    df.drop(columns='发布信息', inplace=True)


def name_split(df):
    # 从“房源信息”列拆分出“小区名”, “房型”, “房间面积”, “房间朝向”和“房间装修类别”
    df['小区名'] = df['房源信息'].str.split('|').str[0]

    df['房型'] = df['房源信息'].str.split('|').str[1]

    df['房间面积'] = df['房源信息'].str.split('|').str[2]
    df['房间面积'] = df['房间面积'].replace('[^0-9.]', '', regex=True)  # 去除非数字字符
    df['房间面积'] = df['房间面积'].astype(float)  # 转换为数字

    df['房间朝向'] = df['房源信息'].str.split('|').str[3]

    df['房间装修类别'] = df['房源信息'].str.split('|').str[4]

    # 删除“房源信息”列
    df.drop(columns='房源信息', inplace=True)


def position_split(df):
    # 从“房源位置”列拆分出 “层数”和“位置”
    df['房源总层数'] = df['房源位置'].str.split('-').str[0]
    df['房源总层数'] = df['房源总层数'].replace('[^0-9]', '', regex=True)  # 去除非数字字符
    df['房源总层数'] = df['房源总层数'].astype(int)  # 转换为数字

    df['小区位置'] = df['房源位置'].str.split('-').str[1]
    df['小区位置'] = df['小区位置'].map(str.strip)

    # 删除“房源位置”列
    df.drop(columns='房源位置', inplace=True)


def str_2_int(df):
    df['总价'] = df['总价'].replace('[^0-9.]', '', regex=True)  # 去除非数字字符
    df['总价'] = df['总价'].astype(float)  # 转换为数字

    df['单价'] = df['单价'].replace('[^0-9.]', '', regex=True)  # 去除非数字字符
    df['单价'] = df['单价'].astype(int)  # 转换为数字


def main():
    df = pd.read_csv('二手房数据.csv', encoding='gbk', engine='python', header=None)
    df.index = np.arange(1, len(df) + 1)
    df.columns = ['发布信息', '房源信息', '房源位置', '总价', '单价', '房源链接']

    follow_split(df)  # 拆分“发布信息”列
    name_split(df)   # 拆分“房源信息”列
    position_split(df)  # 拆分“房源位置”列
    str_2_int(df)  # 将“总价”和“单价”列转换为数字

    # print(df)
    df.to_csv('./二手房数据整理.csv', encoding='gbk')  # 保存整理后的数据


if __name__ == '__main__':
    main()

