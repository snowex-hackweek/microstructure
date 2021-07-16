import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
import sys
from scipy.stats import binned_statistic
import warnings
from scipy.optimize import minimize
sys.path.insert(1,'../../snowmicropyn')
import snowmicropyn
from snowmicropyn import density_ssa

C20_window=1

def get_mct_frame(site):

    frames = pickle.load(open('../data/microCT/processed_mCT.p', 'rb'))

    mct_df = frames[site]

    mct_df = mct_df.drop_duplicates(subset='height_ave (cm)',keep="first")

    mct_df.set_index('height_ave (cm)', inplace=True)
    
    return(mct_df)

def get_ssa(p, coeffs_dict):

    df = snowmicropyn.density_ssa.calc(p.samples,
                                            coeff_model=coeffs_dict,
                                            window=C20_window,
                                            overlap=50)

    df = df[(df['distance'] < p.ground)]

    df['distance_up'] = (p.ground - df['distance'])/10

    df.set_index('distance_up',inplace=True)

    df.sort_index()

    df.dropna(how='any')
    
    return df

def resample_SMP_to_mCT(mct_df, df):
    
    com_df = mct_df.copy()
    
    com_df['ssa'] = [np.nanmean(df['ssa'][(df.index < u) & (df.index > l)]) 
                      for l, u in zip(mct_df['height_min (cm)'], mct_df['height_max (cm)'])   ]
        
    return com_df

def compare_smp_to_mct(coeffs_list,mct_df,p,eqn='ssa'):
    
    coeffs_dict = {'density': [295.8, 65.1, -43.2, 47.1],
                  'ssa':coeffs_list,
                  'equation':eqn}

    df = get_ssa(p, coeffs_dict)
    
    com_df = resample_SMP_to_mCT(mct_df, df)
    
    return(com_df)

def calc_RMSE(coeffs_list,mct_df,p, print=True, eqn='ssa'):
    
    com_df = compare_smp_to_mct(coeffs_list,mct_df,p,eqn)
    
    RMSE = np.sqrt(np.nanmean(np.square(com_df['SSA (m2/kg)']-com_df['ssa'])))
    
    if print: print(RMSE)
    
    return RMSE
