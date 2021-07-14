# Microstructure Project

## Folders

### `notebooks`
Notebooks that are considered delivered results for the project should go in here.

### `scripts`

* download_nsidc.py - Downloads data from the nsidc using file extentions and patterns

## Project Summary

The goal is to evaluate the SMP to SSA conversion coefficients presented by [Colonne et al. 2020](https://tc.copernicus.org/articles/14/1829/2020/)
on the Grand Mesa Dataset.

### Project Title

Brief title describing the proposed work.

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

List one specific application of this work.

### Sample data

#### SMP data (Full) 

        ```bash
        cd scripts/
        python download_nsidc.py https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SMP.001/ --file_ext PNT
        ```

### Specific Questions

* Are the coefficients provided derived by Neige Colonne valid at Grand Mesa?
* If not can we calibrate our own?

### Existing methods

How would you or others traditionally try to address this problem?

### Proposed methods/tools

* https://github.com/mjsandells/snowmicropyn - contains the implemented Colonne Coefficients.

### Background reading

* [King et al. 2020](https://doi.org/10.5194/tc-14-4323-2020)
* [Calonne et al. 2020](https://tc.copernicus.org/articles/14/1829/2020/)
