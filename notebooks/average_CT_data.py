# function to define average CT data to specified intervals
#    by Mike Durand July 2021
#
#    ssa_CT is an array of 
#    height_min and height_max are the CT min and max heights for the CT compute samples
#    ssa_height is height above soil-snow interface for SSA at full ~1/2 mm resolution
#    SSA_SMP_avg is SSA from SMP averaged to the CT samples

import numpy as np
from scipy import interpolate

def average_CT_data(height_CT,ssa_CT,height_IS):

    f = interpolate.interp1d(height_CT, ssa_CT,bounds_error=False,fill_value='nan')
    ssa_CT_i = f(height_IS) 
    
    return ssa_CT_i