# Vanguard's Online Process A/B Testing Evaluation Data Analysis
## Overview
This project involves analyzing A/B testing data to assess the impact of implementing a more intuitive User Interface (UI) and timely in-context prompts on the online process for clients at Vanguard, a US-based investment management company.

## Objective
As a data analyst in the Customer Experience (CX) team, the objective was to determine whether the UI and prompts changes would lead to higher completion rates for the online process.

## Dataset
The dataset was provided by Ironhack and consists of three datasets:
- **Client Profiles (df_final_demo)**: Demographic information such as age, gender, and account details.
- **Digital Footprints (df_final_web_data)**: A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2.
- **Experiment Roster (df_final_experiment_clients)**: A list revealing which clients were part of the grand experiment.

Minimal cleaning was required for the datasets, mainly involving handling null values, duplicates, and setting datetime. Merging datasets was necessary for comprehensive data analysis, with the Footprint dataset presenting the most significant challenge.

## Initial Analysis
An initial analysis was conducted to understand the distribution of time spent between steps. Outliers were identified using statistical methods, and a threshold was established to distinguish the outliers between sessions in digital footprint analysis.

## Valid Session Criteria
Criteria were established to determine a valid session, including conditions for valid/ invalid, successful/ unsuccessful sessions.

## Hypothesis Testing
A Test of Proportions compared the completion rates between the 'Test' and 'Control' groups. The analysis did not provide sufficient evidence to reject the null hypothesis. This indicates that the 'Test' group exhibits completion rates more than 5% higher than those of the 'Control' group.

## Conclusions and Feedback
- The 'Test' group showed higher completion rates compared to the 'Control' group. Completion rates were notably higher in the 18-44 age group.
- The 'Test' group completed the online process faster but needs improvement from step 1 to step 2.
- The 'Test' group had a higher percentage of step backs and confirms compared to the 'Control' group, warranting further investigation into the reasons behind the steps back.
