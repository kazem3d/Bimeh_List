import sqlite3

#define tuple for choices: sex,nationality,city,country,educationa,field,job

conn=sqlite3.connect("ChoicesDB")
curser=conn.cursor()

sex_choice=(
    ('1','مرد'),
    ('2','زن')
)

nat_choice=(
    ('1','ايراني'),
    ('2','غیر ايراني')
)

city_choice=()
curser.execute('SELECT code,name FROM city')
rows=curser.fetchall()
for row in rows:
    city_choice+=(row,)



field=()
curser.execute('SELECT code,name FROM field')
rows=curser.fetchall()
for row in rows:
    field+=(row,)

education=()
curser.execute('SELECT code,name FROM education')
rows=curser.fetchall()
for row in rows:
    education+=(row,)

country=()
curser.execute('SELECT code,name FROM country')
rows=curser.fetchall()
for row in rows:
    country+=(row,)

job_choice=()
curser.execute('SELECT code,name FROM job_slim')
rows=curser.fetchall()
for row in rows:
    job_choice+=(row,)



