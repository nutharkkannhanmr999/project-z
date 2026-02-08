
import sqlite3
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# ---------------- DB ----------------

DB_NAME = "queue.db"


def get_conn():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def add_patient(name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO queue (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def get_all_patients():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM queue ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()
    return rows


def call_next_patient():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM queue ORDER BY id ASC LIMIT 1")
    row = cur.fetchone()

    if row:
        cur.execute("DELETE FROM queue WHERE id = ?", (row[0],))
        conn.commit()

    conn.close()
    return row


# ---------------- UI ----------------

st.set_page_config(page_title="Project Z v2")

init_db()

# live refresh every 2 seconds
st_autorefresh(interval=2000, key="queue_refresh")

st.title("Project Z v2 – Hospital Queue")

name = st.text_input("Enter patient name")

col1, col2 = st.columns(2)

with col1:
    if st.button("Add patient"):
        if name.strip():
            add_patient(name.strip())
            st.success("Patient added")
        else:
            st.warning("Enter a name")

with col2:
    if st.button("Call next"):
        row = call_next_patient()
        if row:
            st.success(f"Now serving : {row[1]}")
        else:
            st.info("Queue empty")


st.subheader("Current Queue")

rows = get_all_patients()

if not rows:
    st.write("No patients")
else:
    for i, r in enumerate(rows, start=1):
        st.write(f"{i}. {r[1]}")