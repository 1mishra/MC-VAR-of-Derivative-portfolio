import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

def simu(data,C,s0,step,miu,delta_t,sigma,T,sim_num):
    bm = []
    for i in range(len(data)):
        temp = norm.rvs(loc=0, scale=1, size=step)
        bm.append(temp)
    bm=np.dot(C,bm)
    dynamics = []
    for x in range(len(data)):
        temp = [s0[x]]
        for j in range(step):
            ds = temp[-1] * (miu * delta_t + sigma*np.sqrt(delta_t) * bm[x][j])
            temp.append(ds + temp[-1])
        dynamics.append(temp)

    for i in range(len(dynamics)):
        plt.plot(np.linspace(0, T, step + 1), dynamics[i])



#s=s0*exp(ut+sigmawt)
def stockopt_var(rvs,C,simulation_num,s0,k,position):
    bm = np.dot(C, rvs)
    sigma=0.25*np.ones(len(s0))
    r=0.05
    T=1.0
    sum = 0
    z = []
    #generating Z

    for i in range(len(s0)):

        for j in range(len(bm[0])):
            st = s0[i] * np.exp(r * T - 0.5 * sigma[i] ** 2 * T + sigma[i] * np.sqrt(T) * bm[i][j])
            p = position[i]*max(0, st - k[i])
            z.append(p)
            sum += p

    return z






