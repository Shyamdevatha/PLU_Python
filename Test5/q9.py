import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY,title TEXT,available TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Members(id INTEGER PRIMARY KEY,name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Borrowed(id INTEGER PRIMARY KEY,book_id INTEGER,member_id INTEGER,status TEXT)")

cur.execute("DELETE FROM Books")
cur.execute("DELETE FROM Members")
cur.execute("DELETE FROM Borrowed")

cur.executemany("INSERT INTO Books VALUES(?,?,?)",[
    (101,"Python","Yes"),
    (102,"C Programming","Yes"),
    (103,"Java","No"),
    (104,"Data Structures","Yes"),
    (105,"DBMS","Yes")
])

cur.executemany("INSERT INTO Members VALUES(?,?)",[
    (1,"Rahul"),
    (2,"Anjali")
])

cur.executemany("INSERT INTO Borrowed VALUES(?,?,?,?)",[
    (1,103,1,"Overdue")
])

conn.commit()

cur.execute("SELECT * FROM Books WHERE available='Yes'")
books = cur.fetchall()

print("Available Books")
for b in books:
    print(b)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    while left and right:
        if left[0][1] < right[0][1]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + left + right

print("\nBooks Sorted Alphabetically")
for b in merge_sort(books):
    print(b)

def binary_search(arr,key):
    arr = sorted(arr,key=lambda x:x[0])
    l,r = 0,len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m][0]==key:
            return arr[m]
        elif arr[m][0]<key:
            l=m+1
        else:
            r=m-1
    return None

bid = int(input("\nEnter Book ID: "))
book = binary_search(books,bid)

if book:
    print("Book Found:",book)
else:
    print("Book Not Found")

bid = int(input("\nEnter Book ID to Borrow: "))
cur.execute("UPDATE Books SET available='No' WHERE id=?",(bid,))
conn.commit()

print("\nOverdue Books")
cur.execute("""
SELECT Books.title,Members.name
FROM Borrowed
JOIN Books ON Borrowed.book_id=Books.id
JOIN Members ON Borrowed.member_id=Members.id
WHERE Borrowed.status='Overdue'
""")

for i in cur.fetchall():
    print(i)

conn.close()