import joblib
import streamlit as st
import pandas as pd
import numpy as np
import datetime


model = joblib.load('model-v1.joblib')
types = ({'GENERAL': 1, 'WHITE': 2, 'BLACK': 3, 'HISPANIC': 4, 'WEALTH': 5})
sex = ({'GENERAL': 1, 'MALE': 2, 'FEMALE': 3})
wealth = ({'Under 100%': 1, '200%': 2, '300%': 3, '400%+': 4})


@st.cache
def predict(data_type, sex_type, wealth_type, normal_type, over_type, obese_type):

    if (data_type == 'GENERAL' and sex_type == 'GENERAL'):
        data = [{'N': normal_type}, {'Ov': over_type}, {'Ob': obese_type}]
    if (data_type == 'GENERAL' and sex_type == 'MALE'):
        data = [{'NM': normal_type}, {'OvM': over_type}, {'ObM': obese_type}]
    if (data_type == 'GENERAL' and sex_type == 'FEMALE'):
        data = [{'NF': normal_type}, {'OvF': over_type}, {'ObF': obese_type}]
    if (data_type == 'WHITE' and sex_type == 'GENERAL'):
        data = [{'NW': normal_type}, {'OvW': over_type}, {'ObW': obese_type}]
    if (data_type == 'WHITE' and sex_type == 'MALE'):
        data = [{'NWM': normal_type}, {
            'OvWM': over_type}, {'ObWM': obese_type}]
    if (data_type == 'WHITE' and sex_type == 'FEMALE'):
        data = [{'NWF': normal_type}, {
            'OvWF': over_type}, {'ObWF': obese_type}]
    if (data_type == 'BLACK' and sex_type == 'GENERAL'):
        data = [{'NB': normal_type}, {'OvB': over_type}, {'ObB': obese_type}]
    if (data_type == 'BLACK' and sex_type == 'MALE'):
        data = [{'NBM': normal_type}, {
            'OvBM': over_type}, {'ObBM': obese_type}]
    if (data_type == 'BLACK' and sex_type == 'FEMALE'):
        data = [{'NBF': normal_type}, {
            'OvBF': over_type}, {'ObBF': obese_type}]
    if (data_type == 'HISPANIC' and sex_type == 'GENERAL'):
        data = [{'NH': normal_type}, {'OvH': over_type}, {'ObH': obese_type}]
    if (data_type == 'HISPANIC' and sex_type == 'MALE'):
        data = [{'NHM': normal_type}, {
            'OvHM': over_type}, {'ObHM': obese_type}]
    if (data_type == 'HISPANIC' and sex_type == 'FEMALE'):
        data = [{'NHF': normal_type}, {
            'OvHF': over_type}, {'ObHF': obese_type}]
    if (data_type == 'WEALTH' and wealth_type == 'Under 100%'):
        data = [{'N100': normal_type}, {
            'Ov100': over_type}, {'Ob100': obese_type}]
    if (data_type == 'WEALTH' and wealth_type == '200%'):
        data = [{'N200': normal_type}, {
            'Ov200': over_type}, {'Ob200': obese_type}]
    if (data_type == 'WEALTH' and wealth_type == '300%'):
        data = [{'N300': normal_type}, {
            'Ov300': over_type}, {'Ob300': obese_type}]
    if (data_type == 'WEALTH' and wealth_type == '400%+'):
        data = [{'N400': normal_type}, {
            'Ov400': over_type}, {'Ob400': obese_type}]
    df = pd.DataFrame([data])

    return model.predict(df)


st.title('Obesity Rate Predictor')
st.image('https://i.insider.com/57d291cadd0895c6308b46b0?width=700&format=jpeg&auto=webp')
st.header('Enter the population data:')

data_type = st.selectbox('Subset associated with data:', types)
sex_type = st.selectbox(
    'Select between general, male, or female (Doesn\'t Affect Wealth-based stats): ', sex)
wealth_type = st.selectbox(
    'Select income in comparison to the poverty level (Only affects wealth-based stats): ', wealth)
normal_type = st.slider(
    'Percentage of selected population with a normal BMI', 0.0, 100.0, 33.0)
over_type = st.slider(
    'Percentage of selected population with an overweight BMI', 0.0, 100.0, 33.0)
obese_type = st.slider(
    'Percentage of selected population with an obese BMI', 0.0, 100.0, 33.0)

if st.button('Predict Source Year of Data'):
    year = predict(data_type=data_type, sex_type=sex_type, wealth_type=wealth_type, normal_type=normal_type,
                   over_type=over_type, obese_type=obese_type)
    if year == 1:
        st.success('The data is from year set 1, approximately 1988-1994.')
    else:
        if year == 2:
            st.success('The data is from year set 1, approximately 1999-2002.')
        else:
            if year == 3:
                st.success(
                    'The data is from year set 1, approximately 2001-2004.')
            else:
                if year == 4:
                    st.success(
                        'The data is from year set 1, approximately 2003-2006.')
                else:
                    if year == 5:
                        st.success(
                            'The data is from year set 5, approximately 2005 - 2008.')
                    else:
                        if year == 6:
                            st.success(
                                'The data is from year set 1, approximately 2007-2010.')
                        else:
                            if year == 7:
                                st.success(
                                    'The data is from year set 1, approximately 2009-2012.')
                            else:
                                if year == 8:
                                    st.success(
                                        'The data is from year set 1, approximately 2011-2014.')
                                else:
                                    if year == 9:
                                        st.success(
                                            'The data is from year set 5, approximately 2013 - 2016.')
                                    else:
                                        if year == 10:
                                            st.success(
                                                'The data is from year set 5, approximately 2015 - 2018.')
