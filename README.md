# 💬 SQLite Chat Assistant

An interactive chat assistant built with **Streamlit** and **SQLite** that allows users to query employee and department data using natural language. Just type your question, and the assistant will convert it into an SQL query to fetch the relevant data from the database.

---

## 🚀 Features
- **Natural Language Querying:** Ask questions like “Show all employees in the Sales department” or “Find employees earning more than 50000.”
- **Real-Time Data Display:** Instantly view query results in a structured table format.
- **Lightweight & Fast:** No external API required—everything runs locally or on Streamlit Cloud.
- **Simple Deployment:** Deploy on [Streamlit Cloud](https://share.streamlit.io) for free.

---

## 📊 Example Queries
- "Show all employees in the Sales department"
- "Who is the manager of the Marketing department?"
- "Find employees earning more than 50000"
- "List all departments"
- "Find employees hired after 2020-01-01"

---

## 🗄️ Database Schema

- **Employees Table:** `ID`, `Name`, `Department`, `Salary`, `Hire_Date`
- **Departments Table:** `ID`, `Name`, `Manager`

The data is stored in a SQLite database (`employees.db`).

---

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**

```git clone https://github.com/your-username/chat-assistant.git```

```cd chat-assistant```

### 2️⃣ **Install Dependencies**
Make sure you have Python installed. Then run:

```pip install -r requirements.txt```

### 3️⃣ **Run the Application Locally**

```streamlit run streamlit_app.py```

Open the provided URL in your browser (usually ```http://localhost:8501```).

---

## 🌍 Deploy on Streamlit Cloud
1. Push your code to GitHub.
2. Go to Streamlit Cloud.
3. Click "New App" → Select your repository.
4. Set the main file path as streamlit_app.py.
5. Click Deploy.

Your app will be live at:

```https://your-username-chat-assistant.streamlit.app```

---

## 📦 Project Structure

```chat-assistant/```

```├── db.py                 # SQLite database setup```

```├── query_handler.py      # Converts natural language to SQL queries```

```├── employees.db              # SQLite database```

```├── streamlit_app.py          # Main Streamlit app```

```├── requirements.txt          # Python dependencies```

```└── README.md                 # Project documentation```

---

## 📜 License
This project is licensed under the MIT License.

---

## ✍️ Author
Sunny Tiwari
