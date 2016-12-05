import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from  sklearn.preprocessing import normalize
from stocks import*
from stock_options import *
from bonds_and_options import *


data = pd.read_excel("equity.xlsx", parse_dates=True)
# data.loc[:,"TSLA"]=normalize((data.loc[:,"TSLA"].values))[0]
# data.loc[:,"MAC"]=normalize((data.loc[:,"MAC"].values))[0]
# data.loc[:,"BIIB"]=normalize((data.loc[:,"BIIB"].values))[0]
# data.loc[:,"GS"]=normalize((data.loc[:,"GS"].values))[0]

data=data.as_matrix()
data=data.T

cov_matrix=np.corrcoef(data)
C=np.linalg.cholesky(cov_matrix)
Ct=C.transpose()


T=0.5
miu=0.03
sigma=0.08
step=100
delta_t=T/step
s0=data[:,0]
k=s0
simulation_num=10000
position=[-1000,-8000,2000,300]
stock_position=[900,700,-1500,-500]
zero_principle=20000.0
bondoptposition=-10000

rvs=[]
for i in range(len(s0)):
    temp = norm.rvs(loc=0, scale=1, size=simulation_num)
    rvs.append(temp)
bm = np.dot(C, rvs)


# for i in range(30):
#     simu(data,C,s0,step,miu,delta_t,sigma,T,simulation_num)
#
#
# plt.title("GBM STOCK DYNAMIC",fontsize=20)
# plt.ylabel("STOCK PRICE",fontsize=20)
# plt.grid()
# plt.show()





var_stock=stock_var(rvs,C,simulation_num,s0,k,stock_position)
var_stock_opt=stockopt_var(rvs,C,simulation_num,s0,k,stock_position)
var_bond,var_bond_opt=bondNopt_var(simulation_num,zero_principle,bondoptposition)



var_portfolio=var_stock+var_stock_opt+var_bond+var_bond_opt


plt.hist(var_portfolio,bins=400,alpha=0.40,color="slateblue")
plt.hist(var_bond_opt,bins=400,alpha=0.40,color="blue")
plt.hist(var_bond,bins=400,alpha=0.40,color="cyan")
plt.hist(var_stock_opt,bins=400,alpha=0.40,color="orange")
plt.hist(var_stock,bins=400,alpha=0.40,color="seagreen")
plt.legend(["TOTAL GAIN","FIXED INCOME DERIVATIVE GAIN","PLAIN BOND GAIN","STOCK OPTIONS GAIN","STOCK GAIN"])
plt.title("PORTFOLIO VALUE SAMPLES",fontsize=20)
plt.ylabel("SAMPLE NUMBERS",fontsize=20)
plt.ylim([0,1900])
plt.grid()
plt.show()
