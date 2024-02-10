"""
STUDENT(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:4

1111:Robert Adams:1234:Computer Science:4.0:
1112:Charles Bailey:5656:Computer Science:3.5:
1113:David Beatle:1212:Mathematics:3.5:
1114:Graham Gooch:5678:Computer Science:3.5:

SELECT_SID_=_1114(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:1

1114:Graham Gooch:5678:Computer Science:3.5:

SELECT_GPA_>_3.5(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:1

1111:Robert Adams:1234:Computer Science:4.0:

SELECT_MAJOR_=_Computer Science(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:3

1111:Robert Adams:1234:Computer Science:4.0:
1112:Charles Bailey:5656:Computer Science:3.5:
1114:Graham Gooch:5678:Computer Science:3.5:
"""
from Database import *
from Relation import *
from Tuple import *

def main():
    db = Database()
    attr1 = ["SID","SNAME","PHONE","MAJOR","GPA"]
    dom1 =  ["INTEGER","VARCHAR","INTEGER","VARCHAR","DECIMAL"]
    r1 =  Relation("STUDENT",attr1,dom1)
    t =  Tuple(attr1,dom1)
    t.addComponent(1111)
    t.addComponent("Robert Adams")
    t.addComponent(1234)
    t.addComponent("Computer Science")
    t.addComponent(4.0)
    r1.addTuple(t)
    t =  Tuple(attr1,dom1)
    t.addComponent(1112)
    t.addComponent("Charles Bailey")
    t.addComponent(5656)
    t.addComponent("Computer Science")
    t.addComponent(3.5)
    r1.addTuple(t)
    t =  Tuple(attr1,dom1)
    t.addComponent(1113)
    t.addComponent("David Beatle")
    t.addComponent(1212)
    t.addComponent("Mathematics")
    t.addComponent(3.5)
    r1.addTuple(t)
    t =  Tuple(attr1,dom1)
    t.addComponent(1114)
    t.addComponent("Graham Gooch")
    t.addComponent(5678)
    t.addComponent("Computer Science")
    t.addComponent(3.5)
    r1.addTuple(t)

    db.addRelation(r1)

    print(r1)

    r2 = r1.select("col","SID","=","num",1114)
    r2.setName("SELECT_SID_=_1114")
    print(r2)

    r3 = r1.select("col","GPA",">","num",3.5)
    r3.setName("SELECT_GPA_>_3.5")
    print(r3)

    r4 = r1.select("col","MAJOR","=","str","Computer Science")
    r4.setName("SELECT_MAJOR_=_Computer Science")
    print(r4)

main()
