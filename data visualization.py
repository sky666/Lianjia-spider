import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号
import seaborn as sns


# 1. 读取数据
df = pd.read_csv('二手房数据分析.csv', encoding='gbk', engine='python')

# 2. 数据清洗
# 查看数据集信息
# print(df.describe().to_string())  # 获取数据类型列的描述统计信息
# print(df.info())  # 查看每一列的数据类型，和数据总数
'''
从数据集信息可以发现没有缺失值
'''

# 3. 数据可视化
# (1):查看各区域的二手房数量
def house_count():
    df_house_count = df.groupby('区域')['小区名'].count().sort_values(ascending=False).to_frame().reset_index()
    print(df_house_count)
    sns.barplot(x='区域', y='小区名', data=df_house_count)
    plt.xlabel('区域')
    plt.ylabel('数量')
    plt.title('无锡市各区域二手房数量')
    plt.savefig('无锡市各区域二手房数量.jpg')
    plt.show()


# (2):查看各区域的二手房房屋总价
def house_total_price():
    sns.boxplot(x='区域', y='总价', data=df)
    plt.xlabel('区域')
    plt.ylabel('房屋总价')
    plt.title('无锡市各区域二手房房屋总价')
    plt.savefig('无锡市各区域二手房房屋总价.jpg')
    plt.show()


# (3):查看各区域的二手房平均每平米单价
def house_average_unitprice():
    df_house_unitprice = df.groupby('区域')['单价'].mean().sort_values(ascending=False).to_frame().reset_index()
    print(df_house_unitprice)
    sns.barplot(x='区域', y='单价', data=df_house_unitprice)
    plt.xlabel('区域')
    plt.ylabel('平均每平米单价')
    plt.title('无锡市各区域二手房平均每平米单价')
    plt.savefig('无锡市各区域二手房平均每平米单价.jpg')
    plt.show()


# (4):查看无锡市的二手房房型数量分布
def house_style():
    sns.countplot(y='房型', data=df)
    plt.xlabel('数量')
    plt.ylabel('房型')
    plt.title('无锡市二手房房型数量')
    plt.savefig('无锡市二手房房型数量.jpg')
    plt.show()


# (5):查看无锡市的二手房装修类型分布
def house_decoration():
    sns.countplot(x='房间装修类别', data=df)
    plt.xlabel('房间装修类别')
    plt.ylabel('数量')
    plt.title('无锡市二手房装修类型分布数量')
    plt.savefig('无锡市二手房装修类型分布数量.jpg')
    plt.show()


# (6):查看无锡市的二手房房间朝向分布
def house_direction():
    sns.countplot(y='房间朝向', data=df)
    plt.xlabel('数量')
    plt.ylabel('房间朝向类别')
    plt.title('无锡市二手房房间朝向类型分布数量')
    plt.savefig('无锡市二手房房间朝向类型分布数量.jpg')
    plt.show()


# (7):查看无锡市的房间面积和单价的关系
def house_area_price_relation():
    df[['房间面积']].astype(int)  # 将房间面积转换为整数
    plt.scatter(x='房间面积', y='单价', data=df, marker='o')
    plt.xlabel('房间面积')
    plt.ylabel('单价')
    plt.title('无锡市二手房房间面积和单价的关系')
    plt.savefig('无锡市二手房房间面积和单价的关系.jpg')
    plt.show()


# (8):查看无锡市的不同房型的关注数和带看数
def house_style_attention():
    ax = sns.boxplot(x='房型', y='关注数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('房型')
    plt.ylabel('关注数')
    plt.title('无锡市二手房不同房型的关注数')
    plt.savefig('无锡市二手房不同房型的关注数.jpg')
    plt.show()

    ax = sns.boxplot(x='房型', y='带看数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('房型')
    plt.ylabel('带看数')
    plt.title('无锡市二手房不同房型的带看数')
    plt.savefig('无锡市二手房不同房型的带看数.jpg')
    plt.show()


# (9):查看无锡市的不同装修类型的关注数和带看数
def house_decoration_attention():
    ax = sns.boxplot(x='房间装修类别', y='关注数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('房间装修类别')
    plt.ylabel('关注数')
    plt.title('无锡市二手房不同房间装修类型的关注数')
    plt.savefig('无锡市二手房不同房间装修类型的关注数.jpg')
    plt.show()

    ax = sns.boxplot(x='房间装修类别', y='带看数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('房间装修类别')
    plt.ylabel('带看数')
    plt.title('无锡市二手房不同房间装修类别的带看数')
    plt.savefig('无锡市二手房不同房间装修类别的带看数.jpg')
    plt.show()


# (10):查看无锡市的不同区域的关注数和带看数
def house_area_attention():
    ax = sns.boxplot(x='区域', y='关注数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('区域')
    plt.ylabel('关注数')
    plt.title('无锡市二手房不同区域的关注数')
    plt.savefig('无锡市二手房不同区域的关注数.jpg')
    plt.show()

    ax = sns.boxplot(x='区域', y='带看数', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right", fontsize=7)
    plt.xlabel('区域')
    plt.ylabel('带看数')
    plt.title('无锡市二手房不同区域的带看数')
    plt.savefig('无锡市二手房不同区域的带看数.jpg')
    plt.show()


