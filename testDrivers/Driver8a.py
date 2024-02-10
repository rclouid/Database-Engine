"""
STUDENT(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:4

1111:Robert Adams:1234:Computer Science:4.0:
1112:Charles Bailey:5656:Computer Science:3.5:
1113:David Beatle:1212:Mathematics:3.5:
1114:Graham Gooch:5678:Computer Science:3.5:

ENROLL(SID:INTEGER,COURSE:VARCHAR,GRADE:VARCHAR)
Number of tuples:3

1111:Database Systems:A:
1114:Database Systems:B:
1114:Java Programming:A:

STUDENT_JOIN_ENROLL(SID:INTEGER,SNAME:VARCHAR,PHONE:INTEGER,MAJOR:VARCHAR,GPA:DECIMAL,COURSE:VARCHAR,GRADE:VARCHAR)
Number of tuples:3

1111:Robert Adams:1234:Computer Science:4.0:Database Systems:A:
1114:Graham Gooch:5678:Computer Science:3.5:Database Systems:B:
1114:Graham Gooch:5678:Computer Science:3.5:Java Programming:A:
"""

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

	attr2 = ["SID","COURSE","GRADE"]
	dom2 = ["INTEGER","VARCHAR","VARCHAR"]
	r2 = Relation("ENROLL",attr2,dom2)
	t = Tuple(attr2,dom2)
	t.addComponent(1111)
	t.addComponent("Database Systems")
	t.addComponent("A")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1114)
	t.addComponent("Database Systems")
	t.addComponent("B")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1114)
	t.addComponent("Java Programming")
	t.addComponent("A")
	r2.addTuple(t)

	db.addRelation(r1)

	print(r1)
	print(r2)

	r3 = r1.join(r2)
	r3.setName("STUDENT_JOIN_ENROLL")
	print(r3)

main()
