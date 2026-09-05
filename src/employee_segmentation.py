import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
def employee_segmentation():
    #load data
    df=pd.read_csv("data/processed/cleaned_employess.csv")
    #convert Start Date
    df["Start Date"]=pd.to_datetime(df["Start Date"])
    #calculate experience
    current_date=pd.Timestamp("2026-08-29")
    df["Experience"]=((current_date-df["Start Date"]).dt.days/365.25)
    #select features
    X=df[["Salary","Bonus %","Experience"]]
    #scaling 
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)
    #Elbow Method
    inertia=[]
    for k in range(2,9):
        kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)
    #plot elbow curve
    plt.figure(figsize=(8,5))
    plt.plot(range(2,9),inertia,marker="o")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for Employee segmentation")
    plt.tight_layout()
    plt.savefig("outputs/figures/elbow_curve.png")
  
    plt.close()
    #final Kmeans
    kmeans=KMeans(n_clusters=4,random_state=42,n_init=10)
    df["Cluster"]=kmeans.fit_predict(X_scaled)
    cluster_names={
        0: "High Bonus -Lower Salary",
        1: "Experienced High Earners",
        2: "Experienced Lower Earners",
        3: "High Earners - Lower Experience"
    }
    df["segment"]=df["Cluster"].map(cluster_names)
    #cluster summary
    summary=df.groupby("Cluster")[["Salary","Bonus %","Experience"]].mean()
    
    print("\n ---Employee Cluster Summary---")
    print(summary)
    #cluster visualization
    plt.figure(figsize=(8,6))
    plt.scatter(df["Experience"],df["Salary"],c=df["Cluster"])
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Employee Segmentation")
    plt.tight_layout()
    plt.savefig("outputs/figures/employee_clusters.png")
    plt.close()
   
 
   
    #save segmented data
    df.to_csv("data/processed/segmented_employees.csv",index=False)
    print("\n Segmented employee data saved successfully!")
    return df, summary
if __name__=="__main__":
    employee_segmentation()
