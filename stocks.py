import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from  sklearn.preprocessing import normalize


def stock_var(rvs,C,simulation_num,s0,k,position):
    bm =np.dot(C, rvs)
    sigma=0.25*np.ones(len(s0))
    r=0.05
    T=1.0
    sum = 0
    z = []

    for i in range(len(s0)):

        for j in range(len(bm[0])):
            st = s0[i] * np.exp(r * T - 0.5 * sigma[i] ** 2 * T + sigma[i] * np.sqrt(T) * bm[i][j])
            p = position[i]*(st - s0[i])
            z.append(p)
            sum += p

    return z







