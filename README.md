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

'''bash
conda env create -f environment.yml
'''
Activate the environment:

'''bash
conda activate cmse802
'''

Then start JupyterLab:

'''bash
jupyter lab
'''

## **Testing and Validation**
Before running pytest, make sure the cmse802 environment is activated. Run this command from the repository root: 

'''bash
conda activate cmse802
'''

Run the tests using either command:

'''bash
python -m pytest
'''

or

'''bash
make test
'''
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



