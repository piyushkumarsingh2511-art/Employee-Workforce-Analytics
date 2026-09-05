import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
def train_ucop_salary_model():
    #Load cleaned data
    df=pd.read_csv("UCOP_Data_2010.csv")
   
    print("\n ---ucop dataset---")
    print("Rows:",len(df))
    print("Columns:",df.columns.tolist())
    #convert gross pay to numeric
    df["gross pay"]=pd.to_numeric(df["gross pay"],errors="coerce")
    #remove missing target values
    df=df.dropna(subset=["gross pay"])
    #remove negative salary
    df=df[df["gross pay"]>=0]
    #remove missing categorical values
    df["location"]=df["location"].fillna("Unknown")
    df["title"]=df["title"].fillna("Unknown")
    #Feature Engineering
   
    #select Features
    X=df[
      [
          "year",
          "location",
          "title"
      ]
    ]
    #target
    y=df["gross pay"]
    #categorical columns
    categorical_features=[
        "location",
        "title",
    ]
    #Numerical columns
    numerical_features=[
        "year"
    ]
    #Preprocessing
    preprocessor=ColumnTransformer(
        transformers=[
            ("categorical",OneHotEncoder(handle_unknown="ignore"),
             categorical_features),
             ("numerical","passthrough",numerical_features)
        ]
    )
   
    #train-test split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    #model we use it
    models={"Linear Regression":LinearRegression()
            
            
    }
    print("\n---Salary Prediction Model Comparison---")
    results=[]
    trained_models={}
    for name, model in models.items():
        #pipeline
        pipeline=Pipeline(steps=[("preprocessor", preprocessor),("model", model)])
    #train
        pipeline.fit(X_train, y_train)
    #Predict
        y_pred=pipeline.predict(X_test)
    #Evaluation
        mae=mean_absolute_error(y_test,y_pred)
        mse=mean_squared_error(y_test, y_pred)
        rmse=np.sqrt(mse)
        r2=r2_score(y_test,y_pred)
        trained_models[name]=pipeline
        results.append({"Model":name,"Mean_absolute_error":mae,"Mean_square_error":mse,"Root Mean Square Error":rmse,"R2":r2})
        print(f"\n{name}")
        print(f"MEAN_ABSOLUTE_ERROR : {mae:.2f}")
        print(f"MEAN_SQUARE_ERROR  : {mse:.2f}")
        print(f"ROOT MEAN SQUARE ERROR : {rmse:.2f}")
        print(f"R2   : {r2:.4f}")
    #comparison table
    results_df=pd.DataFrame(results)
    print("\n---model comparison---")
    print(results_df.to_string(index=False))
    best_model_name=(results_df.sort_values(by="R2",ascending=False).iloc[0]["Model"])
    best_model=trained_models[best_model_name]
    
    print(f"\nBest Model: {best_model_name}")
    joblib.dump(best_model, "salary_model.pkl")
    print("\n Salary model saved successfully!")
    return best_model,results_df
 
if __name__=="__main__":
    train_ucop_salary_model()
    
