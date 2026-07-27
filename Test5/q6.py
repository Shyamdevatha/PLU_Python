import sqlite3
from collections import deque

conn = sqlite3.connect("food.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Restaurant(id INTEGER PRIMARY KEY,name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Delivery(id INTEGER PRIMARY KEY,area TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Orders(id INTEGER PRIMARY KEY,restaurant_id INTEGER,delivery_id INTEGER,status TEXT)")

cur.execute("DELETE FROM Restaurant")
cur.execute("DELETE FROM Delivery")
cur.execute("DELETE FROM Orders")

cur.executemany("INSERT INTO Restaurant VALUES(?,?)",[
    (1,"Dominos"),
    (2,"KFC"),
    (3,"Burger King")
])

cur.executemany("INSERT INTO Delivery VALUES(?,?)",[
    (1,"A"),
    (2,"B"),
    (3,"C")
])

cur.executemany("INSERT INTO Orders VALUES(?,?,?,?)",[
    (101,1,1,"Pending"),
    (102,2,2,"Pending"),
    (103,3,3,"Pending")
])

conn.commit()

cur.execute("""
SELECT Orders.id,Restaurant.name,Delivery.area
FROM Orders
JOIN Restaurant ON Orders.restaurant_id=Restaurant.id
JOIN Delivery ON Orders.delivery_id=Delivery.id
WHERE status='Pending'
""")

orders = cur.fetchall()

print("Pending Orders")
for i in orders:
    print(i)

graph = {
    "Dominos":["A"],
    "KFC":["B"],
    "Burger King":["C"],
    "A":[],
    "B":[],
    "C":[]
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

print("\nDelivery Route")
for o in orders:
    print(bfs(graph,o[1]))

for o in orders:
    cur.execute("UPDATE Orders SET status='Delivered' WHERE id=?",(o[0],))

conn.commit()

print("\nUpdated Orders")
cur.execute("SELECT * FROM Orders")
for i in cur.fetchall():
    print(i)

conn.close()