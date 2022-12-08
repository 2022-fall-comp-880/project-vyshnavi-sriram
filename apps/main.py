"""
Represent a data-set of information about US companies
impacted due to recession.

Authors:
  - https://github.com/VyshnaviMulakalapalli
  - https://github.com/si1051
"""
class Layoffs:
    """
    Represent a data-set of information about US companies
    impacted due to recession.

    Concepts:
        Data processing functionality.
        Reading and writing from CSV files.
    """

    def __init__(self, layoffs_info: list):
        """
        Create and initialize the class attributes.

        Attributes: a list of tuples of:
            company_name: string
            industry: string
            no_of_layoffs: integer
            percentage_of_workforce_impacted: integer
            company_status: string
            headquarters: string
        """
        self.layoffs_info = layoffs_info

    def write(self, filename: str):
        """
        Write a CSV file with US company data.

        A record is a row in the file, with six columns, corresponding to
        a company_name, industry, no_of_layoffs,
        percentage_of_workforce_impacted,
        company_status, headquarters.

        filename: filename to write data to
        """

    def most_impacted_industries(self) -> dict:
        """
        Create a lookup of industries which are most impacted due to recession.

        Return: dictionary, with
            keys: string, each representing a name of industry.
            values: integer, representing rank of industry which indicates its
                    impact.
        """
        company_dict = {}
        for company_details in self.layoffs_info:
            if company_details[3] in company_dict:
                company_dict[company_details[3]] = \
                    company_dict[company_details[3]] + company_details[1]
            else:
                company_dict[company_details[3]] = company_details[1]

        lst = []
        for number_of_layoffs in company_dict.values():
            lst.append(number_of_layoffs)
        lst.sort()
        lst.reverse()
        comp_dict = {}
        rank = 0
        for num in lst:
            for industry in company_dict:
                if company_dict[industry] == num:
                    comp_dict[industry] = rank + 1
            rank = rank + 1
        return comp_dict

    def most_impacted_type_of_company(self) -> dict:
        """
        Create a lookup of percentage impact in each type of company.

        Return: dictionary, with
            keys: string, each representing type of company(public or private).
            values: dictionary, with
                keys representing the range of percentage of impact.
                values representing list of companies in that percentage range.
        """

    def impact_in_cities(self) -> dict:
        """
        Create a lookup of percentage impact in each city.

        Return: dictionary, with
            keys: string, each representing name of city.
            values: integer, representing the percentage of impact.
        """

    def __str__(self):
        """Create string representation of data."""


@staticmethod
def read_dataset(filename: str) -> Layoffs:
    """
    Read a CSV text file that holds 6-element records.

    Each line has company_name, industry, no_of_layoffs,
    percentage_of_workforce_impacted, company_status and headquarters of US
    companies.
    """


def main():
    """Run read_dataset."""


if __name__ == '__main__':
    main()
