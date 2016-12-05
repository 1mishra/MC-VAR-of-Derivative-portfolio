import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm


zerobond=0

def diffusion(time,sigma,sample=1):

    step=len(time)
    delta_t=(float(time[-1]-time[0]))/step
    brownian_one=norm.rvs(size=step,loc=0,scale=delta_t*np.sqrt(sigma))
    return brownian_one


def vasicek_model(time,r0,k,miu,sigma):
    step=len(time)
    delta_t = (float(time[-1] - time[0])) /step
    b=diffusion(time,sigma)
    short_rate=[r0]
    for i in range(len(time)):
        dr=k*(miu-short_rate[-1])*delta_t+b[i]
        short_rate.append(short_rate[-1]+dr)
    return short_rate


def bond_dynamic():

    T=1.0
    b=[0.87]
    steps=50
    r0=0.013 #parameters of short rate model
    miu=0.015 #parameters of short rate model
    sigma = 0.15 #parameters of short rate model
    k=3.8 #parameters of short rate model
    time=np.linspace(0,T,steps)
    delta_t=T/steps
    rvs= norm.rvs(loc=0, scale=1, size=steps)
    short_rate=vasicek_model(time,r0,k,miu,sigma)
    for i in range(len(time)):
        db=(b[-1]**2)*sigma*np.sqrt(delta_t)*rvs[i]+b[-1]*short_rate[i]*delta_t
        b.append(b[-1]+db)
    return b[-1]


def bondNopt_var(simulation_num, principle,opt_position):


    b=0.87#starting price
    strike=0.8# callbale strike
    z=[]
    zopt=[]
    for i in range(simulation_num):
        z.append(principle*(bond_dynamic()-b))
        v=opt_position*max(0,(bond_dynamic()-strike))
        zopt.append(v)

    return z,zopt




















