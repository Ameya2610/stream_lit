import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the main structure of the app
st.title("PocketGrow: Smart Savings & Investment for Students")

# Section 1: Set Savings Goals
st.header("Set Your Savings Goals")
goal_name = st.text_input("What is your savings goal?", "E.g., Buy a new laptop")
goal_amount = st.number_input("How much do you need to save?", min_value=0.0, step=0.01)
current_savings = st.number_input("How much have you saved so far?", min_value=0.0, step=0.01)

if st.button("Add Goal"):
    st.write(f"Goal '{goal_name}' added! You need to save {goal_amount - current_savings} more.")

# Section 2: Track Savings
st.header("Track Your Savings Progress")
progress = (current_savings / goal_amount) * 100 if goal_amount > 0 else 0
st.progress(progress)

# Section 3: Investment Options
st.header("Explore Basic Investment Options")
investment_amount = st.slider("How much would you like to invest?", min_value=0.0, max_value=current_savings, step=0.01)

investment_options = {
    "Stocks": 0.07,  # average return rate
    "Bonds": 0.03,   # average return rate
    "ETFs": 0.05     # average return rate
}

investment_choice = st.selectbox("Choose an investment option", options=list(investment_options.keys()))

# Calculate projected returns
years = st.slider("Investment period (years)", min_value=1, max_value=10)
projected_return = investment_amount * (1 + investment_options[investment_choice])**years

st.write(f"By investing ${investment_amount:.2f} in {investment_choice}, you could have ${projected_return:.2f} after {years} years.")

# Section 4: Financial Education
st.header("Financial Education")
st.write("**Why Save and Invest?** Saving and investing early can help you achieve financial security and reach your goals faster. By starting now, you can take advantage of compound interest, which is the interest on your savings or investments earning interest themselves.")

# Section 5: Budgeting Tool
st.header("Budgeting Tool")
income = st.number_input("Enter your monthly income (e.g., pocket money)", min_value=0.0, step=0.01)
expenses = st.number_input("Enter your monthly expenses", min_value=0.0, step=0.01)
savings_budget = income - expenses

if savings_budget > 0:
    st.success(f"You can save ${savings_budget:.2f} this month.")
else:
    st.warning("Your expenses exceed your income. Consider adjusting your spending.")

# Section 6: Visualization
st.header("Savings and Investment Growth Over Time")
years_projection = np.arange(1, years + 1)
savings_growth = current_savings * (1 + 0.01)**years_projection
investment_growth = investment_amount * (1 + investment_options[investment_choice])**years_projection

fig, ax = plt.subplots()
ax.plot(years_projection, savings_growth, label='Savings Growth')
ax.plot(years_projection, investment_growth, label='Investment Growth')
ax.set_xlabel('Years')
ax.set_ylabel('Amount ($)')
ax.legend()
st.pyplot(fig)

# Section 7: Summary
st.header("Summary")
st.write(f"Total Savings Goal: ${goal_amount}")
st.write(f"Current Savings: ${current_savings}")
st.write(f"Remaining Amount to Save: ${goal_amount - current_savings}")
st.write(f"Projected Investment Return: ${projected_return:.2f} after {years} years")

# Footer
st.write("### Thank you for using PocketGrow! Start saving and investing today for a better tomorrow.")
