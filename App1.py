import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Initialize session state for savings tracking
if 'savings' not in st.session_state:
    st.session_state.savings = []

# Title of the app
st.title("Pocket Money Saver & Investor")

# Sidebar for user input
st.sidebar.header("Input Your Savings")
amount = st.sidebar.number_input("Amount to Save ($)", min_value=0.0, value=0.0, step=0.01)
date = st.sidebar.date_input("Date", datetime.date.today())

# Add savings to session state
if st.sidebar.button("Add Savings"):
    st.session_state.savings.append({"date": date, "amount": amount})
    st.sidebar.success(f"Saved ${amount} on {date}")

# Display Savings History
st.header("Savings History")
if st.session_state.savings:
    df_savings = pd.DataFrame(st.session_state.savings)
    st.table(df_savings)
    
    # Plot savings over time
    st.subheader("Savings Over Time")
    df_savings['date'] = pd.to_datetime(df_savings['date'])
    df_savings = df_savings.sort_values(by='date')
    df_savings['cumulative_savings'] = df_savings['amount'].cumsum()
    plt.plot(df_savings['date'], df_savings['cumulative_savings'], marker='o')
    plt.title("Cumulative Savings Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Savings ($)")
    st.pyplot(plt.gcf())
else:
    st.write("No savings data yet. Start by adding your savings!")

# Investment Options Section
st.header("Investment Options")
st.write("Explore simple investment options to grow your pocket money:")

investment_options = {
    "Savings Account": 1.02,
    "Stock Market Index Fund": 1.07,
    "Cryptocurrency": 1.2,
}

investment_choice = st.selectbox("Choose an Investment Option", list(investment_options.keys()))

if investment_choice:
    years = st.slider("Number of Years to Invest", 1, 10, 5)
    initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, value=0.0, step=0.01)
    
    growth_factor = investment_options[investment_choice] ** years
    final_amount = initial_investment * growth_factor
    
    st.write(f"After {years} years, your investment in {investment_choice} could grow to approximately ${final_amount:.2f}.")

# Educational Content Section
st.header("Learn About Smart Investing")
st.write("""
- **Savings Account**: A safe way to grow your money with a guaranteed but small interest rate.
- **Stock Market Index Fund**: A collection of stocks that gives you exposure to a broad market index.
- **Cryptocurrency**: A highly volatile and risky investment, but with potential for high returns.
- **Diversification**: Spread your investments across different types to reduce risk.
- **Compound Interest**: The process where the value of an investment increases because the earnings on an investment earn interest as time passes.
""")

# Footer
st.sidebar.write("This app is designed to help you learn about saving and investing your pocket money. Happy saving and investing!")
