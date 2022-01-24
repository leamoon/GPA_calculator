"""
Author : wumaomao
Time : 2020.03.11
Address : wuchuan
Environment : windows10 anaconda3 python3.7
Function : calculate your score comprehensively
"""
import pandas as pd
import tkinter as tk
from tkinter import filedialog


def grade_analyze(grade=None, weight=None, semester=None, genre=None):
    # filter the info from grade&weight, return a dictionary
    if grade is None:
        return "Parameter of grade not found"
    if weight is None:
        return "Lost weight parameter"
    if genre is None:
        genre = ['C']*len(grade)
    if semester is None:
        semester = [1]*len(grade)

    grade_dic = {}
    genre_dic = {}
    semester_number = set(semester)

    if '' in semester_number:
        semester_number.remove('')

    for i in semester_number:
        grade_dic['grade_{}'.format(i)], grade_dic['weight_{}'.format(i)], genre_dic['genre_{}'.format(i)] = [], [], []
        for j in range(len(grade)):
            if i == semester[j]:
                grade_dic['grade_{}'.format(i)].append(grade[j])
                grade_dic['weight_{}'.format(i)].append(weight[j])
                genre_dic['genre_{}'.format(i)].append(genre[j])

    return grade_dic, genre_dic


def grade_calculate(grade_dictionary, genre_dictionary):

    gpa_100_dic = {}
    gpa_4_dic = {}
    gpa_weight = {}
    grade_series = pd.Series(grade_dictionary)
    gpa_100_dic['GPA'] = 0
    gpa_4_dic['GPA'] = 0
    gpa_weight['weight'] = 0
    gpa_weight['whole_weight'] = 0

    # 100
    for i in range(int(len(grade_series)/2)):
        i += 1
        gpa_100_dic['GPA_{}'.format(i)] = []
        temp_result = 0
        con_weight = 0

        for j in range(len(grade_series['grade_{}'.format(i)])):
            if genre_dictionary['genre_{}'.format(i)][j] == 0:
                con_weight += grade_series['weight_{}'.format(i)][j]
            else:
                temp_result += grade_series['grade_{}'.format(i)][j] * grade_series['weight_{}'.format(i)][j]

        if sum(grade_series['weight_{}'.format(i)]) != 0:
            gpa_100_dic['GPA_{}'.format(i)] = format(
                temp_result / (sum(grade_series['weight_{}'.format(i)]) - con_weight), '.2f')
        else:
            gpa_100_dic['GPA_{}'.format(i)] = 0

        gpa_weight['whole_weight_{}'.format(i)] = sum(grade_series['weight_{}'.format(i)])
        gpa_weight['weight_{}'.format(i)] = gpa_weight['whole_weight_{}'.format(i)] - con_weight
        gpa_100_dic['GPA'] += float(gpa_100_dic['GPA_{}'.format(i)])*gpa_weight['weight_{}'.format(i)]
        gpa_weight['weight'] += float(gpa_weight['weight_{}'.format(i)])
        gpa_weight['whole_weight'] += float(gpa_weight['whole_weight_{}'.format(i)])

    gpa_100_dic['GPA'] = format(gpa_100_dic['GPA'] / gpa_weight['weight'], '.2f')

    # 4.0
    # if you want the GPA including the optional curriculum, please change the weight to whole_weight of gpa_weight
    for i in range(int(len(grade_series)/2)):
        i += 1
        gpa_4_dic['GPA_{}'.format(i)] = []
        temp_result = 0
        for j in range(len(grade_series['grade_{}'.format(i)])):
            if grade_series['grade_{}'.format(i)][j] >= 85:
                temp_result = temp_result + 4 * grade_series['weight_{}'.format(i)][j]
            elif grade_series['grade_{}'.format(i)][j] < 60:
                temp_result += 1.5 * grade_series['weight_{}'.format(i)][j]
            else:
                temp_result += (4 - 0.1 * (85 - grade_series['grade_{}'.format(i)][j])) * grade_series['weight_{}'.format(i)][j]
        if sum(grade_series['weight_{}'.format(i)]) != 0:
            gpa_4_dic['GPA_{}'.format(i)] = format(temp_result / sum(grade_series['weight_{}'.format(i)]), '.2f')
        else:
            gpa_4_dic['GPA_{}'.format(i)] = 0
        gpa_4_dic['GPA'] += float(gpa_4_dic['GPA_{}'.format(i)])*gpa_weight['weight_{}'.format(i)]

    gpa_4_dic['GPA'] = format(gpa_4_dic['GPA'] / gpa_weight['weight'], '.2f')

    print(pd.Series(gpa_4_dic))
    print(pd.Series(gpa_100_dic))
    print(pd.Series(gpa_weight))

    return gpa_4_dic, gpa_100_dic


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    Filepath = filedialog.askopenfilename()

    # get data from excel & transform them to lists
    data_frame = pd.read_excel("{}".format(Filepath), keep_default_na=False)
    subject_name_list = data_frame['subject'].tolist()
    grade_list = data_frame['grade'].tolist()
    weight_list = data_frame['weight'].tolist()
    genre_list = data_frame['genre'].tolist()
    semester_list = data_frame['semester'].tolist()

    grade_Dic, genre_Dic = grade_analyze(grade=grade_list, weight=weight_list, genre=genre_list, semester=semester_list)
    grade_calculate(grade_Dic, genre_Dic)

    # for packaging
    print('press ENTER to quit')
    input()
