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
        with open(filename, 'w', encoding='utf8') as layoffs_file_obj:
            for company, num_layoffs, percent_layoffs, industry, city, status \
                 in self.layoffs_info:
                company_info_row = f'{company},{num_layoffs},' \
                                   f'{percent_layoffs},{industry},' \
                                   f'{city},{status}\n'
                layoffs_file_obj.write(company_info_row)

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
                    int(company_dict[company_details[3]]) + int(company_details[1])
            else:
                company_dict[company_details[3]] = int(company_details[1])

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
        company_type = {}
        for company_details in self.layoffs_info:
            if company_details[5] in company_type:
                company_type[company_details[5]].append((company_details[0],
                                                        int(company_details[2])
                                                         ))

            else:
                company_type[company_details[5]] = []
                company_type[company_details[5]].append((company_details[0],
                                                         int(company_details[2]
                                                             )))

        for comp_percent in company_type:
            company_type[comp_percent] = \
                self.determine_ranges(company_type[comp_percent])
        return company_type

    @staticmethod
    def determine_ranges(percent_of_companies: list) -> dict:
        """
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
        """
        percent_dict = {}
        lst1 = []
        for percent in percent_of_companies:
            lst1.append(percent[1])
        lst1.sort()
        mini = lst1[0] // 20
        maxi = lst1[len(lst1) - 1] // 20
        key = mini

        while key < maxi:
            key1 = "{} - {} %".format(key * 20, (key + 1) * 20)
            percent_dict[key1] = []
            key = key + 1

        if mini == maxi:
            key1 = "{} - {} %".format(key * 20, (key + 1) * 20)
            percent_dict[key1] = []

        for percent in percent_of_companies:
            val = mini
            while val < maxi:
                i = percent[1]
                if (i >= val * 20) and (i <= (val + 1) * 20):
                    val1 = "{} - {} %".format(val * 20, (val + 1) * 20)
                    percent_dict[val1].append(percent[0])
                    break
                else:
                    val = val + 1

            if mini == maxi:
                val1 = "{} - {} %".format(val * 20, (val + 1) * 20)
                percent_dict[val1].append(percent[0])

        return percent_dict

    def impact_in_cities(self) -> dict:
        """
        Create a lookup of percentage impact in each city.

        Return: dictionary, with
            keys: string, each representing name of city.
            values: integer, representing the percentage of impact.
        """
        impacted_city = {}
        total_layoffs = 0
        for company_details in self.layoffs_info:
            total_layoffs = total_layoffs + int(company_details[1])
            if company_details[4] not in impacted_city:
                impacted_city[company_details[4]] = int(company_details[1])
            else:
                impacted_city[company_details[4]] = impacted_city[
                                                          company_details[4]] \
                                                      + int(company_details[1])

        for city_layoffs in impacted_city.keys():
            percentage = (
                (impacted_city[city_layoffs] * 100) / total_layoffs)
            percentage = round(percentage, 2)
            layoff_percent = str(percentage)
            layoff_percent = layoff_percent + ' %'
            impacted_city[city_layoffs] = layoff_percent
            percentage = 0
        return impacted_city

    def __str__(self):
        """Create string representation of data."""
        return str(self.layoffs_info)


@staticmethod
def read_dataset(filename: str) -> Layoffs:
    """
    Read a text file that holds 6-element records.

    Each line has company_name, industry, no_of_layoffs,
    percentage_of_workforce_impacted, company_status and headquarters of US
    companies.
    """
    f_1 = open(filename, 'r')
    lst = []
    for line in f_1.readlines():
        values = line.rstrip('\n').split(',')
        lst.append(tuple(values))
    f_1.close()

    return Layoffs(lst)


def main():
    """Run read_dataset."""
    input_file = "../data/layoffs_first_10.txt"
    layoffs = read_dataset(input_file)
    print(layoffs)


if __name__ == '__main__':
    main()
