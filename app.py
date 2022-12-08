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
        data = [normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'GENERAL' and sex_type == 'MALE'):
        data = [None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'GENERAL' and sex_type == 'FEMALE'):
        data = [None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'WHITE' and sex_type == 'GENERAL'):
        data = [None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'WHITE' and sex_type == 'MALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'WHITE' and sex_type == 'FEMALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'BLACK' and sex_type == 'GENERAL'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'BLACK' and sex_type == 'MALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'BLACK' and sex_type == 'FEMALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'HISPANIC' and sex_type == 'GENERAL'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'HISPANIC' and sex_type == 'MALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'HISPANIC' and sex_type == 'FEMALE'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None, None, None, None]
    if (data_type == 'WEALTH' and wealth_type == 'Under 100%'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None, None, None, None]
    if (data_type == 'WEALTH' and wealth_type == '200%'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None, None, None, None]
    if (data_type == 'WEALTH' and wealth_type == '300%'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type, None, None, None]
    if (data_type == 'WEALTH' and wealth_type == '400%+'):
        data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normal_type, over_type, obese_type]
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
