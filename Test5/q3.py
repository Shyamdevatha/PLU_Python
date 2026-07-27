import sqlite3

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Transactions(
id INTEGER PRIMARY KEY,
account TEXT,
amount REAL,
date TEXT,
type TEXT)
""")

cur.execute("DELETE FROM Transactions")

data = [
    (101,"A1001",5000,"2026-07-01","Credit"),
    (102,"A1002",2000,"2026-07-02","Debit"),
    (103,"A1003",8000,"2026-07-03","Credit"),
    (104,"A1004",1500,"2026-07-04","Debit"),
    (105,"A1005",10000,"2026-07-05","Credit"),
    (106,"A1006",3000,"2026-07-06","Debit")
]

cur.executemany("INSERT INTO Transactions VALUES(?,?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Transactions")
rows = cur.fetchall()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x[2] <= pivot[2]]
    right = [x for x in arr[1:] if x[2] > pivot[2]]
    return quick_sort(left) + [pivot] + quick_sort(right)

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

print("Sorted by Amount")
sorted_data = quick_sort(rows)
for i in sorted_data:
    print(i)

tid = int(input("\nEnter Transaction ID: "))
result = binary_search(rows, tid)

if result:
    print("\nTransaction Found")
    print(result)
else:
    print("Transaction Not Found")

credit = sum(i[2] for i in rows if i[4] == "Credit")
debit = sum(i[2] for i in rows if i[4] == "Debit")

print("\nTotal Credit:", credit)
print("Total Debit:", debit)

print("\nTop 5 Highest Transactions")
for i in sorted(rows, key=lambda x: x[2], reverse=True)[:5]:
    print(i)

conn.close()
