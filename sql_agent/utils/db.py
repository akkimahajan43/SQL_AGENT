import sqlite3
import pandas as pd

DB_NAME = "database.db"

def run_query(query):

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def get_schema():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """)

    tables = cursor.fetchall()

    schema = ""

    for table in tables:

        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = cursor.fetchall()

        schema += f"\nTable: {table_name}\n"

        for col in columns:
            schema += f"- {col[1]}\n"

    conn.close()

    return schema