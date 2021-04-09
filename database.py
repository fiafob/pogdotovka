import sqlite3


dbname = input()
con = sqlite3.connect(dbname)

cur = con.cursor()

a, b = int(input()), int(input())
result = cur.execute(f"""select students.name, ege.subject, ege.mark from students, ege
where ege.mark in ({a}, {b}) and ege.student = students.id""").fetchall()


print(result)