import pandas as pd
import numpy as np
import math
from itertools import product

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

from scipy.spatial import distance
def dtw_sakoe_chiba(s, t,w1,w2,w3, w=7):
    n, m = len(s), len(t)
    w = abs(n - m) + w
    dtw = matrix(n, m, default=math.inf)
    dtw[0][0] = 0

    for i in range(1, n):
        min_row_score = math.inf
        for j in range(max(1, i-w), min(m, i+w)):
            cost = distance.euclidean(s[i], t[j])
            dtw[i][j] = min( (w1*cost)+dtw[i][j-1],(w2*cost)+ dtw[i-1][j-1],(w3*cost)+dtw[i-1][j])
            min_row_score = min(min_row_score, dtw[i][j])

    return dtw[-1][-1]

def predict(train,test,w1,w2,w3):   
    y_pred = []
    confusion_matrix = {}

    labels = np.unique([label for label, _ in train])
    for l1 in labels:
        confusion_matrix[l1] = {}
        for l2 in labels:
            confusion_matrix[l1][l2] = 0

    for tsl, t in test:
        pred_label, min_score = -1, math.inf

        for trl, s in train:
            score = dtw_sakoe_chiba(s, t,w1,w2,w3)
            if score < min_score:
                min_score = score
                pred_label = trl

        confusion_matrix[tsl][pred_label] = confusion_matrix[tsl][pred_label] + 1

        y_pred.append(tsl == pred_label)

    accuracy = (confusion_matrix[-1.0][-1.0]+confusion_matrix[1.0][1.0])/len(y_pred)
    return y_pred,confusion_matrix,accuracy

train,test = read_input()
weight = [0, 1, 2, 3]

for i in product(weight, repeat=3):
  y_pred,confusion_matrix,accuracy = predict(train,test,i[0],i[1],i[2])
  print(f"{i}: Accuracy is {accuracy}")