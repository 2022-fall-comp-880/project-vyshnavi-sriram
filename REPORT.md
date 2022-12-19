# Project Report
## Authors - Sriram and Vyshnavi

## 1. Purpose 

* The dataset used for the project is regarding the US Tech Layoffs in 2022.
* This dataset is taken from crunchbase website - `https://news.crunchbase.com/startups/tech-layoffs-2022/`
* Author of this dataset is **Keerthi Vedantham**.
* The dataset was last updated on December 9,2022.
* The dataset has 355 rows and 8 attributes which provides details about the layoffs in different companies.
* The attributes are:
     * Company: Name of the company

     * Reported Layouts: No of reported Layouts

     * Workers impacted: Percentage of workers impacted in the respective company

     * Reported date:Date which Layoff's reported

     * Industry: Type of Industry

     * HQ: Headquarters of company

     * Source:In which the article is published
  
     * Company status: whether is private or public

* In this project, we have investigated on the below questions:
  1) What are the industries that have major impact?

  2) What are the ranges of percentage of impact in each type of company(public or private)? What are the companies in those ranges.

  3) What is the impact of layoffs in each city?

## 2. Approach 

### What are the industries that have major impact?

* Initially an empty dictionary named `company_dict` will be created.
* Using a **for** loop, dictionary `company_dict` is transformed into a dictionary with keys as the industry names and values as the total number of layoffs in each industry.
* Next all the values of this dictionary which are total number of layoffs in different industries will be stored in a list `lst`.
* This list `lst` will be sorted and reversed in order to have the elements in the list in descending order.
* A variable `rank` is created and 1 is assigned to it.
* Next using another **for** loop, all the values in dictionary `company_dict` and elements in the list `lst` will be compared.
* In the dictionary `company_dict`, the key which has its value as the first element(the highest number of layoffs) in list `lst` is taken as key to another new dictionary `comp_dict` and give its value as `rank` which indicates its impact.
* The above step is repeated for all the values in dictionary `company_dict` and rank is incremented during each key-value assignment to dictionary `comp_dict`.
* Now the dictionary `comp_dict` has the industry names as keys and its values are the ranks indicating its level of impact.

### What are the ranges of percentage of impact in each type of company(public or private)? What are the companies in those ranges?

* Initially an empty dictionary `company_impact` is created to store the output.
* Using a **for** loop, the keys of dictionary are created based on dataset representing type of company like public or private.
* The values of dictionary are list of tuples with each tuple containing company name and percentage of its impact.
* Now use a **for** loop to call the method `determine_ranges` on each of the values of dictionary `company_impact`.
* Then the values of the dictionary `company_impact` will be transformed into dictionaries with keys as the ranges of percentage impact and values as the list of companies in that range.
* Now the dictionary `company_impact` has keys as industry names, and its values as another dictionary with the keys as ranges and values are list of companies fall in that ranges.

### What is the impact of layoffs in each city?

* Initialize the empty dictionary `impacted_city` is created to store the output.

* Create a variable `total_layoffs` and initialize with zero to store the total layoffs of companies.

* Using a **for** loop ,the keys and values are dictionary are created where keys are cities and values are layoffs of the company that is located in the key city.

* And also focus on total layoffs by adding each company layoffs irrespective of city.

* Use another **for** loop and iterate over keys which are cities ,for each city calculate the city layoff percentage using formula
**layoff% = (no of layoffs of each city / total no of layoffs) * 100**

* round the value to 2 decimals and then append % symbol to the value and update the value of the respective key('City')

* After iteration of all the keys return the result dictionary `impacted_city`

## 3. Testing 

* Unittest library is used for testing the project results. This library can be imported by using `import unittest`.

### class TestLayoffsMostImpactedIndustries(TestCase)

The class `TestLayoffsMostImpactedIndustries` has testing methods to test the method `most_impacted_industries` in the class `Layoffs`.

#### def test_most_impacted_industries_empty(self):

* This method tests the method `most_impacted_industries` over an empty data file `layoffs_empty.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_industries` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

#### def test_most_impacted_industries_first_10(self):

* This method tests the method `most_impacted_industries` over a data file `layoffs_first_10.txt` which has the first ten entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_industries` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

#### def test_most_impacted_industries_last_5(self):

* This method tests the method `most_impacted_industries` over a data file `layoffs_last_5.txt` which has the last five entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_industries` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using

### class TestLayoffsMostImpactedTypeOfCompany(TestCase)

The class `TestLayoffsMostImpactedTypeOfCompany` has testing methods to test the method `most_impacted_type_of_company` in the class `Layoffs`.

#### def test_most_impacted_type_of_company_empty(self):

* This method tests the method `most_impacted_type_of_company` over an empty data file `layoffs_empty.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_type_of_company` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

#### def test_most_impacted_type_of_company_first_10(self):

* This method tests the method `most_impacted_type_of_company` over a data file `layoffs_first_10.txt` which has the first ten entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_type_of_company` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

#### def test_most_impacted_type_of_company_last_5(self):

* This method tests the method `most_impacted_type_of_company` over a data file `layoffs_last_5.txt` which has the last five entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `most_impacted_type_of_company` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

### class LayoffImpactedCity(TestCase)

The class `LayoffImpactedCity` has testing methods to test the method `impact_in_cities` in the class `Layoffs`.

#### def test_layoff_impacted_city_empty(self):

* This method tests the method `impact_in_cities` over an empty data file `layoffs_empty.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `impact_in_cities` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

#### def test_layoff_impacted_city_first_10(self):

* This method tests the method `impact_in_cities` over a data file `layoffs_first_10.txt` which has the first ten entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `impact_in_cities` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.


#### def test_layoff_impacted_city_last_5(self):

* This method tests the method `impact_in_cities` over a data file `layoffs_last_5.txt` which has the last five entries of the original dataset and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `impact_in_cities` method.
* The output will be a dictionary which will be stored in `actual_result` and it will be validated with `expected_result` using assertDictEqual statements.

**Alternative ways for getting and testing results**

* pytest can also be used for testing the results. It also supports unittest test cases execution. It has benefits like supporting built in assert statement, filtering of test cases, returning from last failing test etc.




