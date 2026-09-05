import pandas as pd 
import numpy as np
def generate_analysis(df):
    results = {}
    #Dataset overview
    results["total_employees"]=len(df)
    #Salary statistics
    if "Salary" in df.columns:
        results["average_salary"]=df["Salary"].mean()
        results["median_salary"]=df["Salary"].median()
        results["minimum_salary"]=df["Salary"].min()
        results["maximum_salary"]=df["Salary"].max()
    if "Team" in df.columns:
        results["employees_by_team"]=(
            df["Team"].value_counts()
        )
        if "Salary" in df.columns:
            results["Salary_by_team"]=(
                df.groupby("Team")["Salary"].mean().sort_values(ascending=False)
            )
    #gender analysis
    if "Gender" in df.columns:
        results["gender_distribution"]=(
            df["Gender"].value_counts()
        )
        #senior management
    if "Senior Management" in df.columns:
        results["management_distribution"]=(
            df["Senior Management"].value_counts()
        )
        #hiring trend
    if "Start Date" in df.columns:
        df=df.copy()
        df["Start Year"]=(
            df["Start Date"].dt.year
        )
        results["hiring_trend"]=(
            df["Start Year"].value_counts().sort_index()

        )
    return results