import sqlite3
import heapq

conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Students(
roll INTEGER PRIMARY KEY,
name TEXT,
cgpa REAL,
skills TEXT,
status TEXT)
""")

cur.execute("DELETE FROM Students")

data = [
    (101,"Rahul",8.5,"Python","Not Placed"),
    (102,"Anjali",7.2,"Java","Not Placed"),
    (103,"Kiran",9.1,"C++","Not Placed"),
    (104,"Priya",8.0,"Python, SQL","Not Placed"),
    (105,"Rohan",6.8,"JavaScript","Not Placed")
]

cur.executemany("INSERT INTO Students VALUES(?,?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Students")
students = cur.fetchall()

heap = []
for s in students:
    heapq.heappush(heap, (-s[2], s))

print("Students Sorted by CGPA")
sorted_students = []
while heap:
    student = heapq.heappop(heap)[1]
    sorted_students.append(student)
    print(student)

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

roll = int(input("\nEnter Roll Number: "))
student = binary_search(students, roll)

if student:
    print("Student Found:", student)
else:
    print("Student Not Found")

print("\nEligible Students (CGPA > 7.5)")
for s in students:
    if s[2] > 7.5:
        print(s)

roll = int(input("\nEnter Roll Number to Place: "))
cur.execute("UPDATE Students SET status='Placed' WHERE roll=?", (roll,))
conn.commit()

print("\nUpdated Student List")
cur.execute("SELECT * FROM Students")
for s in cur.fetchall():
    print(s)

conn.close()