from Database import *
from Relation import *
from Tuple import *
"""
Database Class: Encapsulates the entire database, which is nothing but a collection of relations (or tables). 
	We shall use a dictionary to store the relations with relation name serving as the key and the Relation
 	object as the value.
Relation Class: Encapsulates a relation or table; includes both schema and instance.
Tuple Class: Encapsulates a tuple or row of a relation; includes both schema and instance.


Database Schema: 

STUDENT(SID:INTEGER,SNAME:VARCHAR,MAJOR:VARCHAR,GPA:DECIMAL)
COURSE(CNUM:VARCHAR,CTITLE:VARCHAR,DESCRIPTION:VARCHAR,CREDITS:INTEGER)

Relation r1: 
STUDENT(SID:INTEGER,SNAME:VARCHAR,MAJOR:VARCHAR,GPA:DECIMAL)
Number of tuples:2

1111:Robert Adams:Computer Science:4.0:
1112:Charles Bailey:Mathematics:3.0:

Relation r2: 
COURSE(CNUM:VARCHAR,CTITLE:VARCHAR,DESCRIPTION:VARCHAR,CREDITS:INTEGER)
Number of tuples:2

CSC 1301:Intro to CS I:Java Programming and breadth topics:4:
CSC 1302:Intro to CS II:In depth Java Programming and some breadth topics:4:
"""

CSC 1301:Intro to CS I:Java Programming and breadth topics:4:
CSC 1302:Intro to CS II:In depth Java Programming and some breadth topics:4:
def main():
	db = Database()

	attr1 = ["SID","SNAME","MAJOR","GPA"] 
	dom1  = ["INTEGER","VARCHAR","VARCHAR","DECIMAL"]
	r1 = Relation("STUDENT",attr1,dom1)

	t = Tuple(attr1,dom1)
	t.addComponent(1111)
	t.addComponent("Robert Adams")
	t.addComponent("Computer Science")
	t.addComponent(4.00)
	r1.addTuple(t)

	t = Tuple(attr1,dom1)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	t.addComponent("Mathematics")
	t.addComponent(3.00)
	r1.addTuple(t)

	db.addRelation(r1)

	attr2 = ["CNUM","CTITLE","DESCRIPTION","CREDITS"]
	dom2 = ["VARCHAR","VARCHAR","VARCHAR","INTEGER"]
	r2 = Relation("COURSE",attr2,dom2)

	t = Tuple(attr2,dom2)
	t.addComponent("CSC 1301")
	t.addComponent("Intro to CS I")
	t.addComponent("Java Programming and breadth topics")
	t.addComponent(4)
	r2.addTuple(t)

	t = Tuple(attr2,dom2)
	t.addComponent("CSC 1302")
	t.addComponent("Intro to CS II")
	t.addComponent("In depth Java Programming and some breadth topics")
	t.addComponent(4)
	r2.addTuple(t)

	db.addRelation(r2)
	
	print("Database Schema: \n" + db.displaySchema())

	print("Relation r1: \n"+str(r1))
	print("Relation r2: \n"+str(r2))
main()
