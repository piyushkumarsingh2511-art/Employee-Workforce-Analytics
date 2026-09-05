import pandas as pd
import numpy as np
def load_data(file_path):
    df=pd.read_csv(file_path)
  
    print("=" * 60)

    print("DATASET LOADED")
    print("=" * 60)

    print(f"Rows : {df.shape[0]}")
    print(f"Columns :{df.shape[1]}")
    
    return(df)


#data cleaning
def clean_data(df):
    df=df.copy()
    #standardize column names
    df.columns=df.columns.str.strip()
    #replace infinite values
    df.replace([np.inf,-np.inf], np.nan, inplace=True)
    #convert Salary and bonus to numeric 
    if "Salary" in df.columns:
        df["Salary"]=pd.to_numeric(df["Salary"], errors="coerce")
    if "Bonus %" in df.columns:
        df["Bonus %"]=pd.to_numeric(df["Bonus %"], errors="coerce")
    #handles invalid negative salaries
    if "Salary" in df.columns:
        df.loc[df["Salary"]<0,"Salary"]=np.nan
        salary_median=df["Salary"].median()
        df["Salary"]=df["Salary"].fillna(salary_median)
    #handle Bonus %
    if "Bonus %" in df.columns:
        df.loc[df["Bonus %"]<0,"Bonus %"]=np.nan
        bonus_median=df["Bonus %"].median()
        df["Bonus %"]=df["Bonus %"].fillna(bonus_median)

    # Remove duplicate records
    before=len(df)
    df.drop_duplicates(inplace=True)
    after =len(df)
    print(f"Duplicates removed: {before - after}")
    #handle categorical columns
    categorical_columns=[
        "First Name",
        "Gender",
        "Senior Management",
        "Team"
    ]
    for column in categorical_columns:
        if column in df.columns:
            if df[column].isnull().any():
                mode_value=df[column].mode()
                if not mode_value.empty:
                    df[column]=df[column].fillna(mode_value.iloc[0])

# convert start date
    if "Start Date" in df.columns:
        df["Start Date"]=pd.to_datetime(
            df["Start Date"],
            errors="coerce"
        )
        median_date=df["Start Date"].median()
        df["Start Date"]=df["Start Date"].fillna(median_date)
        #salary outlier removal using IQR
    if "Salary" in df.columns:
        Q1=df["Salary"].quantile(0.25)
        Q3=df["Salary"].quantile(0.75)
        IQR= Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        df=df[
            (df["Salary"]>=lower_bound) &
            (df["Salary"]<=upper_bound)
        ]
#Reset index
    df.reset_index(drop=True,inplace=True)
    return df
def validate_data(df):
    print("\n" + "=" *60)
    print("Final Data validation")
    print("=" * 60)
    print("\nShape:")
    print(df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    print(df.duplicated().sum())
    print("\nDate types:")
    print(df.dtypes)
    return df
