import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    product TEXT,
    amount REAL,
    city TEXT,
    order_date TEXT
)
""")

data = [
    ("Akshay", "Laptop", 80000, "Pune", "2026-05-01"),
    ("Rahul", "Mouse", 500, "Mumbai", "2026-05-02"),
    ("Sneha", "Keyboard", 2000, "Delhi", "2026-05-03"),
    ("Akshay", "Monitor", 15000, "Pune", "2026-05-04"),
]

cursor.executemany("""
INSERT INTO sales (
    customer,
    product,
    amount,
    city,
    order_date
)
VALUES (?, ?, ?, ?, ?)
""", data)

conn.commit()

conn.close()

print("Database Created")