# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:06:30 2020

@author: shari
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mpl.rc('font', family='serif')
from scipy import optimize

xl = pd.ExcelFile(r"C:\Users\shari\OneDrive\Documents\Work\3rd Yr\Teaching\Project prep\Test results.xlsx")
df = xl.parse('Sheet1')

as1 = np.array(list(zip(df.iloc[:,0][9:].values, df.iloc[:,1][9:].values)))
a21 = np.array(list(zip(df.iloc[:,0][:9].values, df.iloc[:,1][:9].values)))

as2 = np.array(list(zip(df.iloc[:,2][9:].values, df.iloc[:,3][9:].values)))
a22 = np.array(list(zip(df.iloc[:,2][:9].values, df.iloc[:,3][:9].values)))


attempt = [0,1]

P1 = []
P2 = []
P3 = []
P4 = []

def test1(x,a,b):
    return a*np.e**(b*x)

i = 0
while i < len(as1):
    
    if as1[i][0]>as1[i][1]:
        p1, pcov1 = optimize.curve_fit(test1, attempt, as1[i], p0=[0, 0])
        P1.append(p1[1])
        
    if as2[i][0]>as2[i][1]:
        p2, pcov2 = optimize.curve_fit(test1, attempt, as2[i], p0=[0, 0])
        P2.append(p2[1])           
    i += 1

i = 0
while i < len(a21):
    
    if a21[i][0]>a21[i][1]:
        p3, pcov3 = optimize.curve_fit(test1, attempt, a21[i], p0=[0, 0])
        P3.append(p3[1])
    
    if a22[i][0]>a22[i][1]:
        p4, pcov4 = optimize.curve_fit(test1, attempt, a22[i], p0=[0, 0])
        P4.append(p4[1]) 
        
    i += 1

v1 = np.average(P1)
e1 = np.std(P1)
vhalf1 = np.round(np.log(2)/(-v1), 3)

v2 = np.average(P2)
e2 = np.std(P2)
vhalf2 = np.round(np.log(2)/(-v2), 3)

v3 = np.average(P3)
e3 = np.std(P3)
vhalf3 = np.round(np.log(2)/(-v3), 3)

v4 = np.average(P4)
e4 = np.std(P4)
vhalf4 = np.round(np.log(2)/(-v4), 3)

x = np.linspace(0,10, 10000)

fit1  = np.e**(v1*x)
fit2  = np.e**(v2*x)
fit3  = np.e**(v3*x)
fit4  = np.e**(v4*x)

fit5  = np.e**((v1+e1)*x)
fit6  = np.e**((v2+e2)*x)
fit7  = np.e**((v3+e4)*x)
fit8  = np.e**((v4+e4)*x)

fit9  = np.e**((v1-e1)*x)
fit10 = np.e**((v2-e2)*x)
fit11 = np.e**((v3-e4)*x)
fit12 = np.e**((v4-e4)*x)

n = 18


fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(x, fit1, color = "r")
plt.plot(x, fit5, color = "k")
plt.plot(x, fit9, color = "k")
plt.fill_between(x, fit5, fit9, color = "r",  alpha = 0.5)
plt.ylabel(r"Retained Knowledge", fontsize = n)
plt.xlabel(r"Week", fontsize = n)
plt.tick_params(axis='both', which='major', labelsize=n)
plt.ylim(0,1.2)
plt.annotate(r'$t_{1/2}$ = 1.164 weeks', fontsize = n, xy=(0.55, 0.95), xycoords='axes fraction')
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(x, fit2, color = "b")
plt.plot(x, fit6, color = "k")
plt.plot(x, fit10, color = "k")
plt.fill_between(x, fit6, fit10, color = "b",  alpha = 0.5)
plt.ylabel(r"Retained Knowledge", fontsize = n)
plt.xlabel(r"Week", fontsize = n)
plt.tick_params(axis='both', which='major', labelsize=n)
plt.ylim(0,1.2)
plt.annotate(r'$t_{1/2}$ = 0.829 weeks', fontsize = n, xy=(0.55, 0.95), xycoords='axes fraction')
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(x, fit3, color = "g")
plt.plot(x, fit7, color = "k")
plt.plot(x, fit11, color = "k")
plt.fill_between(x, fit7, fit11, color = "g",  alpha = 0.5)
plt.ylabel(r"Retained Knowledge", fontsize = n)
plt.xlabel(r"Week", fontsize = n)
plt.tick_params(axis='both', which='major', labelsize=n)
plt.ylim(0,1.2)
plt.annotate(r'$t_{1/2}$ = 0.739 weeks', fontsize = n, xy=(0.55, 0.95), xycoords='axes fraction')
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(x, fit4, color = "k")
plt.plot(x, fit8, color = "k")
plt.plot(x, fit12, color = "k")
plt.fill_between(x, fit8, fit12, color = "k",  alpha = 0.5)
plt.ylabel(r"Retained Knowledge", fontsize = n)
plt.xlabel(r"Week", fontsize = n)
plt.tick_params(axis='both', which='major', labelsize=n)
plt.ylim(0,1.2)
plt.annotate(r'$t_{1/2}$ = 0.968 weeks', fontsize = n, xy=(0.55, 0.95), xycoords='axes fraction')
plt.tight_layout()
plt.show()