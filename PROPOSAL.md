# US tech layoffs 2022

**Author**: SRI RAM TEJA IALAM

**Date**: 11/26/2022

**Reviewer**: VYSHNAVI MULAKALAPALLI


## Motivation
As US is in recession, most of the employees have been laid off in 2022 in US Tech sector . This project investigates about companies and industries which have major impact due to this recession.

## Investigative Questions 

1) What are the industries that have major impact?

2) What kind of companies are having more impact?(public or private)

3) What is the impact of layoffs in each city?


## Approach 

* This Dataset is about list of top companies that have laid off their employees in 2022.
* This dataset is from crunchbase website,size is about 355 rows and 9 columns.
* Keerthi vedantham is the one who contributed to the dataset.
* The date of recent update in the dataset is 14th November 2022.

* For the project ,I want to remove the last column notes ,because it won't make any impact. We can store details of each 
  company in the form of lists with tuples as their elements.

  * Data: [(company name,Industry,no of layoffs reported,% of workforce impacted,company status,HQ)]

* I am planning to develop the project by creating 3 different directories named apps, data and tests. 

* Apps contain a .py file with a class with class name as `Layoffs` and defining 3 different methods in which each method can be able to answer one of my investigative questions.

* I am planning to use dictionaries, lists and their operations while implementing these methods.

* Tests folder contains a .py file which contains the testcases and Data folder contains .txt files which has the data.


## Expected Results 

* Get the industries which have more impact due to recession. This will be represented by using dictionary in which keys are the names of the industry and values are the ranks representing the impact - if rank is low, impact is high.
* Get the impact on private and public companies. This will be represented by a dictionary in which key is the company status like private or public and value is dictionary, with keys representing the range of percentage of impact, values representing list of companies in that percentage range.
* Get the impact of layoffs in each city. This will be represented by a dictionary in which keys are the names of city and values are the percentage of impact in each city.

## New Python Packages or Modules

* import os - This module will be used for identifying the current directory.
* import unittest - This module provides a rich set of tools for constructing and running tests.


## Dataset Documentation
The dataset is taken from crunchbase webiste https://news.crunchbase.com/startups/tech-layoffs-2022/
using the dataset we can build the methods we need as mentioned above.
1. Name of the dataset is `US Tech Layoffs in 2022`.
2. It is the latest version and last updated on November 14, 2022.
3. Owner of dataset is Keerthi Vedantham.
4. The dataset is dedicated to public domain and anybody can access it.
5. Data Information:

   * Company: Name of the company

   * Reported Layouts: No of reported Layouts

   * Workers impacted: Percentage of workers impacted in the respective company

   * Reported date:Date which Layoff's reported

   * Industry: Type of Industry

   * HQ: Headquarters of company

   * Source:In which the article is published

   * Company status: whether is private or public




