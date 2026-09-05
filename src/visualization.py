import matplotlib.pyplot as plt 
import seaborn as sns
import os
def create_output_folder():
    os.makedirs("outputs/figures",exist_ok=True)
def salary_distribution(df):
    plt.figure(figsize=(10,6))
    sns.histplot(df["Salary"],kde=True)
    plt.title("Employee Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig("outputs/figures/salary_distribution.png",dpi=300)
    plt.close()
def employees_by_team(df):
    team_counts=(df["Team"].value_counts().sort_values(ascending=True))
    plt.figure(figsize=(10,7))
    team_counts.plot(kind="barh")
    plt.title("Employees by Team")
    plt.xlabel("Number of Employees")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.savefig("outputs/figures/employees_by_team.png",dpi=300)
    plt.close()
def salary_by_team(df):
    salary=(df.groupby("Team")["Salary"].mean().sort_values(ascending=True))
    plt.figure(figsize=(10,7))
    salary.plot(kind="barh")
    plt.title("Average Salary by Team")
    plt.xlabel("Average Salary")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.savefig("outputs/figures/salary_by_team.png",dpi=300)
    plt.close()
def hiring_trend(df):
    temp=df.copy()
    temp["Start Year"]=(temp["Start Date"].dt.year)
    hiring=(
        temp["Start Year"].value_counts().sort_index()

        )
    plt.figure(figsize=(10,6))
    hiring.plot(kind="line",marker="o")
    plt.title("employee Hiring Trend")
    plt.xlabel("Year")
    plt.ylabel("Employees Hired")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/figures/hiring_trend.png",dpi=300)
    plt.close()
def bonus_distribution(df):
    plt.figure(figsize=(10,6))
    sns.histplot(df["Bonus %"],kde=True)
    plt.title("Bonus Percentage Distribution")
    plt.xlabel("Bonus %")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig("outputs/figures/bonus_distribution.png",dpi=300)
    plt.close()