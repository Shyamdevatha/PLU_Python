import sqlite3
from collections import deque

conn = sqlite3.connect("cab.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Drivers(id INTEGER PRIMARY KEY,name TEXT,city TEXT,status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY,name TEXT,city TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Bookings(id INTEGER PRIMARY KEY,customer_id INTEGER,driver_id INTEGER)")

cur.execute("DELETE FROM Drivers")
cur.execute("DELETE FROM Customers")
cur.execute("DELETE FROM Bookings")

cur.executemany("INSERT INTO Drivers VALUES(?,?,?,?)",[
    (101,"Rahul","A","Available"),
    (102,"Kiran","B","Available"),
    (103,"Rohan","C","Available")
])

cur.executemany("INSERT INTO Customers VALUES(?,?,?)",[
    (1,"Anjali","A")
])

cur.executemany("INSERT INTO Bookings VALUES(?,?,?)",[
    (201,1,None)
])

conn.commit()

cur.execute("""
SELECT Drivers.id,Drivers.name,Drivers.city
FROM Drivers
WHERE status='Available'
""")

drivers = cur.fetchall()

print("Available Drivers")
for d in drivers:
    print(d)

graph = {
    "A":["B"],
    "B":["A","C"],
    "C":["B"]
}

def bfs(graph,start):
    q = deque([start])
    visited = []
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    return visited

cur.execute("SELECT city FROM Customers WHERE id=1")
customer_city = cur.fetchone()[0]

route = bfs(graph, customer_city)
print("\nNearest Route:", route)

driver = drivers[0]

cur.execute("UPDATE Drivers SET status='Booked' WHERE id=?", (driver[0],))
cur.execute("UPDATE Bookings SET driver_id=? WHERE id=201", (driver[0],))
conn.commit()

print("\nBooking Assigned")
cur.execute("""
SELECT Bookings.id,Customers.name,Drivers.name
FROM Bookings
JOIN Customers ON Bookings.customer_id=Customers.id
JOIN Drivers ON Bookings.driver_id=Drivers.id
""")

for i in cur.fetchall():
    print(i)

conn.close()