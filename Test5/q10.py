import sqlite3

conn = sqlite3.connect("sales.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Sales(
id INTEGER PRIMARY KEY,
product TEXT,
quantity INTEGER,
revenue REAL,
region TEXT,
incentive TEXT)
""")

cur.execute("DELETE FROM Sales")

data = [
    (101,"Laptop",5,250000,"North","No"),
    (102,"Mouse",20,10000,"South","No"),
    (103,"Keyboard",15,18000,"East","No"),
    (104,"Monitor",8,120000,"North","No"),
    (105,"Printer",6,60000,"West","No"),
    (106,"Speaker",12,36000,"South","No")
]

cur.executemany("INSERT INTO Sales VALUES(?,?,?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Sales")
sales = cur.fetchall()

print("Sales Records")
for s in sales:
    print(s)

print("\nSorted by Revenue")
sorted_sales = sorted(sales, key=lambda x: x[3], reverse=True)
for s in sorted_sales:
    print(s)

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

eid = int(input("\nEnter Salesperson ID: "))
emp = binary_search(sales, eid)

if emp:
    print("Record Found:", emp)
else:
    print("Record Not Found")

print("\nTop 5 Salespersons")
for s in sorted_sales[:5]:
    print(s)

region = {}
for s in sales:
    region[s[4]] = region.get(s[4], 0) + s[3]

best = max(region, key=region.get)
print("\nHighest Revenue Region:", best, region[best])

cur.execute("UPDATE Sales SET incentive='Yes' WHERE revenue>=50000")
conn.commit()

print("\nUpdated Records")
cur.execute("SELECT * FROM Sales")
for s in cur.fetchall():
    print(s)

conn.close()