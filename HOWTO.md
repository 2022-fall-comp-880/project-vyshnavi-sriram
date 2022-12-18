## HOWTO

### Clone the project:

* Clone the project into your local machine using the github URL: `https://github.com/2022-fall-comp-880/project-vyshnavi-sriram.git`

### Setting-up virtual environment:

* Open the project folder in PyCharm after cloning in local machine.
* In the status bar (at the bottom of the IDE window), click Python 3.10 and select Interpreter Settings.
* Select Virtualenv Environment
* Check off New environment
* Location should be the path to your project folder
  * If the location is different, change it. 
  * Base interpreter should be Python 3.10 you have installed at the system level.
* Now you can now see the .venv folder with Lib,Scripts sub folders in it under our project in our file structure.

### Import libraries:

* Import the libraries `os` and `unittest` as below:
```angular2html
import os
import unittest
```

### Run the program:

* Run the whole program using the command `python -m apps.main` from terminal.

### Run the tests:

* Run the tests for method `most_impacted_industries` using `python -m tests.test_most_impacted_industries`
* Run the tests for method `most_impacted_type_of_company` using `python -m tests.test_most_impacted_type_of_company`
* Run the tests for method `impact_in_cities` using `python -m tests.test_impact_in_cities`
