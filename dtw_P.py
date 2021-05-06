import pandas as pd
import numpy as np
import math
from scipy.spatial import distance


def read_input(folder='/content'):
    train = pd.read_csv("ECG200_TRAIN", header=None, index_col=0, delim_whitespace=True)
    train = train.T.reset_index(drop=True).T
    train.index.name = "label"
    train = [(train.index[i],train.values.tolist()[i]) for i in range(len(train))]

    test = pd.read_csv("ECG200_TEST", header=None, index_col=0, delim_whitespace=True)
    test = test.T.reset_index(drop=True).T
    test.index.name = "label"
    test = [(test.index[i],test.values.tolist()[i]) for i in range(len(test))]

    return train, test


def matrix(n, m=None, default=0):
    m = m or n
    return [[default] * m for _ in range(n)]


def dtw_sakoe_chiba_P0_sym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0
    
    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(1):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min(g[i][j-1]+d[i][j],
                          g[i-1][j-1]+2*d[i][j],
                          g[i-1][j]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P0_asym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0
    
    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(1):
      d[0][i] = 0
      d[i][0] = 0

    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min(g[i][j-1],
                          g[i-1][j-1]+d[i][j],
                          g[i-1][j]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P05_sym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(3):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-1][j-3]+2*d[i][j-1]+d[i][j-1]+d[i][j],
                             g[i-1][j-2]+2*d[i][j-1]+d[i][j],
                             g[i-1][j-1]+2*d[i][j],
                             g[i-2][j-1]+2*d[i-1][j]+d[i][j],
                             g[i-3][j-1]+2*d[i-2][j]+d[i-1][j]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P05_asym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(3):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-1][j-3]+(d[i][j-2]+d[i][j-1]+d[i][j])/3,
                             g[i-1][j-2]+(d[i][j-1]+d[i][j])/2,
                             g[i-1][j-1]+d[i][j],
                             g[i-2][j-1]+d[i-1][j]+d[i][j],
                             g[i-3][j-1]+d[i-2][j]+d[i-1][j]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P1_sym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(2):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-1][j-2]+2*d[i][j-1]+d[i][j],
                             g[i-2][j-1]+2*d[i-1][j]+d[i][j],
                             g[i-1][j-1]+2*d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P1_asym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(2):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-1][j-2]+(d[i][j-1]+d[i][j])/2,
                             g[i-2][j-1]+d[i-1][j]+d[i][j],
                             g[i-1][j-1]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P2_sym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(3):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-2][j-3]+2*d[i-1][j-2]+2*d[i][j-1]+d[i][j],
                             g[i-3][j-2]+2*d[i-2][j-1]+2*d[i-1][j]+d[i][j],
                             g[i-1][j-1]+2*d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def dtw_sakoe_chiba_P2_asym(s, t, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    g = matrix(n, m, default=math.inf)
    g[0][0] = 0

    d = np.full((n, min(m, n+w)),np.inf)
    for i in range(3):
      d[0][i] = 0
      d[i][0] = 0
    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            d[i][j] = distance.euclidean(s[i], t[j])
            g[i][j] = min( g[i-2][j-3]+2*(d[i-1][j-2]+d[i][j-1]+d[i][j])/3,
                             g[i-3][j-2]+d[i-2][j-1]+d[i-1][j]+d[i][j],
                             g[i-1][j-1]+d[i][j])
            min_row_score = min(min_row_score, g[i][j])

    return g[-1][-1]


def predict(train,test,func):   
    y_pred = []
    confusion_matrix = {}
    accuracies = {}
    labels = np.unique([label for label, _ in train])
    for l1 in labels:
        confusion_matrix[l1] = {}
        for l2 in labels:
            confusion_matrix[l1][l2] = 0

    for tsl, t in test:
        pred_label, min_score = -1, math.inf

        for trl, s in train:
            score = func(s, t)
            if score < min_score:
                min_score = score
                pred_label = trl

        confusion_matrix[tsl][pred_label] = confusion_matrix[tsl][pred_label] + 1

        y_pred.append(tsl == pred_label)

    accuracy = (confusion_matrix[-1.0][-1.0]+confusion_matrix[1.0][1.0])/len(y_pred)
    return accuracy
