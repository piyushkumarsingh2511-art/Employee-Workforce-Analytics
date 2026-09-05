import streamlit as st
import pandas as pd
import joblib
from src.analysis import generate_analysis
from src.visualization import (
    salary_distribution,
    employees_by_team,
    salary_by_team,
    hiring_trend,
    bonus_distribution
)

st.set_page_config(
    page_title="Employee Workforce Analytics",
    page_icon="💼",
    layout="wide"
)
st.sidebar.title("💼 Workforce Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Overview",
        "📊 Employee Analysis",
        "📈 Employee Visualizations",
        "👥 Employee Segmentation",
        "💰 Salary Prediction",
        "📊 UCOP Salary Analysis",
        "📋 Dataset Preview"
    ]
)

# Existing processed files
employee_df = pd.read_csv(
    "data/processed/cleaned_employess.csv"
)

employee_df["Start Date"] = pd.to_datetime(
    employee_df["Start Date"],
    errors="coerce"
)

segmented_df = pd.read_csv(
    "data/processed/segmented_employees.csv"
)

ucop_df = pd.read_csv(
    "data/processed/cleaned_UCOP_Data_2010.csv"
)

# Existing trained model
salary_model = joblib.load(
    "salary_model.pkl"
) 
results = generate_analysis(employee_df)
if page == "🏠 Overview":

    st.title("💼 Employee Workforce Analytics")
    st.caption(
        "Workforce insights, salary intelligence & employee segmentation"
    )

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Total Employees",
            f"{results['total_employees']:,}"
        )

    with col2:
        st.metric(
            "💰 Average Salary",
            f"${results['average_salary']:,.0f}"
        )

    with col3:
        st.metric(
            "📊 Median Salary",
            f"${results['median_salary']:,.0f}"
        )

    with col4:
        st.metric(
            "💵 Maximum Salary",
            f"${results['maximum_salary']:,.0f}"
        )

    st.divider()

    # Dataset Overview
    st.subheader("📂 Project Data Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            f"**Employee Dataset**\n\n"
            f"{employee_df.shape[0]:,} records"
        )

    with col2:
        st.info(
            f"**Segmented Employees**\n\n"
            f"{segmented_df.shape[0]:,} records"
        )

    with col3:
        st.info(
            f"**UCOP Payroll Dataset**\n\n"
            f"{ucop_df.shape[0]:,} records"
        )

    st.divider()

    # Quick Insights
    st.subheader("📌 Quick Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🏢 Largest Team")

        largest_team = results["employees_by_team"].idxmax()
        largest_team_count = results["employees_by_team"].max()

        st.success(
            f"{largest_team} — {largest_team_count:,} employees"
        )

    with col2:
        st.write("### 💰 Highest Average Salary Team")

        highest_salary_team = results["Salary_by_team"].idxmax()
        highest_salary = results["Salary_by_team"].max()

        st.success(
            f"{highest_salary_team} — ${highest_salary:,.0f}"
        )
        st.divider()

    st.subheader("📈 Workforce Snapshot")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "outputs/figures/salary_distribution.png",
            # caption="Employee Salary Distribution",
            use_container_width=True
        )

    with col2:
        st.image(
            "outputs/figures/employees_by_team.png",
            # caption="Employees by Team",
            use_container_width=True
        )

# results = generate_analysis(employee_df)
elif page =="📊 Employee Analysis":
    st.subheader("📊 Employee Analysis")

    st.write("Total Employees:", results["total_employees"])
    st.write("Average Salary:", results["average_salary"])
    st.write("Median Salary:", results["median_salary"])
    st.write("Minimum Salary:", results["minimum_salary"])
    st.write("Maximum Salary:", results["maximum_salary"])
# st.divider()
elif page == "📈 Employee Visualizations":
    st.subheader("📈 Employee Visualizations")

    st.image(
        "outputs/figures/salary_distribution.png",
        caption="Employee Salary Distribution"
    )

    st.image(
        "outputs/figures/employees_by_team.png",
        caption="Employees by Team" 
    )

    st.image(
        "outputs/figures/salary_by_team.png",
        caption="Average Salary by Team"
    )

    st.image(
        "outputs/figures/hiring_trend.png",
        caption="Employee Hiring Trend"
    )

    st.image(
        "outputs/figures/bonus_distribution.png",
        caption="Bonus Distribution"
    )
# st.divider()

elif page == "👥 Employee Segmentation":
    st.subheader("👥 Employee Segmentation")

    st.write("KMeans segmentation from existing employee_segmentation.py")

    st.dataframe(
        segmented_df[
            ["Salary", "Bonus %", "Experience", "Cluster", "segment"]
        ],
        use_container_width=True
    )

    st.subheader("Employees per Segment")

    segment_count = segmented_df["segment"].value_counts()

    st.bar_chart(segment_count)
    st.divider()
elif page == "💰 Salary Prediction":
    st.subheader("💰 Salary Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        year = st.selectbox(
            "Year",
            sorted(ucop_df["year"].dropna().unique())
        )

    with col2:
        location = st.selectbox(
            "Location",
            sorted(ucop_df["location"].dropna().unique())
        )

    with col3:
        title = st.selectbox(
            "Job Title",
            sorted(ucop_df["title"].dropna().unique())
        )

    if st.button("🔮 Predict Salary"):

        input_data = pd.DataFrame({
            "year": [year],
            "location": [location],
            "title": [title]
        })

        prediction = salary_model.predict(input_data)[0]

        st.success(
            f"Predicted Gross Pay: ${prediction:,.2f}"
        )
        st.divider()
elif page == "📊 UCOP Salary Analysis":
    st.subheader("📊 UCOP Salary Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Gross Pay",
            f"${ucop_df['gross pay'].mean():,.2f}"
        )

    with col2:
        st.metric(
            "Median Gross Pay",
            f"${ucop_df['gross pay'].median():,.2f}"
        )

    with col3:
        st.metric(
            "Average Regular Pay",
            f"${ucop_df['regular pay'].mean():,.2f}"
        )

    with col4:
        st.metric(
            "Average Overtime Pay",
            f"${ucop_df['overtime pay'].mean():,.2f}"
        ) 
    st.subheader("📈 UCOP Salary Visualizations")

    st.image(
        "outputs/figures/ucop_salary_distribution.png",
        caption="UCOP Gross Pay Distribution"
    )

    st.image(
        "outputs/figures/ucop_salary_by_location.png",
        caption="Average Gross Pay by UC Location"
    )
elif page == "📋 Dataset Preview":
    st.subheader("📋 Dataset Preview")

    st.write("### Employee Dataset")
    st.dataframe(
        employee_df.head(20),
        use_container_width=True
    )

    st.write("### Segmented Employee Dataset")
    st.dataframe(
        segmented_df.head(20),
        use_container_width=True
    )

    st.write("### UCOP Dataset")
    st.dataframe(
        ucop_df.head(20),
        use_container_width=True
    )