import sqlite3

conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
name TEXT,
category TEXT,
quantity INTEGER,
price REAL)
""")

cur.execute("DELETE FROM Products")

data = [
    (101,"Laptop","Electronics",15,75000),
    (102,"Mouse","Electronics",8,500),
    (103,"Keyboard","Electronics",12,1200),
    (104,"Monitor","Electronics",5,15000),
    (105,"Printer","Electronics",3,8000)
]

cur.executemany("INSERT INTO Products VALUES(?,?,?,?,?)", data)
conn.commit()

class Product:
    def __init__(self,id,name,category,qty,price):
        self.id=id
        self.name=name
        self.category=category
        self.qty=qty
        self.price=price

cur.execute("SELECT * FROM Products")
products=[Product(*row) for row in cur.fetchall()]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    res=[]
    while left and right:
        if left[0].qty<right[0].qty:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res+left+right

def binary_search(arr,key):
    arr=sorted(arr,key=lambda x:x.id)
    l,r=0,len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[m].id==key:
            return arr[m]
        elif arr[m].id<key:
            l=m+1
        else:
            r=m-1
    return None

print("All Products")
for p in products:
    print(p.id,p.name,p.category,p.qty,p.price)

print("\nSorted by Quantity")
for p in merge_sort(products):
    print(p.id,p.name,p.qty)

pid=int(input("\nEnter Product ID: "))
p=binary_search(products,pid)

if p:
    print("Found:",p.id,p.name,p.category,p.qty,p.price)
else:
    print("Product Not Found")

print("\nLow Stock Products")
for p in products:
    if p.qty<10:
        print(p.id,p.name,p.qty)

conn.close()