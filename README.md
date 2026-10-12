# CMSE 802 Project: Crash Severity Analysis of Right-turn related Crashes at Road Intersections

## **Project Description**
The project aim to analyze how roadway geometric and traffic characteristics are associated with the severity of right-turn related crashes at roadway intersections.

## **Project Objectives**
- Develop machine-learning model to understand the effect of different roadway factors on right-turning vehicles' crash severity.
- Analyze roadway geometric and traffic relationships with right-turn crash severity at intersections using computational models. 
- Provide recommendation on roadway intersection design to reduce crash severities. 

## **Project Workflow**
- Data preparation and cleaning
- Exploratory data analysis
- Model development and validation
- Results interpretation and recommendation development 

## **Installation and Setup**
The project environment is defined in environment.yml.

Create the Conda environment from the repository root:

conda env create -f environment.yml

Activate the environment:

conda activate cmse802

Then start JupyterLab:

jupyter lab

## **Testing and Validation**
Before running pytest, make sure the cmse802 environment is activated. Run this command from the repository root: 

conda activate cmse802

Run the tests using either command:

python -m pytes

or

make test

Expected result: 9 tests passed. 

## Milestone 1
The initial project repository has been established.

## Milestone 2

The "01_initial_prototype" notebook will show an initial workflow to describe the variables in the crash severity analysis. The main outcomes are- 
1. Loads a CSV database that contains the variables regarding roadway geometric and traffic characteristics of intersections and crash severity outcomes.  
2. Creates a bar chart showing how many right-turning crashes fall into each crash severity category.
3. Shows the variable categories for "speed limit" of roadways.
4. Creates a bar chart showing the crash severity outcomes by roadway speed limit.

## Milestone 3 

The "02_testing_validation" notebook will show some automated tests implemented in "test_validation" python file. The tests evaluate data validation and processing functions, including: 
1. Verification of required dataset columns
2. Retention of valid observations and exclusion of invalid observations.
3. Removal of unnecessary whitespace.
4. Calculation of crash severity frequencies.
5. Generation of cross-tabulations and summary totals.
6. Handling of datasets with no valid observations.

### Run automated tests 
From the repository root directory, activate the Conda environment and run:

conda activate cmse802
make test

The Makefile disables automatic loading of third-party pytest plugins to avoid an environment-specific plugin compatibility issue.

Alternatively, on Windows Anaconda Prompt, run:

set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python -m pytest -v test_validation.py

### Run validation checks
make check

This command executes the automated tests and checks that test_validation.py compiles successfully.

### View Available Make Commands
make help

Expected result: 9 tests passed. 

### Limitations: 
The current makefile uses Windows Command Prompt syntax to disable automatic pytest plugin loading. Users on other operating systems may need to adjust this command.
