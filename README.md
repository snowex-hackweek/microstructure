# Microstructure Project

## Folders

### `notebooks`
Notebooks that are considered delivered results for the project should go in here.

### `scripts`

* download_nsidc.py - Downloads data from the nsidc using file extentions and patterns

## Project Summary

The goal is to evaluate the SMP to SSA conversion coefficients presented by [Calonne et al. 2020](https://tc.copernicus.org/articles/14/1829/2020/)
on the Grand Mesa Dataset.

### Collaborators on this project

* Anna Valentine 
* Michael Durand 
* Robbie Mallet 
* Mel Sandells
* Batuhan Osmanoglu
* Micah Johnson 

### The problem

What problem are you going to explore? Provide a few sentences. If this is a technical exploration of software or data science methods, explain why this work is important in a broader context.

### Application Example

Accurate characterisation of snow microscture is critical for for understanding volume scattering from airborne and spaceborne radars and radiometers.

### Sample data

#### SMP data (Full) 
    * SNEX20_SMP_S19M1285_1S17_20200208.CSV, SNEX20_SMP_S19M1284_1S17_20200208.CSV, SNEX20_SMP_S19M1287_1S17_20200208.CSV, SNEX20_SMP_S19M1289_1S17_20200208.CSV
    * SNEX20_SMP_S19M1174_2N13_20200206.CSV, SNEX20_SMP_S19M1175_2N13_20200206.CSV, SNEX20_SMP_S19M1172_2N13_20200206.CSV, SNEX20_SMP_S19M1173_2N13_20200206.CSV
    * SNEX20_SMP_S19M1261_2S16_20200208.CSV, SNEX20_SMP_S19M1262_2S16_20200208.CSV, SNEX20_SMP_S19M1268_2S16_20200208.CSV, SNEX20_SMP_S19M1269_2S16_20200208.CSV, SNEX20_SMP_S19M1260_2S16_20200208.CSV
    * SNEX20_SMP_S19M1256_2S7_20200208.CSV, SNEX20_SMP_S19M1255_2S7_20200208.CSV, SNEX20_SMP_S19M1243_2S7_20200208.CSV, SNEX20_SMP_S19M1257_2S7_20200208.CSV, SNEX20_SMP_S19M1244_2S7_20200208.CSV, SNEX20_SMP_S19M1240_2S7_20200208.CSV
    * SNEX20_SMP_S19M1145_9C16_20200205.CSV, SNEX20_SMP_S19M1152_9C16_20200205.CSV, SNEX20_SMP_S19M1134_9C16_20200205.CSV, SNEX20_SMP_S19M1150_9C16_20200205.CSV, SNEX20_SMP_S19M1151_9C16_20200205.CSV
    
    ```bash
        cd scripts/
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 1S17_20200208 --file_ext PNT
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 2N13_20200206 --file_ext PNT
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 2S16_20200208 --file_ext PNT
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 2S7_20200208 --file_ext PNT
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 9C16_20200205 --file_ext PNT
    ```

### Specific Questions

* Are the coefficients provided derived by Neige Colonne and Martin Proksh valid at Grand Mesa? 
* Which is better?
* If not can we calibrate our own?


### Proposed methods/tools

* https://github.com/mjsandells/snowmicropyn - contains the implemented Colonne Coefficients.

### Background reading

* [King et al. 2020](https://doi.org/10.5194/tc-14-4323-2020)
* [Calonne et al. 2020](https://tc.copernicus.org/articles/14/1829/2020/)
