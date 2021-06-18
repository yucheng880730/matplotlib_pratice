import pandas as pd 
import matplotlib.pyplot as plt


def pace():
    df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
    df = df[['age','pace']]
    
    df = (df.nlargest(100, 'pace'))
    # print(df)

    x = df['age']
    y = df['pace']
    
    fig  = plt.figure()

    plt.axis([15, 45, 75, 100])
    plt.xlabel('age')
    plt.ylabel('value')
    plt.scatter(x, y)
    plt.title("pace_scatter")
    plt.minorticks_on()
    plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
    fig.set_figheight(20)
    fig.set_figwidth(20)
    plt.show()


def shooting():
    df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
    df = df[['age','shooting']]

    df = (df.nlargest(100, 'shooting'))
    # print(df)
    
    x = df['age']
    y = df['shooting']

    fig  = plt.figure()

    plt.axis([15, 45, 75, 100])
    plt.xlabel('age')
    plt.ylabel('value')
    plt.scatter(x, y)
    plt.title("shooting_scatter")
    plt.minorticks_on()
    plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
    fig.set_figheight(20)
    fig.set_figwidth(20)
    plt.show()

def passing():
    df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
    df = df[['age','passing']]

    df = (df.nlargest(100, 'passing'))
    # print(df)

    x = df['age']
    y = df['passing']

    fig  = plt.figure()

    plt.axis([15, 45, 75, 100])
    plt.xlabel('age')
    plt.ylabel('value')
    plt.scatter(x, y)
    plt.title("passing_scatter")
    plt.minorticks_on()
    plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
    fig.set_figheight(20)
    fig.set_figwidth(20)
    plt.show()

def dribbling():
    df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
    df = df[['age','dribbling']]

    df = (df.nlargest(100, 'dribbling'))
    # print(df)

    x = df['age']
    y = df['dribbling']

    fig  = plt.figure()

    plt.axis([15, 45, 75, 100])
    plt.xlabel('age')
    plt.ylabel('value')
    plt.scatter(x, y)
    plt.title("dribbling_scatter")
    plt.minorticks_on()
    plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
    fig.set_figheight(20)
    fig.set_figwidth(20)
    plt.show()

def defending():
    df = pd.read_csv('C:/Users/yucheng/Desktop/NTU_python/players_20.csv')
    df = df[['age','defending']]

    df = (df.nlargest(100, 'defending'))
    # print(df)

    x = df['age']
    y = df['defending']

    fig  = plt.figure()

    plt.axis([15, 45, 75, 100])
    plt.xlabel('age')
    plt.ylabel('value')
    plt.scatter(x, y)
    plt.title("defending_scatter")
    plt.minorticks_on()
    plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
    fig.set_figheight(20)
    fig.set_figwidth(20)
    plt.show()


pace()
shooting()
passing()
dribbling()
defending()