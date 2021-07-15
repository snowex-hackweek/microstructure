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

This downloads the profiles found with in the date and site id constraints shown in the which_pit.ipynb notebook.

*Warning* You must have the `.netrc` file as described by the NSIDC here on [programmatic access](https://nsidc.org/support/how/v0-programmatic-data-access-guide)


To download all the SMP profiles taken by the pit for our locations just use
``` bash
    cd scripts/
    python download_nsidc.py --just_give_it_to_me smp_sources.txt --output ../data/SMP/
```

Otherwise here is an example to get the data from nsidc using our script using pattern searching and file extensions

``` bash
    cd scripts/
    python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_pattern 1S17_20200208 --file_ext PNT
```

* https://nsidc.org/sites/nsidc.org/files/technical-references/SNEX20_SMP_FieldNotes.xlsx


### Specific Questions

* Are the coefficients provided derived by Neige Colonne and Martin Proksh valid at Grand Mesa? 
* Which is better?
* If not can we calibrate our own?


### Proposed methods/tools

* https://github.com/mjsandells/snowmicropyn - contains the implemented Colonne Coefficients.

### Background reading

* [King et al. 2020](https://doi.org/10.5194/tc-14-4323-2020)
* [Calonne et al. 2020](https://tc.copernicus.org/articles/14/1829/2020/)
