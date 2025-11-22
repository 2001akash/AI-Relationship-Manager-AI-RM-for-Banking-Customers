"""
TEST QUERIES FOR AI RELATIONSHIP MANAGER (AI-RM)

Use these queries to test all features of your backend:

------------------------------------------------------
1. Transaction Insights
------------------------------------------------------
Example queries:
- "How much did I spend on food last week?"
- "How much did I spend on travel this month?"
- "What was my highest expense this month?"
- "Show my total bills for last month."
- "Show my shopping expenses for September."
- "How much did I spend overall last week?"

Expected output includes:
✔ Total amount
✔ Category-wise breakdown
✔ Highest transaction
✔ Time-based filtering

------------------------------------------------------
2. Investment Overview
------------------------------------------------------
Example queries:
- "What’s my return on equity mutual funds?"
- "Show my investment performance."
- "How are my debt investments performing?"
- "What is my overall portfolio return?"
- "Should I rebalance my portfolio?"

Expected output includes:
✔ Invested amount
✔ Current value
✔ Absolute & percentage returns
✔ Product-wise summary

------------------------------------------------------
3. Personalized Recommendations
------------------------------------------------------
Example queries:
- "You have idle funds; consider short-term debt funds for 6–8% yield."
- "Can I invest ₹20,000 in a low-risk plan?"
- "Suggest something safe for ₹50,000."
- "Give me a recommendation based on my profile."
- "Where should I invest ₹10,000?"

Expected output includes:
✔ Allocation suggestions (equity/debt mix)
✔ Product suggestions
✔ Risk-based advice
✔ Human RM-style disclaimer

------------------------------------------------------
4. Smart Summaries
------------------------------------------------------
Example queries:
- "Give me a summary of my finances for September."
- "What are my top 3 recurring payments?"
- "Show my complete spending summary."
- "Give me a monthly overview of spending and investments."
- "Summarize my expenses and returns."

Expected output includes:
✔ Total spending
✔ Category distribution
✔ Recurring charges (rent, bills, subscriptions)
✔ Investment summary
✔ Overall returns

------------------------------------------------------

You can use this file as:
• Documentation for your project
• A QA/test checklist
• A script to manually test with /chat endpoint
"""


import requests

API_URL = "http://localhost:8000/chat"

# List of test queries to automatically run
queries = [
    # Transaction Insights
    "How much did I spend on food last week?",
    "What was my highest expense this month?",
    "Show my total bills last month.",
    "How much did I spend overall last week?",

    # Investment Overview
    "What’s my return on equity mutual funds?",
    "Show my investment performance.",
    "How are my debt investments performing?",

    # Personalized Recommendations
    "Can I invest ₹20,000 in a low-risk plan?",
    "Suggest something safe for ₹50,000.",
    "Give me an investment recommendation.",

    # Smart Summaries
    "Give me a summary of my finances for September.",
    "What are my top 3 recurring payments?",
    "Show my complete financial summary.",
]


def run_tests():
    print("\n===== Running Test Queries for AI-RM =====\n")

    for q in queries:
        print(f"\n--- Query: {q} ---")
        response = requests.post(API_URL, json={"query": q})

        if response.status_code == 200:
            print("Response:")
            print(response.json()["reply"])
        else:
            print(f"Error {response.status_code}: Could not get response.")


if __name__ == "__main__":
    run_tests()
