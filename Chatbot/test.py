import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Slider widget
x = st.slider("Select a value", 0, 100)

# Display the selected value

st.write(f"The selected value is {x}")

# Display the square of the selected value
st.write(f"{x} squared is {x * x}")
