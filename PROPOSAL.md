# US tech layoffs 2022

**Author**: SRI RAM TEJA IALAM
**Date**: 11/26/2022
**Reviewer**: VYSHNAVI MULAKALAPALLI


## Motivation
As US is in recession most of the employees have been laid off in 2022 in US Tech sector . So from the layoff.csv Dataset I want to know what are the 
industries that have an impact because of this recession. 


## Investigative Questions 

1)What are the industries that have major impact?

2)What kind of companies are having more impact?(public or private)

3)what percentage of workforce impacted in each company?

4)which company has more no of reported layouts ?

5)List the companies in ranges of percentage of workforce impacted?



## Approach 

* This Dataset is about list of top companies that have laid off their employees in 2022.

Data Information:

Company: Name of the company

Reported Layouts: No of reported Layouts

workers impacted: Percentage of workers impacted in the respective company

Reported date:Date which Layoff's reported

Industry: Type of Industry

HQ: Headquarters of company

source:In which the article is published

Company status: whether is private or public

notes:message of layoffs


We got the Dataset from crunchbase website,size is about 355 rows and 9 columns ,keerthi vedantham is the one who contributed to the dataset.
The date of recent update in the dataset is 14th November 2022.

* For the project ,I want to remove the last column notes ,because it won't make any impact. We can store details of each 
  company in lists, and we can use dictionaries  where company as key and remaining details are values .

* Data: [company name,Industry,no of layoffs reported,% of workforce impacted,company status,HQ]

* I am planning to develop the project by creating 3 different directories named apps, data and tests. 

* Apps contain a .py file with a class with class name as `Layoffs` and defining 3 different methods in which each method can be able to answer one of my investigative questions.

* I am planning to use dictionaries, lists and their operations while implementing these methods.

* Tests folder contains a .py file which contains the testcases and Data folder contains .txt files which has the data.


## Expected Results 

* For this project we can get the results of the highest layoff percentage by company wise in a particular month or till date.
What industries are getting affected most on layoffs. for this we can use dictionaries where company names are key and 
layoff numbers are values. we can also predict the highest layoffs reported in a month using dictionaries where company as key and layoffs numbers are values. 
we can also get no of private companies,public companies. for this we use dictionaries where company status as key and number as value.


## New Python Packages or Modules

* OS module will be used for identifying the current directory.
* CSV module will be used to read and write tabular data in CSV format.

## Dataset Documentation
The dataset is taken from crunchbase webiste https://news.crunchbase.com/startups/tech-layoffs-2022/
using the dataset we can build the methods we need as mentioned above.
1. Name of the dataset is `Layoffs`.
2. It is the latest version and last updated on November 14, 2022.
3. Owner of dataset is keerthi vedantham
4. The dataset is dedicated to public domain and anybody can access it.
5. Data Information:

    Company: Name of the company

    Reported Layouts: No of reported Layouts

    workers impacted: Percentage of workers impacted in the respective company

    Reported date:Date which Layoff's reported

    Industry: Type of Industry

    HQ: Headquarters of company

    source:In which the article is published

    Company status: whether is private or public

    notes:message of layoffs



