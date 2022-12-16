import streamlit as st
import pandas as pd
import joblib
from PIL import Image

filename = 'body_performance_model.pk1'
model = joblib.load(filename)
columns = ['age', 'gender', 'height_in', 'weight_ibs', 'body fat_%', 'gripForce',
       'sit and bend forward_in', 'sit-ups counts', 'broad jump_in']

image = Image.open('Biomechanics.JPEG')
st.title('Body Performance Detector')
st.image(image)
st.write('Enter the required Information below '
         'to figure out your body performance on a scale from A to D (best to worst).')

age = st.slider('Age:', 0, 100, None)
gender = st.selectbox('Gender:', ['M', 'F'])
height_in = st.slider('Height (in):', 0, 96, None)
weight_ibs = st.slider('Weight (ibs):', 0, 500, None)
body_fat = st.slider('Body Fat %:', 0, 100, None)
gripForce = st.slider('GripForce:', 0, 100, None)
sitandbend = st.slider('How many inches can you sit and bend forward?', 0, 120, None)
situps = st.slider('Max Sit-ups in One Sitting:', 0, 150, None)
broadjump_in = st.slider('Broad Jump (in):', 0, 150, None)


def predict():
    prediction = model.predict(
        pd.DataFrame(
            [[age,
              gender,
              height_in,
              weight_ibs,
              body_fat,
              gripForce,
              sitandbend,
              situps,
              broadjump_in]],
            columns=columns
        )
    )
    if prediction == 0:
        prediction = 'A'
    elif prediction == 1:
        prediction = 'B'
    elif prediction == 2:
        prediction = 'C'
    elif prediction == 3:
        prediction = 'D'

    return prediction


if st.button('Predict Performance'):
    y = predict()
    st.success(f'Performance Rating: {y}')


