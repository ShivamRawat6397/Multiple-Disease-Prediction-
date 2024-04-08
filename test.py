import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open(
    'D:/college/project/Multiple Disease Prediction System-20230415T143518Z-001/Multiple Disease Prediction System/saved models/diabetes_model.sav',
    'rb'))

heart_disease_model = pickle.load(open(
    'D:/college/project/Multiple Disease Prediction System-20230415T143518Z-001/Multiple Disease Prediction System/saved models/heart_disease_model.sav',
    'rb'))

parkinsons_model = pickle.load(open(
    'D:/college/project/Multiple Disease Prediction System-20230415T143518Z-001/Multiple Disease Prediction System/saved models/parkinsons_model.sav',
    'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction'],
                               icons=['activity', 'heart', 'person'],
                               default_index=0)

