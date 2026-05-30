import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Titanic Analytics & Survival Intelligence Dashboard",
    page_icon="🚢",
    layout="wide"
)

st.markdown("""
<style>
.main {padding-top: 1rem;}
[data-testid="stMetricValue"] {font-size: 2rem;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = sns.load_dataset("titanic")
    df["age"] = df["age"].fillna(df["age"].median())
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df["fare"] = df["fare"].fillna(df["fare"].median())
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    return df

df = load_data()

st.sidebar.title("Dashboard Filters")

gender = st.sidebar.multiselect(
    "Gender", df["sex"].unique(), default=df["sex"].unique()
)

pclass = st.sidebar.multiselect(
    "Passenger Class",
    sorted(df["pclass"].unique()),
    default=sorted(df["pclass"].unique())
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df.age.min()),
    int(df.age.max()),
    (int(df.age.min()), int(df.age.max()))
)

filtered = df[
    (df["sex"].isin(gender))
    & (df["pclass"].isin(pclass))
    & (df["age"].between(age_range[0], age_range[1]))
]

st.title("🚢 Titanic Analytics & Survival Intelligence Dashboard")
st.caption("Presentation-Level Data Science Portfolio Project")

total = len(filtered)
survived = int(filtered["survived"].sum())
rate = round(filtered["survived"].mean()*100,2)
avg_age = round(filtered["age"].mean(),1)

c1,c2,c3,c4 = st.columns(4)
c1.metric("Passengers", total)
c2.metric("Survivors", survived)
c3.metric("Survival Rate", f"{rate}%")
c4.metric("Average Age", avg_age)

tab1,tab2,tab3,tab4 = st.tabs(
    ["Executive Dashboard","Analytics","AI Insights","Prediction"]
)

with tab1:
    col1,col2 = st.columns(2)

    fig1 = px.pie(
        filtered,
        names="survived",
        title="Survival Distribution"
    )
    col1.plotly_chart(fig1, use_container_width=True)

    fig2 = px.histogram(
        filtered,
        x="age",
        color="survived",
        title="Age Distribution"
    )
    col2.plotly_chart(fig2, use_container_width=True)

    fig3 = px.bar(
        filtered.groupby("sex")["survived"].mean().reset_index(),
        x="sex",
        y="survived",
        title="Survival Rate by Gender"
    )
    st.plotly_chart(fig3, use_container_width=True)

with tab2:

    col1,col2 = st.columns(2)

    fig4 = px.bar(
        filtered.groupby("pclass")["survived"].mean().reset_index(),
        x="pclass",
        y="survived",
        title="Survival Rate by Class"
    )
    col1.plotly_chart(fig4, use_container_width=True)

    fig5 = px.box(
        filtered,
        x="survived",
        y="fare",
        title="Fare vs Survival"
    )
    col2.plotly_chart(fig5, use_container_width=True)

    st.subheader("Dataset Explorer")
    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode()
    st.download_button(
        "Download Filtered Data",
        csv,
        "titanic_filtered.csv",
        "text/csv"
    )

with tab3:

    female_rate = round(
        df[df.sex=="female"]["survived"].mean()*100,2
    )
    male_rate = round(
        df[df.sex=="male"]["survived"].mean()*100,2
    )

    first_rate = round(
        df[df.pclass==1]["survived"].mean()*100,2
    )
    third_rate = round(
        df[df.pclass==3]["survived"].mean()*100,2
    )

    st.success(
        f"Female passengers had a survival rate of {female_rate}% compared to {male_rate}% for males."
    )

    st.info(
        f"First-class passengers survived at {first_rate}% versus {third_rate}% in third class."
    )

    st.warning(
        "Passenger class and gender were the strongest indicators of survival."
    )

with tab4:

    st.subheader("Passenger Survival Predictor")

    model_df = df[["survived","pclass","sex","age","fare","family_size"]].copy()
    model_df["sex"] = model_df["sex"].map({"male":0,"female":1})

    X = model_df.drop("survived", axis=1)
    y = model_df["survived"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train,y_train)

    pclass_input = st.selectbox("Class",[1,2,3])
    sex_input = st.selectbox("Gender",["male","female"])
    age_input = st.slider("Age",1,80,30)
    fare_input = st.slider("Fare",0.0,600.0,50.0)
    family_input = st.slider("Family Size",1,10,2)

    if st.button("Predict Survival"):
        sample = pd.DataFrame({
            "pclass":[pclass_input],
            "sex":[1 if sex_input=="female" else 0],
            "age":[age_input],
            "fare":[fare_input],
            "family_size":[family_input]
        })

        prob = model.predict_proba(sample)[0][1]*100
        pred = model.predict(sample)[0]

        st.metric("Survival Probability", f"{prob:.2f}%")

        if pred == 1:
            st.success("Prediction: Survived")
        else:
            st.error("Prediction: Did Not Survive")
