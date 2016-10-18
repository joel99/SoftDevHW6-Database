import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f)

#needs 2 cursors so that fxns do not interfere
c = db.cursor()
d = db.cursor()

def calcAvg(id):
    q = "SELECT mark FROM courses WHERE courses.id = " + str(id) + ";"
    data = d.execute(q)
    sum = 0.0
    ctr = 0
    for grade in data:
        sum += grade[0]
        ctr += 1
    return sum / ctr

cmd = "SELECT name, id FROM students;"
data = c.execute(cmd)

for record in data:
    
    print "Name: %s, ID: %d, Average: %f"%(record[0], record[1], calcAvg(record[1]))

db.commit()
db.close()
