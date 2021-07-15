## Finds ground depth from .csv
from snowmicropyn import Profile,density_ssa, detection
import matplotlib.pyplot as plt
import pandas as pd

path = '../data/SMP/SNEX20_SMP*.PNT'
field_notes = '../data/SNEX20_SMP_FieldNotes.csv'

def list_files_local(path):
    """ Get file list form local folder. """
    from glob import glob
    return glob(path)

def find_m_num(profile):
    name = profile.name
    m_num = name[4:]
    return m_num

def find_ground(data_path):
    list_SMP_files = list_files_local(data_path)
    
    ## Read in our .csv file of field notes 
    df1 = pd.read_csv(field_notes, skiprows=9)
    
    g_detect = []
    sd_list = []
    names = []

    for file in list_SMP_files:
        p = Profile.load(file)
        ground = detection.detect_ground(p)
        m_num = find_m_num(p)
        m_num = int(m_num)
        
        #and finally, let's see what our .csv thinks the depth is
        row = (df1.loc[lambda df: df1["Fname sufix"] == m_num, :])
        sd = row["Snow depth"].values
        
        #Add a name id so for pd dataframe
        name = p.name
    
        #Add to our list
        g_detect.append(ground)
        sd_list.append(sd[0]*10)  #cm to mm
        names.append(name)
        
    #put it in a data frame and return
    df_depths = pd.DataFrame(list(zip(names, sd_list, g_detect)),
               columns =['Name', 'Field Notes Depth', "Ground Detect Depth"])
        
    return df_depths