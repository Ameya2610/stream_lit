import streamlit as st
import pandas as pd

# Function to calculate the estimated price (this is a dummy function for demonstration purposes)
def estimate_price(area, bedrooms, bathrooms, location):
    base_price = 100000  # base price in dollars
    price = base_price + (area * 150) + (bedrooms * 50000) + (bathrooms * 30000)

    # Adjusting price based on location (this is a simplistic model)
    if location.lower() == "city center":
        price *= 1.5
    elif location.lower() == "suburbs":
        price *= 1.2
    return price

# Title of the app
st.title("Real Estate Price Estimator")

# Section to input property details
st.header("Property Details")

# Input fields
area = st.number_input("Area (in square feet)", min_value=500, max_value=10000, value=1000, step=100)
bedrooms = st.selectbox("Number of Bedrooms", options=[1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", options=[1, 2, 3])
location = st.selectbox("Location", options=["City Center", "Suburbs", "Countryside"])

# Button to estimate the price
if st.button("Estimate Price"):
    estimated_price = estimate_price(area, bedrooms, bathrooms, location)
    st.subheader(f"Estimated Property Price: ${estimated_price:,.2f}")

# Sample data to display a list of properties
st.header("Listed Properties")
properties = pd.DataFrame({
    'Area (sqft)': [1200, 850, 950, 1500],
    'Bedrooms': [3, 2, 2, 4],
    'Bathrooms': [2, 1, 2, 3],
    'Location': ["City Center", "Suburbs", "Countryside", "City Center"],
    'Price ($)': [180000, 120000, 135000, 220000]
})

st.dataframe(properties)

# Footer
st.write("This is a simple real estate app to estimate property prices.")
