import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="PMS",
        user="postgres",
        password="tiwari"
    )

# CRUD FUNCTIONS (same as before) ...

# ---------------- ANALYTICS ---------------- #
def get_analytics():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*), 
               AVG(EXTRACT(DAY FROM (due_date - CURRENT_DATE))),
               MIN(due_date),
               MAX(due_date)
        FROM goals
    """)
    analytics = cur.fetchone()
    cur.close()
    conn.close()
    return analytics

def goals_by_status():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT status, COUNT(*)
        FROM goals
        GROUP BY status
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
