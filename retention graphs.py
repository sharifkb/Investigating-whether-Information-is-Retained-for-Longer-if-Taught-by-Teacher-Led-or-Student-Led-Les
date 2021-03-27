# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:14:23 2020

@author: shari
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mpl.rc('font', family='serif')

xl = pd.ExcelFile(r"C:\Users\shari\OneDrive\Documents\Work\3rd Yr\Teaching\Project prep\Test results.xlsx")
df = xl.parse('Sheet1')

as1 = df.iloc[:,0][9:]
a21 = df.iloc[:,0][:9]

as2 = df.iloc[:,1][9:]
a22 = df.iloc[:,1][:9]

as3 = df.iloc[:,2][9:]
a23 = df.iloc[:,2][:9]

as4 = df.iloc[:,3][9:]
a24 = df.iloc[:,3][:9]

# asav1 = [np.average(as1), np.average(as2)]/np.average(as1)
# asav2 = [np.average(as3), np.average(as4)]/np.average(as3)
# a2av1 = [np.average(a21), np.average(a22)]/np.average(a21)
# a2av2 = [np.average(a23), np.average(a24)]/np.average(a23)

# as_err1 = [np.std(as1), np.std(as2)]/np.average(as1)
# as_err2 = [np.std(as3), np.std(as4)]/np.average(as3)
# a2_err1 = [np.std(a21), np.std(a22)]/np.average(a21)
# a2_err2 = [np.std(a23), np.std(a24)]/np.average(a23)

asav1 = [np.average(as1), np.average(as2)]
asav2 = [np.average(as3), np.average(as4)]
a2av1 = [np.average(a21), np.average(a22)]
a2av2 = [np.average(a23), np.average(a24)]

as_err1 = [np.std(as1), np.std(as2)]
as_err2 = [np.std(as3), np.std(as4)]
a2_err1 = [np.std(a21), np.std(a22)]
a2_err2 = [np.std(a23), np.std(a24)]


# x1 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

# x2 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,]

x1 = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]

attempt = [0,1]

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(attempt, asav1, color ="k")
plt.plot(x1, [*as1, *as2] , "o", color = "r")
plt.errorbar(attempt, asav1, yerr = as_err1, fmt = "none", color = "g")
plt.ylabel(r"Test result, %", fontsize = 18)
plt.xlabel(r"Week", fontsize = 18)   
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(attempt, asav2, color ="k")
plt.plot(x1, [*as3, *as4] , "o", color = "r")
plt.errorbar(attempt, asav2, yerr = as_err2, fmt = "none", color = "g")
plt.ylabel(r"Test result, %", fontsize = 18)
plt.xlabel(r"Week", fontsize = 18)   
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(attempt, a2av1, color ="k")
plt.plot(x2, [*a21, *a22] , "o", color = "r")
plt.errorbar(attempt, a2av1,yerr = a2_err1, fmt = "none", color = "g")
plt.ylabel(r"Test result, %", fontsize = 18)
plt.xlabel(r"Week", fontsize = 18)   
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tight_layout()
plt.show()

fig1 = plt.figure(figsize=(8,5.5)) 
plt.plot(attempt, a2av2, color ="k")
plt.plot(x2, [*a23, *a24] , "o", color = "r")
plt.errorbar(attempt, a2av2,yerr = a2_err2, fmt = "none", color = "g")
plt.ylabel(r"Test result, %", fontsize = 18)
plt.xlabel(r"Week", fontsize = 18)   
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tight_layout()
plt.show()

