# **LangChain: Postgres AI**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.0.0-orange)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)](https://www.postgresql.org/)

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Querying the Database](#querying-the-database)
- [License](#license)

---

## **Overview**

LangChain: Postgres AI is an intelligent assistant that allows users to interact with a PostgreSQL database using natural language queries. It leverages the power of LangChain agents and the Groq API for seamless integration with database operations.

---

## **Features**
- **Natural Language Querying**: Translate user queries into SQL and fetch results dynamically.
- **Streamlit Interface**: An intuitive web-based UI for interaction.
- **Dynamic Database Integration**: Configure and connect to any PostgreSQL database.
- **Error Handling**: Robust error detection and informative feedback.
- **Agent-Based Execution**: Leverages LangChain Zero-Shot React agents for database queries.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/langchain-postgres-ai.git
cd langchain-postgres-ai
```

### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4.Configure PostgreSQL Database**
```bash
[postgresql]
host=<YOUR_DB_HOST>
database=<YOUR_DB_NAME>
user=<YOUR_DB_USER>
password=<YOUR_DB_PASSWORD>
port=<YOUR_DB_PORT>
```
## **Usage**

### **1. Run the script**
```bash
streamlit run app.py
```
### **2. Provide API Key**
```bash
Input your Groq API key in the sidebar under Groq API Key.
```
## **Database Configuration**

### **1. Configure the Database Connection**
```bash
def connect():
    connection = psycopg2.connect(**config())
    return connection

```

## **Querying the Database**

### **1. Chat Input**
```bash
"Show all employees earning above $50,000."
```
### **2. Database Results**
```bash
"The system translates the query into SQL and fetches results from the connected database."
```

## **License**


```bash
"This project is licensed under the MIT License. See the LICENSE file for more details
."
```

