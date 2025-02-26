import streamlit as st

# Custom CSS for Styling
st.markdown(
    """
    <style>
        /* Background color */
        .stApp {
            background-color:#f0f8ff;
            padding: 20px;
        }

        /* Title styling */
        h1 {
            color: #333;
            text-align: center;
            font-family: Arial, sans-serif;
        }

        /*  input styling */
        .stSelectbox, .stNumberInput {
            background-color:  #987;
               box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1); 
            border-radius: 5px;
            padding: 10px;
        }

        /* Button styling */
        .stButton>button {
            background-color: #987;
            box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1); 
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }

        /* Button hover effect */
        .stButton>button:hover {
            background-color: #0056b3;
        }

        /* Result box */
        .result-box {
            background-color: #654;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #ffff;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🌍🔄 Unit Converter")

# Conversion Functions
def length_converter(value):
    return value / 1000  # meters to kilometers

def weight_converter(value):
    return value * 1000  # kilograms to grams

def temp_converter(value):
    return (value * 9/5) + 32  # Celsius to Fahrenheit

# Dropdown for unit selection
unit_type = st.selectbox("📌 Select Conversion Type", [
    "Length (m to km)", "Weight (kg to g)", "Temperature (C to F)"
])

# Input Value
value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")

# Convert Button
if st.button("🚀 Convert Now"):
    if unit_type == "Length (m to km)":
        result = length_converter(value)
        unit = "km"
    elif unit_type == "Weight (kg to g)":
        result = weight_converter(value)
        unit = "g"
    elif unit_type == "Temperature (C to F)":
        result = temp_converter(value)
        unit = "°F"
    else:
        result = "Invalid selection"
        unit = ""

    st.markdown(f'<div class="result-box">✅ Converted Value: {result} {unit}</div>', unsafe_allow_html=True)

# Ensure script runs properly
if __name__ == "__main__":
    pass  # Streamlit handles execution automatically
