import pandas as pd 
import matplotlib.pyplot as plt

print("Choose a player")
name = input()

print("Choose attribute(pace/shooting/passin/dribbling/defending)")
attribute = input()

x = []
y = []

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_15.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])


df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_16.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_17.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_18.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_19.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])

df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
df = df.loc[df['short_name'] == name]
df = df[['age','pace','shooting','passing','dribbling','defending']]
x.append(df['age'])
y.append(df[attribute])

#print(type(x))
plt.plot(x, y)
plt.title(name + "'s " + attribute + " value")
plt.xlabel('age')
plt.ylabel('value')
plt.show()