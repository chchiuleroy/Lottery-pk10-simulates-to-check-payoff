# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:13:10 2018

@author: roy
"""

import numpy as np; import pandas as pd
from joblib import Parallel, delayed; import multiprocessing

def game(x, a):
    u = []
    y = range(x[0], x[1])
    for i in range(a):
        u.append(np.random.choice(y, size = len(y), replace = False))
    u = np.array(u)
    v = np.sum(u[:, 0:2], axis = 1)
    pay = np.array([0, 0, 0, 44.145, 44.145, 22.070, 22.070, 14.695, 14.695, 11.025, 11.025, 8.820, 11.025, 11.025, 
                    14.695, 14.695, 22.070, 22.070, 44.145, 44.145])
    money = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1])
    w = []
    for j in range(np.shape(v)[0]):
        w.append(pay[v[j]]*money[v[j]])
    outcome = sum(w)/a/sum(money)
    return outcome

x = np.array([1, 11]); a = 1000000
run = 30
cores_n = multiprocessing.cpu_count(); n = cores_n - 4
results = Parallel(n_jobs = n, backend = "threading")(delayed(game)(x, a) for l in range(run))