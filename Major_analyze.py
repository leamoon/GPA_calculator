"""
Author : wumaomao
Time : 2020.03.23
Address : Wuchuan
Environment : windows10 python3.7 Anaconda3
Function : exposing major-data visible
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    try:
        data_frame = pd.read_excel('2017级专业分流录取名次对照表-简版.xlsx')
        rank = data_frame['名次 '].tolist()
        grade = data_frame['总平均加权成绩 '].tolist()
        major = data_frame['录取专业'].tolist()
    except Exception:
        print('data file is not right')
        sys.exit(-1)

    # Dividing four parts
    Optic = []
    Optic_grade = []
    Integrate = []
    Integrate_grade = []
    Micro = []
    Micro_grade = []
    Elc = []
    Elc_grade = []


    for i in range(0, len(rank)):
        if major[i] == '光电':
            Optic.append(rank[i])
            Optic_grade.append(grade[i])

        elif major[i] == '集成':
            Integrate.append(rank[i])
            Integrate_grade.append(grade[i])

        elif major[i] == '微电子':
            Micro.append(rank[i])
            Micro_grade.append(grade[i])

        elif major[i] == '电子':
            Elc.append(rank[i])
            Elc_grade.append(grade[i])

        else:
            print('error:')
            print(rank[i])

    print('Grade of Optic : %f' % (sum(Optic_grade)/len(Optic_grade)))
    print('Grade of Integrate : %f' % (sum(Integrate_grade)/len(Integrate_grade)))
    print('Grade of Micro : %f' % (sum(Micro_grade)/len(Micro_grade)))
    print('Grade of Elc : %f' % (sum(Elc_grade)/len(Elc_grade)))
    print(Micro)
    # data -> visible
    fig = plt.figure()

    list1 = [0] * len(Optic)
    list2 = [5] * len(Integrate)
    list3 = [10] * len(Micro)
    list4 = [15] * len(Elc)

    ax = Axes3D(fig)
    plt.xlabel('Rank')
    plt.ylabel('Grade')

    ax.scatter3D(Optic, Optic_grade, list1, label='Optic')
    ax.scatter3D(Integrate, Integrate_grade, list2, label='Integrate')
    ax.scatter3D(Micro, Micro_grade, list3, label='Micro')
    ax.scatter3D(Elc, Elc_grade, list4, label='Elc')

    plt.legend()
    plt.show()
