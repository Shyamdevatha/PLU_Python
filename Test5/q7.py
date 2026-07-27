import sqlite3
from datetime import datetime

conn = sqlite3.connect("attendance.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Employee(
id INTEGER PRIMARY KEY,
name TEXT,
checkin TEXT,
checkout TEXT)
""")

cur.execute("DELETE FROM Employee")

data = [
    (101,"Rahul","09:00","18:00"),
    (102,"Anjali","09:30","19:30"),
    (103,"Kiran","10:00","20:00"),
    (104,"Priya","09:00","17:00"),
    (105,"Rohan","08:30","18:30")
]

cur.executemany("INSERT INTO Employee VALUES(?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Employee")
employees = cur.fetchall()

hours = []

print("Employee Working Hours")
for e in employees:
    t1 = datetime.strptime(e[2], "%H:%M")
    t2 = datetime.strptime(e[3], "%H:%M")
    h = (t2 - t1).seconds / 3600
    week = h * 5
    hours.append((e[0], e[1], week))
    print(e[0], e[1], week, "hours")

print("\nSorted by Working Hours")
hours.sort(key=lambda x: x[2], reverse=True)
for h in hours:
    print(h)

def binary_search(arr, key):
    arr = sorted(arr, key=lambda x: x[0])
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m][0] == key:
            return arr[m]
        elif arr[m][0] < key:
            l = m + 1
        else:
            r = m - 1
    return None

eid = int(input("\nEnter Employee ID: "))
emp = binary_search(employees, eid)

if emp:
    print("Employee Found:", emp)
else:
    print("Employee Not Found")

print("\nEmployees Worked More Than 45 Hours")
for h in hours:
    if h[2] > 45:
        print(h)

conn.close()