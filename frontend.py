import streamlit as st
import pandas as pd
import backend as db

st.set_page_config(page_title="Performance Management System", layout="wide")

st.title("📊 Performance Management System (PMS)")

menu = ["Add Goal", "View Goals", "Update Goal", "Delete Goal", "Analytics Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- CRUD Operations (same as before) ---------------- #
# Add Goal
if choice == "Add Goal":
    st.subheader("➕ Add New Goal")
    emp_id = st.text_input("Employee ID")
    description = st.text_area("Goal Description")
    due_date = st.date_input("Due Date")
    status = st.selectbox("Status", ["Draft", "In Progress", "Completed", "Cancelled"])
    if st.button("Add Goal"):
        db.add_goal(emp_id, description, due_date, status)
        st.success("✅ Goal added successfully!")

# View Goals
elif choice == "View Goals":
    st.subheader("📖 View All Goals")
    goals = db.get_goals()
    if goals:
        st.table(goals)
    else:
        st.warning("No goals found!")

# Update Goal
elif choice == "Update Goal":
    st.subheader("✏️ Update Goal Status")
    goal_id = st.text_input("Goal ID to Update")
    new_status = st.selectbox("New Status", ["Draft", "In Progress", "Completed", "Cancelled"])
    if st.button("Update Goal"):
        db.update_goal_status(goal_id, new_status)
        st.success("✅ Goal status updated!")

# Delete Goal
elif choice == "Delete Goal":
    st.subheader("🗑️ Delete Goal")
    goal_id = st.text_input("Goal ID to Delete")
    if st.button("Delete Goal"):
        db.delete_goal(goal_id)
        st.success("✅ Goal deleted successfully!")

# ---------------- ANALYTICS DASHBOARD ---------------- #
elif choice == "Analytics Dashboard":
    st.subheader("📊 PMS Analytics Dashboard")

    # KPIs
    count, avg_days, min_due, max_due = db.get_analytics()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Goals", count)
    col2.metric("Avg Days Until Due", round(avg_days, 2) if avg_days else "N/A")
    col3.metric("Earliest Due Date", min_due)
    col4.metric("Latest Due Date", max_due)

    st.markdown("---")

    # Goals by Status (Charts)
    status_data = db.goals_by_status()
    if status_data:
        df = pd.DataFrame(status_data, columns=["Status", "Count"])

        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(df.set_index("Status"))
        with col2:
            st.write("📌 Goals Distribution")
            st.dataframe(df)
            st.pyplot(df.set_index("Status").plot.pie(y="Count", autopct="%.1f%%", legend=False).figure)
    else:
        st.warning("No goals found to analyze!")
