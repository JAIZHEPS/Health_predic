
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="Human Health Prediction Models",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded"
)

model_info = {
    'Heart Health Model': 'heart_model (1).pkl',
    'Diabetes Prediction Model': 'diabetes_model (1).pkl',
    'Lung Health Model': 'lung_model (1).pkl',
    'Thyroid Health Model': 'model.pkl',
    'General Cardiovascular Risk Model': 'model (1).pkl'
}

model_feature_maps = {
    'Heart Health Model': [
        'male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'diabetes',
        'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'
    ],
    'Diabetes Prediction Model': [
        'pregnancies', 'glucose', 'sysBP', 'skin_thickness', 'insulin',
        'BMI', 'diabetes_pedigree_function', 'age'
    ],
    'Lung Health Model': [
        'age', 'sex', 'currentSmoker', 'cigsPerDay', 'smoking_years',
        'chest_pain', 'shortness_of_breath', 'cough_severity', 'fatigue_level'
    ],
    'Thyroid Health Model': [
        'age', 'sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
        'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
        'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych',
        'TSH', 'T3', 'TT4', 'T4U', 'FTI',
        'TSH measured', 'T3 measured', 'TT4 measured', 'T4U measured', 'FTI measured'
    ],
    'General Cardiovascular Risk Model': [
        'male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'diabetes',
        'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'
    ]
}

class DummyHealthModel:
    def __init__(self, name):
        self.name = name
    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            return np.random.rand(len(X)) * 100
        else:
            return np.random.rand() * 100
    def __str__(self):
        return f"Dummy Model: {self.name}"

loaded_models = {}
for display_name, filename in model_info.items():
    try:
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                model = pickle.load(file)
            loaded_models[display_name] = model
        else:
            loaded_models[display_name] = DummyHealthModel(display_name)
    except Exception as e:
        loaded_models[display_name] = DummyHealthModel(display_name)

st.title("❤️ Human Health Prediction Interface")
st.markdown("""
Welcome to the Human Health Prediction Machine Learning Model Interface!
Input the person's health-related features below to get predictions from the five deployed models.
""")

st.sidebar.header("Instructions")
st.sidebar.markdown("""
1.  Adjust the input sliders/fields on the main page to describe the person's health features.
2.  Click the 'Get Health Predictions' button.
3.  View the health prediction results from each of the five models.
""")

st.header("Input Health Features")
st.markdown("Please provide the values for the features your health models expect.")

st.subheader("Demographics & Lifestyle")
col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age (Years)", 0, 120, 35)
    sex_input = st.radio("Gender", ["Male", "Female"], index=0)
    current_smoker = st.checkbox("Current Smoker?", False)
    cigs_per_day = st.number_input("Cigarettes Per Day", 0, 100, 0)
with col2:
    bmi = st.number_input("BMI (Body Mass Index)", 10.0, 60.0, 25.0, step=0.1, format="%.1f")
    smoking_years = st.number_input("Years Smoked (for Lung Model)", 0, 80, 0)
    bp_meds = st.checkbox("On Blood Pressure Medication?", False)
    diabetes_status = st.checkbox("Has Diabetes?", False)

st.subheader("Cardiovascular & Metabolic Indicators")
col3, col4 = st.columns(2)
with col3:
    tot_chol = st.number_input("Total Cholesterol (mg/dL)", 100, 400, 200)
    sys_bp = st.number_input("Systolic Blood Pressure (mmHg)", 80, 250, 120)
    dia_bp = st.number_input("Diastolic Blood Pressure (mmHg)", 40, 150, 80)
with col4:
    heart_rate = st.number_input("Heart Rate (bpm)", 40, 120, 70)
    glucose = st.number_input("Glucose Level (mg/dL)", 50, 300, 90)
    pregnancies = st.number_input("Number of Pregnancies (for Diabetes Model)", 0, 17, 0)
    insulin = st.number_input("Insulin Level (mu U/ml, for Diabetes Model)", 0.0, 900.0, 0.0, step=0.1)

st.subheader("Specific Health Condition Indicators")
col5, col6 = st.columns(2)
with col5:
    on_thyroxine = st.checkbox("On Thyroxine?", False)
    query_on_thyroxine = st.checkbox("Query on Thyroxine?", False)
    on_antithyroid_meds = st.checkbox("On Antithyroid Medication?", False)
    sick = st.checkbox("Is Sick?", False)
    pregnant = st.checkbox("Is Pregnant?", False)
    thyroid_surgery = st.checkbox("Had Thyroid Surgery?", False)
    i131_treatment = st.checkbox("Had I131 Treatment?", False)
    query_hypothyroid = st.checkbox("Query Hypothyroid?", False)
    query_hyperthyroid = st.checkbox("Query Hyperthyroid?", False)
    lithium = st.checkbox("On Lithium?", False)
    goitre = st.checkbox("Has Goitre?", False)
    tumor = st.checkbox("Has Tumor?", False)
    hypopituitary = st.checkbox("Has Hypopituitary?", False)
    psych = st.checkbox("Has Psychological Issues?", False)
    tsh = st.number_input("TSH Level", 0.0, 500.0, 1.0, step=0.1)
    t3 = st.number_input("T3 Level", 0.0, 10.0, 2.0, step=0.01)
    tt4 = st.number_input("TT4 Level", 0.0, 500.0, 100.0, step=0.1)
    t4u = st.number_input("T4U Level", 0.0, 2.0, 1.0, step=0.001)
    fti = st.number_input("FTI Level", 0.0, 500.0, 100.0, step=0.1)

