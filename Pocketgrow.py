import streamlit as st

def main():
    # Title and introduction
    st.title("Grow Your Pocket Money: Smart Investment Choices for Students")
    st.subheader("Learn how to make informed investment decisions and grow your savings.")

    st.markdown("""
    ### Welcome to the Student Investment Guide!
    This interactive platform is designed to help you understand how to invest wisely. Whether you're saving up for something special or simply want to make the most of your allowance, this app will guide you through the basics of investing, risk management, and more.
    """)

    # Section: Understanding Investments
    st.header("🔍 Understanding Investments")
    st.markdown("""
    Investing is about putting your money to work so that it can grow over time. You can invest in various assets like savings accounts, stocks, bonds, or even start your own small business.
    
    Before starting, it's essential to understand the different types of investments and how they can help you achieve your financial goals.
    """)

    # Section: Types of Investments
    st.header("💼 Types of Investments")
    st.markdown("""
    - **Savings Accounts:** Low risk, low return. Ideal for short-term savings.
    - **Stocks:** Higher risk, potential for higher returns. Best for long-term goals.
    - **Bonds:** Moderate risk and returns, suitable for medium-term goals.
    - **Mutual Funds:** A mix of stocks and bonds, managed by professionals.
    - **Small Business:** High risk, high reward. Invest in your own or someone else's business idea.
    """)

    # Interactive tool: Investment Simulation
    st.header("📈 Investment Simulation")
    st.markdown("Use this tool to simulate how your investment could grow over time.")

    # User input: Initial amount and investment choice
    initial_amount = st.number_input("Enter the amount you want to invest (in dollars):", min_value=0, value=100)
    investment_choice = st.selectbox("Choose an investment option:", 
                                     ["Savings Account", "Stocks", "Bonds", "Mutual Funds", "Small Business"])

    # Example logic for investment growth (simplified)
    growth_rates = {
        "Savings Account": 0.01,
        "Stocks": 0.07,
        "Bonds": 0.03,
        "Mutual Funds": 0.05,
        "Small Business": 0.1,
    }

    years = st.slider("Select the number of years you plan to invest:", min_value=1, max_value=20, value=5)
    future_value = initial_amount * (1 + growth_rates[investment_choice]) ** years

    st.write(f"After {years} years, your investment in {investment_choice} could grow to approximately ${future_value:,.2f}.")

    # Section: Risk Management
    st.header("⚖️ Managing Risk")
    st.markdown("""
    Investing involves risks, but understanding and managing these risks is key to successful investing.
    
    - **Diversification:** Spread your investments across different types of assets to reduce risk.
    - **Research:** Always research before investing. Know what you're getting into.
    - **Start Small:** Begin with a small amount that you can afford to lose, especially if you're new to investing.
    """)

    # Section: Tips for Students
    st.header("💡 Tips for Students")
    st.markdown("""
    - **Set a Budget:** Only invest money that you can afford to set aside after covering your essentials.
    - **Be Patient:** Investments take time to grow. Don't expect quick returns.
    - **Learn Continuously:** The more you learn about investing, the better your decisions will be.
    """)

    # Conclusion
    st.header("Start Growing Your Money Today!")
    st.markdown("""
    Now that you have a basic understanding of investing, it's time to start thinking about how you can grow your pocket money. The earlier you start, the more time your money has to grow. Happy investing!
    """)

if __name__ == "__main__":
    main()
