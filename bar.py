import pandas as pd 
import matplotlib.pyplot as plt
#mport seaborn as sns

# 把數據顯示在圖表上
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

# 選擇年分
print("Choose year(2015-2020)")
year = input()
year = str(int(year) -2000)

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_' + year +'.csv')

# 選擇球員
print("Choose a player")
name = input()
df = df.loc[df['short_name'] == name]
df = df[['player_positions','pace','shooting','passing','dribbling','defending']]
#print(type(df))
#print(str(df['player_positions']))

if ("GK" in str(df['player_positions'])):
    print("He is goal keeper!")
else:
    # X軸
    df = df.drop(['player_positions'], axis=1)
    x = ['pace','shooting','passing','dribbling','defending']

    # Y軸
    y = [int(df[i]) for i in ['pace','shooting','passing','dribbling','defending']]


    plt.bar(x, y)
    addlabels(x, y)

    plt.title(name + " value")
    plt.xlabel('attribute')
    plt.ylabel('value')
    plt.show() 