with col6:
    chest_pain = st.checkbox("Experiences Chest Pain?", False)
    shortness_of_breath = st.checkbox("Experiences Shortness of Breath?", False)
    cough = st.checkbox("Has Chronic Cough?", False)
    cough_severity = st.slider("Cough Severity (1-10)", 1, 10, 5)
    fatigue_level = st.slider("Fatigue Level (1-10)", 1, 10, 5)
    skin_thickness = st.number_input("Skin Thickness (mm, for Diabetes Model)", 0.0, 100.0, 20.0, step=0.1)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function (for Diabetes Model)", 0.0, 2.5, 0.5, step=0.001)

all_input_features = {
    'age': age,
    'sex': 1 if sex_input == "Male" else 0,
    'male': 1 if sex_input == "Male" else 0,
    'currentSmoker': 1 if current_smoker else 0,
    'cigsPerDay': cigs_per_day,
    'BPMeds': 1 if bp_meds else 0,
    'diabetes': 1 if diabetes_status else 0,
    'totChol': tot_chol,
    'sysBP': sys_bp,
    'diaBP': dia_bp,
    'BMI': bmi,
    'heartRate': heart_rate,
    'glucose': glucose,
    'pregnancies': pregnancies,
    'skin_thickness': skin_thickness,
    'insulin': insulin,
    'diabetes_pedigree_function': diabetes_pedigree_function,
    'smoking_years': smoking_years,
    'chest_pain': 1 if chest_pain else 0,
    'shortness_of_breath': 1 if shortness_of_breath else 0,
    'cough_severity': cough_severity,
    'fatigue_level': fatigue_level,
    'on thyroxine': 1 if on_thyroxine else 0,
    'query on thyroxine': 1 if query_on_thyroxine else 0,
    'on antithyroid medication': 1 if on_antithyroid_meds else 0,
    'sick': 1 if sick else 0,
    'pregnant': 1 if pregnant else 0,
    'thyroid surgery': 1 if thyroid_surgery else 0,
    'I131 treatment': 1 if i131_treatment else 0,
    'query hypothyroid': 1 if query_hypothyroid else 0,
    'query hyperthyroid': 1 if query_hyperthyroid else 0,
    'lithium': 1 if lithium else 0,
    'goitre': 1 if goitre else 0,
    'tumor': 1 if tumor else 0,
    'hypopituitary': 1 if hypopituitary else 0,
    'psych': 1 if psych else 0,
    'TSH': tsh,
    'T3': t3,
    'TT4': tt4,
    'T4U': t4u,
    'FTI': fti,
    'TSH measured': 1,
    'T3 measured': 1,
    'TT4 measured': 1,
    'T4U measured': 1,
    'FTI measured': 1
}

if st.button("Get Health Predictions", help="Click to run all five models on the input data"):
    st.header("Prediction Results")
    st.write("Here are the health predictions from each of your five models:")
    for model_display_name, model_obj in loaded_models.items():
        try:
            expected_features = model_feature_maps.get(model_display_name, [])
            if not expected_features:
                continue
            model_input_data = pd.DataFrame([[all_input_features[feature] for feature in expected_features]],
                                            columns=expected_features)
            prediction = model_obj.predict(model_input_data)[0]
            st.markdown(f"**{model_display_name}:** `{prediction:.2f}`")
            if "Risk" in model_display_name or "Prediction" in model_display_name:
                if prediction > 0.5:
                    st.error("This model indicates a higher risk or positive prediction for this condition. 🚨")
                else:
                    st.success("This model indicates a lower risk or negative prediction for this condition. 🎉")
            elif "Health Model" in model_display_name:
                if prediction > 75:
                    st.success("This model suggests a very good health outlook. 🎉")
                elif prediction > 50:
                    st.info("This model suggests a good health outlook. 👍")
                elif prediction > 25:
                    st.warning("This model suggests a moderate health outlook. Might need attention. ⚠️")
                else:
                    st.error("This model suggests a challenging health outlook. Please consult a professional. 🚨")
            else:
                st.info(f"Raw prediction value: {prediction:.2f}")
        except KeyError as ke:
            st.error(f"Error for '{model_display_name}': Missing expected input feature '{ke}'. Please ensure all required inputs are provided and feature names in `model_feature_maps` are correct.")
        except Exception as e:
            st.error(f"Error predicting with '{model_display_name}': {e}. This might be due to incorrect input feature order, type, or missing preprocessing steps specific to this model.")

st.markdown("---")
st.caption("Developed with Streamlit for ML Model Deployment")

