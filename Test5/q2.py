import sqlite3
import heapq

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Patients(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
priority INTEGER,
status TEXT)
""")

cur.execute("DELETE FROM Patients")

data = [
    (101,"Rahul",25,2,"Waiting"),
    (102,"Anjali",40,1,"Waiting"),
    (103,"Kiran",35,3,"Waiting"),
    (104,"Priya",50,1,"Waiting"),
    (105,"Rohan",28,2,"Waiting")
]

cur.executemany("INSERT INTO Patients VALUES(?,?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Patients WHERE status='Waiting'")
rows = cur.fetchall()

pq = []

for row in rows:
    heapq.heappush(pq, (row[3], row[0], row[1], row[2]))

print("Attending Patients")

while pq:
    priority, pid, name, age = heapq.heappop(pq)
    print(pid, name, age, priority)
    cur.execute("UPDATE Patients SET status='Attended' WHERE id=?", (pid,))
    conn.commit()

cur.execute("SELECT * FROM Patients WHERE status='Waiting'")
rows = cur.fetchall()

print("\nRemaining Patients")
if rows:
    for r in rows:
        print(r)
else:
    print("No Patients Waiting")

conn.close()