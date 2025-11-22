### **README.md**

---

# **AI Relationship Manager (AI-RM)**

A conversational financial insights assistant built using **FastAPI** + **HTML/JS UI**.

---

## 🧭 **Overview**

The **AI Relationship Manager (AI-RM)** is a chatbot designed to simulate how a human banking Relationship Manager interacts with customers.
It provides:

* Expense & transaction insights
* Investment performance summaries
* Personalized recommendations
* Smart financial summaries

This project uses **mock customer data**, **FastAPI backend**, and a **simple HTML UI** to demonstrate the concept.

---

## 🎯 **Core Features**

### **1. Transaction Insights**

AI-RM can understand time-based and category-based queries.

Example queries:

* *“How much did I spend on food last week?”*
* *“What was my highest expense this month?”*
* *“Show my total bills last month.”*

It returns:

* Total amount
* Category breakdown
* Highest transaction
* Time-range filtering

---

### **2. Investment Overview**

AI-RM summarizes investment performance across:

* Equity funds
* Debt funds
* FDs
* Hybrid funds

Example queries:

* *“What’s my return on equity mutual funds?”*
* *“Show my investment performance.”*
* *“Should I rebalance my portfolio?”*

It returns:

* Invested amount
* Current value
* Percentage returns
* Product-wise breakdown

---

### **3. Personalized Recommendations**

Based on profile + risk category, AI-RM suggests next steps.

Example queries:

* *“Can I invest ₹20,000 in a low-risk plan?”*
* *“Suggest something safe for ₹50,000.”*
* *“Where should I invest ₹10,000?”*

Outputs include:

* Ideal allocation
* Return expectations
* Suggested products
* Real-world style RM disclaimer

---

### **4. Smart Financial Summaries**

Example queries:

* *“Give me a summary of my finances for September.”*
* *“What are my top 3 recurring payments?”*
* *“Show my complete financial summary.”*

Summaries include:

* Total spending
* Category distribution
* Recurring charges
* Investment growth
* Overall return %

---

## 📁 **Project Structure**

```
ai_rm/
│
├── main.py                   # FastAPI entry point
├── config.py                 # Mock customer, transaction, investment data
├── models.py                 # Pydantic models
│
├── handlers/
│     ├── transaction_handler.py
│     ├── investment_handler.py
│     ├── recommendation_handler.py
│     └── summary_handler.py
│
├── utils/
│     ├── date_utils.py
│     ├── txn_utils.py
│     ├── formatting.py
│     └── intent_utils.py
│
├── index.html                # Frontend chat UI
└── requirements.txt
```

---

## 🚀 **How to Run the Project**

### **1. Install dependencies**

```
pip install -r requirements.txt
```

### **2. Start the backend**

```
python main.py
```

Backend runs at:

```
http://localhost:8000
```

Swagger Docs:

```
http://localhost:8000/docs
```

### **3. Run the UI**

Just open:

```
index.html
```

in your browser.

---

## 🧪 **Testing the Chatbot**

Use these sample queries to test each module:

### **Transaction Insights**

* How much did I spend on food last week?
* How much did I spend last month?
* What was my highest expense this month?

### **Investment Overview**

* What’s my return on equity mutual funds?
* Show my investment performance.
* How are my FDs performing?

### **Personalized Recommendations**

* Can I invest ₹20,000 in a low-risk plan?
* Suggest something safe for ₹50,000.
* Where should I invest ₹10,000?

### **Smart Summaries**

* Give me a summary of my finances for September.
* What are my top 3 recurring payments?
* Show my complete financial summary.

---

## 🧩 **Technologies Used**

* **Python 3.10+**
* **FastAPI**
* **Pydantic**
* **HTML, CSS, JavaScript**
* **CORS Middleware**
* **Uvicorn**

---

## 📝 **Disclaimer**

This project uses **mock financial data** only.
All insights, recommendations, and summaries are generated for demonstration purposes and **should not be considered actual financial advice**.

---

