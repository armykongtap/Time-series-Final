from itertools import product

import numpy as np
import pandas as pd

import dba

df = pd.read_csv("ECG200_TRAIN", header=None, index_col=0, delim_whitespace=True)
df = df.T.reset_index(drop=True).T
df.index.name = "label"

#%%
# Find the represent of data group
def _dba(df):
    series = df.to_numpy()
    avg_series = dba.performDBA(series)
    return pd.DataFrame([avg_series])


df_dba = df.groupby("label").apply(_dba).reset_index(level=1, drop=True)

#%%


def custom_dtw(s, t, w1=1, w2=1, w3=1):
    n, m = len(s), len(t)
    dtw_matrix = np.full((n + 1, m + 1), np.inf)
    dtw_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(s[i - 1] - t[j - 1])
            # take last min from a square box
            last_min = np.min(
                [
                    w1 * dtw_matrix[i - 1, j],
                    w2 * dtw_matrix[i - 1, j - 1],
                    w3 * dtw_matrix[i, j - 1],
                ]
            )
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix[-1, -1]


def classify_dtw(s, df, *args) -> float:
    """
    Input
        - s: Series of data to classify
        - df: Dataframe represent group of data
    """
    res = 0.0
    dis = float("inf")

    for index, row in df.iterrows():
        d = custom_dtw(s, row, *args)
        if d < dis:
            res = index
            dis = d

    return res


#%%
# Test with diff weight
df = pd.read_csv("ECG200_TEST", header=None, index_col=0, delim_whitespace=True)
df = df.T.reset_index(drop=True).T
df.index.name = "label"

for i in product([1, 2, 3], repeat=3):
    result = df.apply(classify_dtw, axis=1, args=(df_dba, *i))

    result = result.to_frame("predict")
    result = result.reset_index()

    accuracy = (result["predict"] == result["label"]).sum() / result.shape[0]

    print(f"{i}: Accuracy is {accuracy}")
