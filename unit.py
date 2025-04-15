# Project 01: Unit Converter
# Build a Google-style Unit Converter using Python and Streamlit

import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🌐")

st.title("🌐 Unit Converter")

# Dropdown for selecting conversion type
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

# Side-by-side input columns
col1, col2 = st.columns(2)

# From and To unit selection based on conversion type
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligram", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligram", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Input value
value = st.number_input("Enter the value to convert", format="%.2f")

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1,
        'Kilometers': 0.001,
        'Centimeters': 100,
        'Millimeters': 1000,
        'Miles': 0.000621371,
        'Yards': 1.09361,
        'Inches': 39.3701,
        'Feet': 3.28084
    }
    return value / length_units[from_unit] * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1,
        'Grams': 1000,
        'Milligram': 1000000,
        'Pounds': 2.20462,
        'Ounces': 35.274
    }
    return value / weight_units[from_unit] * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None  # Fallback if no valid conversion path

# Convert button
if st.button("Convert"):
    result = None
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Something went wrong. Please check your selections.")

# Footer
st.markdown("---")
st.markdown("Created by **Qusain Farooq**")
