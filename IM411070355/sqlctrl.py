import sqlite3

#INSERT
sqlins ="""
INSERT INTO "main"."product_info" ("name", "version", "remark")
VALUES ('iPhone', '17.42', 'iPhone lover');
"""
cursor.execute(sqlins)
cursor.fetchall()
conn.commit()

#SELECT
conn = sqlite3.connect('DevOps.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM product_info')
records = cursor.fetchall()
print(records)