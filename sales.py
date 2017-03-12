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
v = [0]*len(c)
t = [0]*len(c)
tot = [0]*len(c)

sales = pd.DataFrame([c,v,t,tot])
sales = sales.T
sales.columns = ['Chapter','Visors', 'Tanks', 'Adjusted Total (1*Visors + 2*Tanks)']

translate = dict({'ΚΔ':'Kappa Delta', 'ΑΦ':'Alpha Phi', 'ΔΓ': 'Delta Gamma', 'ΔΖ':'Delta Zeta', 'ΑΔΠ': 'Alpha Delta Pi', 'ΑΧΩ':'Alpha Chi Omega', 'ΚΑΘ': 'Kappa Alpha Theta', 'ΚΚΓ':'Kappa Kappa Gamma', 'ΠΒΦ':'Pi Beta Phi', 'ΣK':'Sigma Kappa', 'ΧΩ': 'Chi Omega'})

for chapter in chapters:
    t = 0
    for sale in df['name']:
        if chapter in sale:
            if 'Visor' in sale:
                sales.loc[sales.Chapter == translate[chapter],'Visors'] = sales.loc[sales.Chapter == translate[chapter],'Visors'] + df.loc[t, 'quantity']
            elif 'Tank' in sale:
                sales.loc[sales.Chapter == translate[chapter],'Tanks'] = sales.loc[sales.Chapter == translate[chapter],'Tanks'] + df.loc[t, 'quantity']
        t= t+1
        
sales['Adjusted Total (1*Visors + 2*Tanks)'] = sales['Visors'] + 2*sales['Tanks']


sales.to_csv('orders_out.csv',index=False)