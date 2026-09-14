# CMSE 802 Project: Crash Severity Analysis of Right-turn related Crashes at Road Intersections

## **Project Motivation**
At intersections, right-turning drivers interact with other vehicles, pedestrians, bicyclists, and roadway infrastructure. The severity of these crashes may be influenced by roadway geometry, traffic characteristics, intersection design, and operating conditions. This project aims to understand these relationships and recommend roadway intersection design characteristics to assist transportation agencies in developing appropriate safety countermeasures.

## **Research Question**
*How do roadway geometric and traffic characteristics affect the severity of right-turn-related crashes at intersections?*

## **Data**
Police recorded crash records will be combined with available roadway geometric and traffic characteristics. 

## **Analysis**
Exploratory data analysis will first be conducted to understand crash-severity distributions and relationships among candidate explanatory variables. A suitable crash-severity model will then be developed.

## **Software**
Python will be used to implement data preparation, analysis, modeling, validation and visualization. Reusable functions will be placed in the `src` directory, exploratory analyses will be performed in notebooks, and project workflows will be documented.

## **First-phase Plan**

### Phase 1: Repository and data organization (by September)
Establish the repository structure, document the project, identify relevant variables, and prepare the crash and roadway datasets.

### Phase 2: Exploratory analysis (by mid October)
Examine crash-severity distributions, missing data, roadway characteristics, traffic characteristics.

### Phase 3: Model development (by November)
Develop one or more crash-severity models and identify roadway geometric and traffic factors associated with severity.

### Phase 4: Validation and interpretation (by November)
Evaluate model performance using appropriate validation metrics and interpret the effects or importance of roadway and traffic characteristics.

### Phase 5: Documentation (by November/first week of December)
Prepare reproducible documentation, figures, results, and a final manuscript. 

## **Testing and Validation**
The computational workflow will be validated at both the software and modeling levels. Data-processing functions will include checks for expected variable types, missing values, and valid severity categories. Reusable functions developed in the `src` directory will be tested using small example datasets. Model performance will be evaluated using appropriate classification metrics. It will include accuracy, precision, recall, F1-score, confusion matrices, and cross-validation.

## **Success Metric**
The project will be considered successful if it produces a reproducible dataset-processing workflow and at least one validated crash-severity model;
