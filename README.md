# Time Series Mining Final Project

This project is the final project of 2110430 Time Series Mining and Knowledge Discovery in Semester 2/2020 Computer Engineering of Chulalongkorn University

The project is seperated in 2 parts below.

## Part 1: Optimal weight for DTW distance calculation

This part is to experiment the DTW distance calculation between two time series sequences, regarding Sakoe and Chiba (1978)'s paper: Dynamic programming algorithm optimization for spoken word recognition (DOI: [10.1109/TASSP.1978.1163055](https://doi.org/10.1109/TASSP.1978.1163055))

In classification tasks in the dataset, we will classify the time series datasets into many classes, by considering the distance between the sequences. Thus, before making classification tasks, we have to complete the distance tasks.

The easiest way to calculate how far between two time series sequences is finding the difference at each pair of the data points from two time series sequences. This method is called Euclidean distance.

![Euclidean distance vs DTW](https://i.imgur.com/tfqoIFR.png)\
*Euclidean distance\
Credit: GUNA, J. et al. (DOI: [10.1007/s11042-013-1635-1](https://doi.org/10.1007/s11042-013-1635-1))*

But in many cases, e.g. spoken words (from Sakoe and Chiba (1978)'s paper), the euclidean method will give the inaccurate distance, because this type of time series sequences usually gave the distort shape, so that Euclidean distance might gave the bad results.

One of the accurate way of distance tasks is DTW algorithm. To briefly explain about the algorithm, firstly, the DTW algorithm is the distance function for calculating how far between two time series sequences by matching the points that will give the smallest distance.

![DTW: Dynamic Time Warping](https://upload.wikimedia.org/wikipedia/commons/a/ab/Dynamic_time_warping.png)\
*Dynamic Time Warping (DTW)\
Credit: [Wikipedia](https://commons.wikimedia.org/wiki/File:Dynamic_time_warping.png)*

In Sakoe and Chiba (1978)'s paper

![Caption](img/)\
*Caption\
Credit: Sakoe H, Chiba S. (DOI: [10.1109/TASSP.1978.1163055](https://doi.org/10.1109/TASSP.1978.1163055))*

In this project, we make an experiment by modifying the weights to find that what is the optimal values of the weights that make the accuracy better. Moreover, we considered other cells instead of the three modified neighboring cells and find out the effect on the classification accuracy

The implemented python codes ```dtw.py``` and ```dtw_p.py``` modified from ```dtw.py``` in [eug/dynamic-time-warping](https://github.com/eug/dynamic-time-warping) 

Our experiment is on the ECG200 datasets, that are attached in this repo.

We seperated the test into 2 parts.
### 1a: 

The summary is, we can't find the optimal values of the weights, but we can find that the weight that have the most significantly affect to the classification accuracy is 

### 1b:


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
