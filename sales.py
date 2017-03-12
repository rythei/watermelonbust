#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:12:34 2017

@author: RyThei
"""

import pandas as pd


df = pd.read_csv('orders_in.csv')

chapters = ['ΚΔ', 'ΑΦ', 'ΔΓ', 'ΔΖ', 'ΑΔΠ', 'ΑΧΩ', 'ΚΑΘ', 'ΚΚΓ', 'ΠΒΦ', 'ΣK', 'ΧΩ']


c = ['Kappa Delta','Alpha Phi', 'Delta Gamma', 'Delta Zeta', 'Alpha Delta Pi','Alpha Chi Omega', 'Kappa Alpha Theta', 'Kappa Kappa Gamma', 'Pi Beta Phi', 'Sigma Kappa', 'Chi Omega']
s = [0]*len(c)

sales = pd.DataFrame([c,s])
sales = sales.T
sales.columns = ['Chapter','Sales']

translate = dict({'ΚΔ':'Kappa Delta', 'ΑΦ':'Alpha Phi', 'ΔΓ': 'Delta Gamma', 'ΔΖ':'Delta Zeta', 'ΑΔΠ': 'Alpha Delta Pi', 'ΑΧΩ':'Alpha Chi Omega', 'ΚΑΘ': 'Kappa Alpha Theta', 'ΚΚΓ':'Kappa Kappa Gamma', 'ΠΒΦ':'Pi Beta Phi', 'ΣK':'Sigma Kappa', 'ΧΩ': 'Chi Omega'})

for chapter in chapters:
    t = 0
    for sale in df['name']:
        if chapter in sale:
            sales.loc[sales.Chapter == translate[chapter],'Sales'] = sales.loc[sales.Chapter == translate[chapter],'Sales'] + df.loc[t, 'quantity']
        t= t+1


sales.to_csv('orders_out.csv',index=False)