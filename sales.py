#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:12:34 2017

@author: RyThei
"""

import pandas as pd

PI_PHI_MENS = 65
THETA_MENS = 15
ADPI_MENS = 1
DZ_MENS = 23
APHI_MENS = 7
DG_MENS = 3
AXO_MENS = 8
KKG_MENS = 2
KD_MENS = 1


df = pd.read_csv('orders_in.csv')

chapters = ['ΚΔ', 'ΑΦ', 'ΔΓ', 'ΔΖ', 'ΑΔΠ', 'ΑΧΩ', 'ΚΑΘ', 'ΚΚΓ', 'ΠΒΦ', 'ΣK', 'ΧΩ']


c = ['Kappa Delta','Alpha Phi', 'Delta Gamma', 'Delta Zeta', 'Alpha Delta Pi','Alpha Chi Omega', 'Kappa Alpha Theta', 'Kappa Kappa Gamma', 'Pi Beta Phi', 'Sigma Kappa', 'Chi Omega']
v = [0]*len(c)
t = [0]*len(c)
d = [0]*len(c)
tot = [0]*len(c)

sales = pd.DataFrame([c,v,t,d,tot])
sales = sales.T
sales.columns = ['Chapter','Visors', 'Tanks', 'DBacks', 'Adjusted Total (1*Visors + 2*Tanks)']

translate = dict({'ΚΔ':'Kappa Delta', 'ΑΦ':'Alpha Phi', 'ΔΓ': 'Delta Gamma', 'ΔΖ':'Delta Zeta', 'ΑΔΠ': 'Alpha Delta Pi', 'ΑΧΩ':'Alpha Chi Omega', 'ΚΑΘ': 'Kappa Alpha Theta', 'ΚΚΓ':'Kappa Kappa Gamma', 'ΠΒΦ':'Pi Beta Phi', 'ΣK':'Sigma Kappa', 'ΧΩ': 'Chi Omega'})
donations = np.array([0,0,0,0,0])


for chapter in chapters:
    t = 0
    for sale in df['name']:
        if chapter in sale:
            if 'Visor' in sale:
                sales.loc[sales.Chapter == translate[chapter],'Visors'] = sales.loc[sales.Chapter == translate[chapter],'Visors'] + df.loc[t, 'quantity']
            elif 'Tank' in sale:
                sales.loc[sales.Chapter == translate[chapter],'Tanks'] = sales.loc[sales.Chapter == translate[chapter],'Tanks'] + df.loc[t, 'quantity']
            elif 'Diamondbacks' in sale:
                sales.loc[sales.Chapter == translate[chapter], 'DBacks'] = sales.loc[sales.Chapter == translate[chapter], 'DBacks'] +df.loc[t, 'quantity']
        #if 'Donate' in sale:
         #       print(sale)
                
        t= t+1
 
for i in range(len(df['name'])):
    if 'Donate' in df.loc[i,'name']:
       donations = np.vstack((donations,df.loc[i,:]))
       
donations = pd.DataFrame(donations)

sales.loc[sales.Chapter == "Pi Beta Phi", "Tanks"] = sales.loc[sales.Chapter == "Pi Beta Phi", "Tanks"] + PI_PHI_MENS
sales.loc[sales.Chapter == "Kappa Alpha Theta", "Tanks"] = sales.loc[sales.Chapter == "Kappa Alpha Theta", "Tanks"] + THETA_MENS
sales.loc[sales.Chapter == "Alpha Delta Pi", "Tanks"] = sales.loc[sales.Chapter == "Alpha Delta Pi", "Tanks"] + ADPI_MENS
sales.loc[sales.Chapter == "Delta Zeta", "Tanks"] = sales.loc[sales.Chapter == "Delta Zeta", "Tanks"] + DZ_MENS
sales.loc[sales.Chapter == "Alpha Phi", "Tanks"] = sales.loc[sales.Chapter == "Alpha Phi", "Tanks"] + APHI_MENS
sales.loc[sales.Chapter == "Delta Gamma", "Tanks"] = sales.loc[sales.Chapter == "Delta Gamma", "Tanks"] + DG_MENS
sales.loc[sales.Chapter == "Kappa Kappa Gamma", "Tanks"] = sales.loc[sales.Chapter == "Kappa Kappa Gamma", "Tanks"] + KKG_MENS
sales.loc[sales.Chapter == "Kappa Delta", "Tanks"] = sales.loc[sales.Chapter == "Kappa Delta", "Tanks"] + KD_MENS
sales.loc[sales.Chapter == "Alpha Chi Omega", "Tanks"] = sales.loc[sales.Chapter == "Alpha Chi Omega", "Tanks"] + AXO_MENS

sales['Adjusted Total (1*Visors + 2*Tanks)'] = sales['Visors'] + 2*sales['Tanks']

#sales.to_csv('orders_out.csv',index=False)