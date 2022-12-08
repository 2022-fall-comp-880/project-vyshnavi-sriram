## COMP-880 Integrated Practicum - Fall 2022 - Project

## Design Document
## Authors : Vyshnavi Mulakalapalli ,Sri Ram Teja Ialam

### class Layoffs:
    
    Represent a data-set of information about US companies 
    impacted due to recession.

    Concepts:
        Data processing functionality.
        Reading and writing from CSV files.

### def __init__(self, layoffs_info: list):

    Create and initialize the class attributes.

    Attributes: a list of tuples of:
        company_name: string
        industry: string
        no_of_layoffs: integer
        percentage_of_workforce_impacted: integer
        company_status: string
        headquarters: string

* Initialize `layoffs_info` using parameter `self`.

### def write(self, filename: str):
        
    Write a CSV file with US company data.

    A record is a row in the file, with six columns, corresponding to
    a company_name, industry, no_of_layoffs, percentage_of_workforce_impacted,
    company_status, headquarters.

    filename: filename to write data to

* Open a file in write 'w' mode.
* Create a 'for' loop and use company_name, industry, no_of_layoffs, percentage_of_workforce_impacted, company_status, headquarters as iterator variables to iterate over the Layoffs object 'layoffs_info'.
* Create a variable `layoffs_info_row` and assign it with the company_name, industry, no_of_layoffs, percentage_of_workforce_impacted, company_status, headquarters of company using f-string.
* Write `layoffs_info_row` into the file opened in write mode.
* Repeat the above 2 steps for all the data in `layoffs_info`.

        
### def most_impacted_industries(self) -> dict:

    Create a lookup of industries which are most impacted due to recession.
    
    Return: dictionary, with
        keys: string, each representing a name of industry.
        values: integer, representing rank of industry which indicates its 
                impact.

* Create an empty dictionary `company_dict` to store the industry names and total  number of layoffs in each industry.
* Create a **for** loop to iterate over the class object `layoffs_info`. Use `company_details` as iterator variable.
* Check if the industry name already exists in the dictionary using **if** statement.
* If the industry name does not exist, then create a key with that industry name and give the layoffs in that industry as its value.
* If the industry name already exists, then add the number of layoffs to existing value of the key with that industry name.
* Create an empty list `lst` to store the number of layoffs in each industry.
* Sort and reverse the list `lst` to the descending order sequence of values.
* Create an empty dictionary `comp_dict` to store the industry name and its rank based on its layoffs impact.
* Create a variable `rank` and assign it with 0.
* Create a **for** loop to iterate over the list `lst` with iterator variable as `num`.
* Create another **for** loop inside the above loop to iterate over the keys of `company_dict` with iterator variable as `industry`.
* Check for the key for which has its value as the first element in the list `lst` has the highest impact.
* Create a key with same name in `company_dict` and give the value as 1 which indicates rank.
* Repeat the above 2 steps for all elements in the list `lst`.
* Return `comp_dict`.

### def most_impacted_type_of_company(self) -> dict:
    
    Create a lookup of percentage impact in each type of company.

    Return: dictionary, with
        keys: string, each representing type of company(public or private).
        values: dictionary, with 
                keys representing the range of percentage of impact.
                values representing list of companies in that percentage range.

* Create a Variable company_type and initialize with empty dictionary to store 
  the output

* Create a **for** loop and iterate over self.layoffs_info for each company_data 
  we get .

* Create a **if** condition to check whether that particular company type is 
 present in dictionary or not

  * if present make company type as key and append a list of tuple where tuple 
    consists of company name,layoff percentage

  * if not present make company type as key and create a empty list .After that
   append company name ,layoff percentage as a value.

* To find the ranges of each company we should iterate over each company data 
  which is already stored a list of tuple.

* Create a for loop and iterate over dictionary company type  and make 
  company_percent as key and values will be again a nested dictionary where 
 ranges are keys and values are list of companies that fall in that range. 

* These will be determined by calling a function 
  self.determine_ranges(company_type[comp_percent]) where dictionary is a 
  parameter to that method.


### def determine_ranges(percent_of_companies: list) -> dict:

    Return the list of companies in different ranges of
    percentage_of_workforce_impacted.
    
    Parameters:
        percent_of_companies: list of tuples
        Each tuple consists of two elements - company name and 
        percentage_of_workforce_impacted for that company.
    
    Return: dictionary, with
        keys: string, representing the range of percentage of impact.
        values: representing list of companies in that percentage 
                range.

* Create an empty dictionary `percent_dict` to store the output.
* Create an empty list `lst1` to store the values of percentage impact in each company.
* Create a **for** loop to get all values of percentage impact into list `lst1`.
* Sort the list `lst1` and assign first and last elements divided by 20 to `mini` and `maxi` respectively.
* Assign the value of `mini` to `key`.
* Use a **while** loop to create the keys of dictionary `percent_dict` which are percentage ranges.
* Create a key for each value of `key` until the condition that `key` is less than `maxi` is satisfied.
* If `mini` and `maxi` are same, then create the key using **if** statement.
* Create a **for** loop to iterate over the list `percent_of_companies` to append the company names to values of corresponding keys. Use iterator variable as `percent`.
* Use a **while** loop to generate the values of dictionary `percent_dict` which are lists of companies in that ranges.
* If `mini` and `maxi` are same, then generate the value using **if** statement.
* Return `percent_dict`.

### def impact_in_cities(self) -> dict:

    Create a lookup of percentage impact in each city.

    Return: dictionary, with
        keys: string, each representing the name of city.
        values: integer, representing the percentage of impact.
 
* Create a variable impacted_city and initialize with empty dictionary to store
  the output.

* Create a variable total_layoffs and initialize with zero.

* Create a for loop and iterate over self.layoffs_info .for each company data 
  add layoffs number to the total_layoffs.

* Create a if condition and check the city is present in impact_city dictionary

  * if present add the no of layoffs to the value of that particular city(key)
  
  * else create the  city as new key and layoff number as value .
  
* After the completion of iteration we have total no of layoffs and a partial 
  dictionary is created with keys as cities and values as no of layoffs of each 
  city.

* Now we create a another for loop and iterate over keys .for each city(key) 
  we get ,calculate the layoff percentage with the respective value that each 
  key holds 
  
   * layoff% = (no of layoffs of each city / total no of layoffs) * 100

* After calculating each city layoff percentage  we assign this percentage 
  value as value to the city(key).

* After the completion of iteration we thus get the output as dictionary with 
  cities as keys and percentages as values .

* Finally return the output dictionary impact_city.


### def __str__(self):

    Create string representation of data.

### def read_dataset(filename: str) -> Layoffs:

    Read a CSV text file that holds 6-element records.

    Each line has company_name, industry, no_of_layoffs, 
    percentage_of_workforce_impacted, company_status and headquarters of US 
    companies.

* Open the `filename` in read mode and assign it to a file object `f_1`.
* Initialize a variable `lst` and assign it with an empty list.
* Use the method `readlines` on `f_1` which creates a list of strings of text in the file `filename`.
* Create a **for** loop to iterate over the above list.
* Use iterator variable `line` to get hold of each element in the list.
* Remove the `\n` in `line` and split it into list with `,`.
* Convert the second and third elements which are no_of_layoffs, percentage_of_workforce_impacted into integers.
* Convert the result from above two lines to tuple and assign it to `values`.
* Append this `values` to `lst`.
* Return `lst` as an object of `Layoffs`.
