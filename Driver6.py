from Database import *
from Relation import *
from Tuple import *

def main():
    db = Database()
    attr1 = ["SID","SNAME","PHONE","MAJOR","GPA"]
    dom1 = ["INTEGER","VARCHAR","INTEGER","VARCHAR","DECIMAL"]
    r1 = Relation("STUDENT",attr1,dom1)
    t = Tuple(attr1,dom1)
    t.addComponent(1111)
    t.addComponent("Robert Adams")
    t.addComponent(1234)
    t.addComponent("Computer Science")
    t.addComponent(4.0)
    r1.addTuple(t)
    t = Tuple(attr1,dom1)
    t.addComponent(1112)
    t.addComponent("Charles Bailey")
    t.addComponent(5656)
    t.addComponent("Computer Science")
    t.addComponent(3.5)
    r1.addTuple(t)
    t = Tuple(attr1,dom1)
    t.addComponent(1113)
    t.addComponent("David Beatle")
    t.addComponent(1212)
    t.addComponent("Mathematics")
    t.addComponent(3.5)
    r1.addTuple(t)
    t = Tuple(attr1,dom1)
    t.addComponent(1114)
    t.addComponent("Graham Gooch")
    t.addComponent(5678)
    t.addComponent("Computer Science")
    t.addComponent(3.5)
    r1.addTuple(t)

    db.addRelation(r1)

    print(r1)

    cnames1 = ["SID","GPA"]
    r2 = r1.project(cnames1)
    r2.setName("PROJECT_SID_GPA_STUDENT")
    print(r2)

    cnames2 = ["MAJOR","GPA"]
    r3 = r1.project(cnames2)
    r3.setName("PROJECT_MAJOR_GPA_STUDENT")
    print(r3)

    cnames3 = ["MAJOR"]
    r4 = r1.project(cnames3)
    r4.setName("PROJECT_MAJOR_STUDENT")
    print(r4)

main()