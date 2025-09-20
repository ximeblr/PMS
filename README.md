# PMS
Tracking team's performance


Performance Management System (PMS) Dashboard

A modern **Performance Management System (PMS)** built with **Streamlit** and **PostgreSQL**, designed to help managers and employees collaborate on goal setting, progress tracking, and performance insights.

This system provides **CRUD operations** for managing goals, tasks, and feedback while offering an **analytics dashboard** powered by SQL aggregate functions.

---

 Key Features
 **Goal & Task Management** – Create, update, delete, and view employee goals.
 **Progress Tracking** – Monitor status updates and track deadlines.
**Feedback System** – Managers can provide direct and automated feedback.
 **Analytics Dashboard** –

* KPIs: Total Goals, Average Due Days, Earliest & Latest Deadlines
* Visuals: Goal distribution (bar & pie charts)
  **ACID-Compliant Transactions** – Ensures reliable and consistent data.

---

 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend**: Python (`psycopg2` for PostgreSQL connection)
* **Database**: PostgreSQL
* **Charts & Analytics**: Streamlit Charts, Matplotlib

---

 Project Structure

```
 PMS-Dashboard
  backend.py        # Database connection & CRUD logic
 frontend.py       # Streamlit UI & Analytics
 ┣ requirements.txt  # Python dependencies
  README.md         # Project Documentation
```

---

##  Database Schema

**Employees Table**

```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100)
);
```

**Goals Table**

```sql
CREATE TABLE goals (
    goal_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES employees(emp_id),
    description TEXT,
    due_date DATE,
    status VARCHAR(20) CHECK (status IN ('Draft','In Progress','Completed','Cancelled'))
);
```

**Feedback Table**

```sql
CREATE TABLE feedback (
    feedback_id SERIAL PRIMARY KEY,
    goal_id INT REFERENCES goals(goal_id),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/pms-dashboard.git
cd pms-dashboard
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

* Create a database: `pms_db`
* Run the schema scripts above
* Update DB credentials in `backend.py`

### 5. Run Application

```bash
streamlit run frontend.py
```

---

 Analytics Dashboard

The system provides insights using SQL functions:

* **COUNT** → Total number of goals per employee
* **SUM** → Aggregated task completions
* **AVG** → Average days to complete goals
* **MIN/MAX** → Earliest & latest deadlines
Example Visuals:

* **Bar Chart**: Goals by Status
* **Pie Chart**: Goal Completion Ratio
* **KPI Cards**: Key performance numbers

---

 ACID Compliance

This PMS ensures reliable performance data through:

* **Atomicity** – Each goal/feedback transaction is all-or-nothing.
* **Consistency** – Foreign keys & constraints preserve data integrity.
* **Isolation** – Concurrent updates are managed via PostgreSQL MVCC.
* **Durability** – Committed transactions are stored with WAL logs.

---

 Future Roadmap

* Role-based dashboards (Manager vs Employee)
* Email/SMS alerts for overdue tasks
* AI-driven feedback sentiment analysis
* Export analytics to PDF & Excel

---

 Author

Developed by **Citizen Software Developer Team** ✨
For startups & enterprises looking to **digitize their PMS workflows**.

---

Would you like me to also **add some example screenshots (mock images)** in the README so it looks visually richer (with dashboard preview sections)?
