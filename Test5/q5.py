import sqlite3

conn = sqlite3.connect("movies.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Movies(
id INTEGER PRIMARY KEY,
title TEXT,
genre TEXT,
rating REAL,
watch_count INTEGER)
""")

cur.execute("DELETE FROM Movies")

data = [
    (101,"Pushpa: The Rise","Action",9.4,9800000),
    (102,"Pushpa 2: The Rule","Action",9.8,15000000),
    (103,"Ala Vaikunthapurramuloo","Family",9.5,12000000),
    (104,"Race Gurram","Action",9.2,8500000),
    (105,"Sarrainodu","Action",9.1,8000000),
    (106,"DJ: Duvvada Jagannadham","Action",8.9,7000000)
]

cur.executemany("INSERT INTO Movies VALUES(?,?,?,?,?)", data)
conn.commit()

cur.execute("SELECT * FROM Movies")
movies = cur.fetchall()

print("Movies Sorted by Rating")
sorted_movies = sorted(movies, key=lambda x: x[3], reverse=True)
for m in sorted_movies:
    print(m)

def binary_search(arr, key):
    arr = sorted(arr, key=lambda x: x[0])
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid][0] == key:
            return arr[mid]
        elif arr[mid][0] < key:
            l = mid + 1
        else:
            r = mid - 1
    return None

mid = int(input("\nEnter Movie ID: "))
movie = binary_search(movies, mid)

if movie:
    print("Movie Found:", movie)
else:
    print("Movie Not Found")

print("\nTop Rated Movies")
for m in sorted_movies[:10]:
    print(m)

print("\nMost Watched Movie in Each Genre")
genres = {}

for m in movies:
    if m[2] not in genres or m[4] > genres[m[2]][4]:
        genres[m[2]] = m

for g in genres.values():
    print(g)

conn.close()