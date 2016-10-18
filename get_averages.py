import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f)

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


'''
sum = 0.0
ctr = 0
name = ""
id = 0
newName = 0

for record in data:
    if (newName == 0):
        sum = 0.0
        ctr = 0
        name = record[0]
        id = record[1]
        newName = 1
    elif (name == record[0]):
        print record[2]
        sum += record[2]
        ctr += 1
    else:
        print "Name: %s, ID: %d, Average: %f"%(name, id, sum/ctr)
        newName = 0
    

'''
