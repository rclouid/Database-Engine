"""
Before Removing Duplicates: 
STUDENT(SID:INTEGER,SNAME:VARCHAR)
Number of tuples:7

1111:Robert Adams:
1112:Charles Bailey:
1113:Donald James:
1112:Charles Bailey:
1112:Charles Bailey:
1114:Michael James:
1113:Donald James:

After Removing Duplicates: 
STUDENT(SID:INTEGER,SNAME:VARCHAR)
Number of tuples:4

1111:Robert Adams:
1112:Charles Bailey:
1113:Donald James:
1114:Michael James:
"""
from Database import *
from Relation import *
from Tuple import *

def main():
	db = Database()

	attr = ["SID","SNAME"]
	dom = ["INTEGER","VARCHAR"]
	r = Relation("STUDENT",attr,dom)

	t = Tuple(attr,dom)
	t.addComponent(1111)
	t.addComponent("Robert Adams")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1113)
	t.addComponent("Donald James")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1114)
	t.addComponent("Michael James")
	r.addTuple(t)

	t = Tuple(attr,dom)
	t.addComponent(1113)
	t.addComponent("Donald James")
	r.addTuple(t)

	db.addRelation(r)

	print("Before Removing Duplicates: \n" + str(r))
	r.removeDuplicates()
	print("After Removing Duplicates: \n" + str(r))

main()
