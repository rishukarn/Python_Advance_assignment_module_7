

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create a table named 'students'
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL)''')

print("Table 'students' created successfully.")

# Insert data into the students table
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Bob", 22, "B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Charlie", 21, "A"))

# Commit the changes
conn.commit()

print("Data inserted successfully.")

# Fetch and display data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

# Close the connection
conn.close()

