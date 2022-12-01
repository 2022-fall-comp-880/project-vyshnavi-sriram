## COMP-880 Integrated Practicum - Fall 2022 - Project

## Design Document

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
