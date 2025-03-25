import sqlite3

# Step 1: Connect to SQLite Database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")  # Creates a database file named "example.db"
cursor = conn.cursor()

# Step 2: Create a Table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL)''')

# Step 3: Insert Data into the Table
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Bob", 22, "B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Charlie", 21, "A"))

# Commit changes
conn.commit()

# Step 4: Fetch and Display Data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Step 5: Close the Connection
conn.close()