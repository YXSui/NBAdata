# -*- coding: utf-8 -*-
p = [[] for i in range(18)]
def str2float2d(k):
    for i in range(len(k)):
        for j in range(len(k[i])):
            k[i][j]=float(k[i][j])
    return k
# an example
def plotregular():
    plt.plot(d[2],d[11],'b*')
    plt.plot(d[2][8],d[11][8],'r*')
    plt.plot(d[2][7],d[11][7],'r*')
    plt.plot(d[2][12],d[11][12],'r*')
    plt.plot(35.4,0.450,'g*')
    plt.plot(32.0,0.503,'g*')
    plt.plot(35.0,0.535,'g*')
    plt.plot(30.1,0.504,'g*')
    plt.text(35.4,0.450,'06Bryant',fontsize=7)
    plt.text(32.0,0.503,'14Durant',fontsize=7)
    plt.text(35.0,0.535,'88Jordan',fontsize=7)
    plt.text(30.1,0.504,'16Curry',fontsize=7)
    plt.text(d[2][12],d[11][12],'Durant',fontsize=7)
    plt.text(d[2][7],d[11][7],'James',fontsize=7)
    plt.text(d[2][8],d[11][8],'Leonard',fontsize=7)
    plt.xlabel('PTS')
    plt.ylabel('FG_PCT')
    plt.title('16-17 Regular Season of NBA')
    plt.show()
#team,player,pts,ast,reb,dreb,oreb,stl,blk,tov,fga,fgpc,fg3a,fg3pc,fta,ftpc,eff,mi
if __name__ == '__main__':   
    import csv
    import copy
    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas import DataFrame
    import numpy as np
    with open('2016-2017Regular.csv','rb') as f:
        readers = csv.reader(f)
        rows = [row for row in readers]       
        for line in rows:
            p[0].append(line[rows[0].index('TEAM')])
            p[1].append(line[rows[0].index('PLAYER')])
            p[2].append(line[rows[0].index('PTS')])
            p[3].append(line[rows[0].index('AST')])
            p[4].append(line[rows[0].index('REB')])
            p[5].append(line[rows[0].index('DREB')])
            p[6].append(line[rows[0].index('OREB')])
            p[7].append(line[rows[0].index('STL')])
            p[8].append(line[rows[0].index('BLK')])
            p[9].append(line[rows[0].index('TOV')])
            p[10].append(line[rows[0].index('FGA')])
            p[11].append(line[rows[0].index('FG_PCT')])
            p[12].append(line[rows[0].index('FG3A')])
            p[13].append(line[rows[0].index('FG3_PCT')])
            p[14].append(line[rows[0].index('FTA')])
            p[15].append(line[rows[0].index('FT_PCT')])
            p[16].append(line[rows[0].index('EFF')])
            p[17].append(line[rows[0].index('MIN')])
        f.close()
    d = copy.deepcopy(p)
    for i in d:
        i.pop(0)
    str2float2d(d[2:])
    plotregular()
    frame = DataFrame(np.array(d).T,index=pd.Index(d[1]),columns=[i[0] for i in p])
    frame1 = frame.drop('PLAYER',axis=1)

