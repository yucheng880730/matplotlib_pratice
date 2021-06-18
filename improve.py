import pandas as pd 

df1 = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
df2 = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_15.csv')

print("Choose a player")
name = input()

df1 = df1.loc[df1['short_name'] == name]
df2 = df2.loc[df2['short_name'] == name]

pace20 = int(df1['pace'])
shooting20 = int(df1['shooting'])
passing20 = int(df1['passing'])
dribbling20 = int(df1['dribbling'])
defending20 = int(df1['defending'])

pace15 = int(df2['pace'])
shooting15 = int(df2['shooting'])
passing15 = int(df2['passing'])
dribbling15 = int(df2['dribbling'])
defending15 = int(df2['defending'])

pace = (pace20 - pace15) / pace15
shooting = (shooting20 - shooting15) / shooting15
passing = (passing20 - passing15) / passing15
dribbling = (dribbling20 - dribbling15) / dribbling15
defending = (defending20 - defending15) / defending15

print('from 2015 to 2020 pace improve rate: {:.2%}'.format(pace))
print('from 2015 to 2020 shooting improve rate: {:.2%}'.format(shooting))
print('from 2015 to 2020 passing improve rate: {:.2%}'.format(passing))
print('from 2015 to 2020 dribbling improve rate: {:.2%}'.format(dribbling))
print('from 2015 to 2020 defending improve rate: {:.2%}'.format(defending))