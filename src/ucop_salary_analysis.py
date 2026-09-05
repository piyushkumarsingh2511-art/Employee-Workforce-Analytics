import pandas as pd
import matplotlib.pyplot as plt
import joblib

def ucop_salary_analysis():

    # Load UC public employee wage data
    df = pd.read_csv("UCOP_Data_2010.csv")

    print("\n--- Dataset Information ---")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\nColumns:")
    print(df.columns.tolist())

    # Convert pay columns to numeric
    pay_columns = [
        "gross pay",
        "regular pay",
        "overtime pay",
        "other pay"
    ]

    for col in pay_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove records without gross pay
    df = df.dropna(subset=["gross pay"])

    # Remove negative gross pay
    df = df[df["gross pay"] >= 0]

    # Missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Basic salary statistics
    print("\n--- Gross Pay Statistics ---")
    print(df["gross pay"].describe())

    # Top job titles by average gross pay
    title_salary = (
        df.groupby("title")["gross pay"]
        .agg(["count", "mean", "median"])
        .sort_values("mean", ascending=False)
    )

    print("\n--- Top 15 Job Titles by Average Gross Pay ---")
    print(title_salary.head(15))

    # Location-wise salary
    location_salary = (
        df.groupby("location")["gross pay"]
        .agg(["count", "mean", "median"])
        .sort_values("mean", ascending=False)
    )

    print("\n--- Salary by Location ---")
    print(location_salary)

    # Pay component analysis
    pay_summary = df[
        ["gross pay", "regular pay", "overtime pay", "other pay"]
    ].mean()

    print("\n--- Average Pay Components ---")
    print(pay_summary)

    # Save cleaned UC data
    df.to_csv(
        "data/processed/cleaned_UCOP_Data_2010.csv",
        index=False
    )

    print(
        "\nCleaned UCOP data saved successfully!"
    )

    # -----------------------------
    # Visualization 1: Salary Distribution
    # -----------------------------

    plt.figure(figsize=(9, 5))

    plt.hist(
        df["gross pay"],
        bins=50
    )

    plt.xlabel("Gross Pay")
    plt.ylabel("Number of Employees")
    plt.title("UC Employee Gross Pay Distribution")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/ucop_salary_distribution.png"
    )

    plt.close()

    # -----------------------------
    # Visualization 2: Location Salary
    # -----------------------------

    location_plot = (
        df.groupby("location")["gross pay"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))

    location_plot.plot(kind="barh")

    plt.xlabel("Average Gross Pay")
    plt.ylabel("Location")
    plt.title("Average Gross Pay by UC Location")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/ucop_salary_by_location.png"
    )

    plt.close()

    print(
        "\nUCOP salary visualizations saved successfully!"
    )
    return {"data": df,"title_salary": title_salary,"location_salary": location_salary,"pay_summery": pay_summary}

if __name__ == "__main__":
    ucop_salary_analysis()