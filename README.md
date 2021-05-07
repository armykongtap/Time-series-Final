# Time Series Mining Final Project

This project is the final project of 2110430 Time Series Mining and Knowledge Discovery in Semester 2/2020 Computer Engineering of Chulalongkorn University

The project is seperated in 2 parts below.

## Part I: Optimal weight for DTW distance calculation

In the DTW distance calculation between two time series sequences, regarding Sakoe and Chiba (1978)'s paper (DOI: [10.1109/TASSP.1978.1163055](https://doi.org/10.1109/TASSP.1978.1163055)), we modified the weights to find that what is the optimal values of the weights that make the accuracy better. Moreover, we considered other cells instead of the three modified neighboring cells and find out the effect on the classification accuracy

The implemented python codes ```dtw.py``` and ```dtw_p.py``` modified from ```dtw.py``` in [eug/dynamic-time-warping](https://github.com/eug/dynamic-time-warping) 

The summary is, we can't find the optimal values of the weights, but we can ...

## Part II: Shape averaging method

The project is about shape averaging method of multiple time series sequences. The method that using in this project called "DTA: Dynamic Time Warping Barycenter Averaging".

The implemented python code ```dba.py``` modified from [fpetitjean/DBA](https://github.com/fpetitjean/DBA) based on the papers below
* [Pattern Recognition 2011](http://francois-petitjean.com/Research/Petitjean2011-PR.pdf): A global averaging method for Dynamic Time Warping 
(DOI: [10.1016/j.patcog.2010.09.013](https://doi.org/10.1016/j.patcog.2010.09.013))
* [ICDM 2014](http://francois-petitjean.com/Research/Petitjean2014-ICDM-DTW.pdf): Dynamic Time Warping Averaging of Time Series allows Faster and more Accurate Classification
(DOI: [10.1109/ICDM.2014.27](https://doi.org/10.1109/ICDM.2014.27))
* [ICDM 2017](http://francois-petitjean.com/Research/ForestierPetitjean2017-ICDM.pdf): Generating synthetic time series to augment sparse datasets
(DOI: [10.1109/ICDM.2017.106](https://doi.org/10.1109/ICDM.2017.106))

## Members
1. Kongtap Arunlakvilart 6030033321
2. Kantorn Chitchuen 6030038521
3. Yanika Dontong 6031010021
