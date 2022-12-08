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

* A list of tuples will be created with each tuple having industry name and total number of layoffs in that industry.
* Another list will be created with total number of layoffs in each industry and sort the list.
* Create an empty dictionary to store output.
* Use a for loop to compare the second list with the first and the industry whose total number of layoffs match with the highest number in the second list, create a key with industry and give the rank 1 as value.
* Keep repeating the above step and increment the rank each time a key is created.

### def most_impacted_type_of_company(self) -> dict:
    
    Create a lookup of percentage impact in each type of company.

    Return: dictionary, with
        keys: string, each representing type of company(public or private).
        values: dictionary, with 
                keys representing the range of percentage of impact.
                values representing list of companies in that percentage range.

* Create an empty dictionary `company_impact` to store the output.
* Use a for loop to create the keys of dictionary based on dataset representing type of company like public or private.
* Use another for loop to specify the ranges in each key.
* Use another for loop to get the list of companies fall in that range.

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
* Convert the result from above line to tuple and assign it to `values`.
* Append this `values` to `lst`.
* Return `lst` as an object of `Layoffs`.
