import os
from src.cleaning import (load_data,clean_data,validate_data

)
from src.analysis import generate_analysis
from src.visualization import (
    create_output_folder,salary_distribution,employees_by_team,salary_by_team,hiring_trend,bonus_distribution
)
def main():
    #load data
    df=load_data("employees(1).csv")
    #initial information
    print("\nInitial dataset:")
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())
    #clean data
    df_clean=clean_data(df)
    #validate
    validate_data(df_clean)
    #save cleaned dataset
    os.makedirs("data/processed", exist_ok=True)
    df_clean.to_csv("data/processed/cleaned_employess.csv",index=False)
    print("\nCleaned dataset saved successfully!")
    #generate analysis
    results=generate_analysis(df_clean)
    print("\n"+"="*60)
    print("Key insights")
    print("="*60)
    print("Total employees:",results["total_employees"])
    if "average_salary" in results:
        print(
            "average salary:",
            round(
                results["average_salary"],2
            )
        )
        print(
            "Median salary:",
            round(
                results["median_salary"],
                2)
        )
        print(
            "Minimun salary:",
            round(
                results["minimum_salary"],
                2
            )
        )
        print(
            "Maximum salary:",
            round(
                results["maximum_salary"],
                2
            )
        )
    create_output_folder()
    salary_distribution(df_clean)
    employees_by_team(df_clean)
    salary_by_team(df_clean)
    hiring_trend(df_clean)
    bonus_distribution(df_clean)
    print("\nAll visualizations generated successfully!")
if __name__=="__main__":
    main()