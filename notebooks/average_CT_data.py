# function to define SMP height, average SMP data to specified intervals, and support (future)
#    work to rescale or shift profile if necessary
#    by Mike Durand June 2021
#
#    ssa_smp is a pandas dataframe with data at e.g. ~1/2 mm resolution data from SMP. length ~2000 
#    height_min and height_max are the CT min and max heights for the CT compute samples
#    ssa_height is height above soil-snow interface for SSA at full ~1/2 mm resolution
#    SSA_SMP_avg is SSA from SMP averaged to the CT samples

import numpy as np

def average_CT_data(ssa_smp,height_min,height_max):

    ssa_height=(max(height_max*10)-ssa_smp.distance)/10

    nCT=len(height_min)
    SSA_SMP_avg=np.empty(nCT)

    for i in range(nCT):
        idx=np.where( (ssa_height > height_min[i]) & (ssa_height < height_max[i]))
        SSA_SMP_avg[i]=ssa_smp.iloc[idx].ssa.mean()
    
    return ssa_height, SSA_SMP_avg