# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:13:10 2018

@author: roy
"""

import numpy as np, pandas as pd, matplotlib.pyplot as plt

a = 1; b = 11; r = 10
runs = 1000000; people = 30

pay = np.array([0, 0, 0, 44.145, 44.145, 22.070, 22.070, 14.695, 14.695, 11.025, 11.025, 8.820, 11.025, 11.025, 
                    14.695, 14.695, 22.070, 22.070, 44.145, 44.145])
bet = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1])

def test(a, b, r, pay, bet):
    out = np.array([np.random.choice(range(a,b), size = r, replace = False)])[:,0:2].sum()
    reward = pay[out]*bet[out]
    return reward

process = np.array([[test(a, b, r, pay, bet) for j1 in range(runs)]for j2 in range(people)]).mean(axis = 1)/bet.sum()

plt.boxplot(process); plt.show()
