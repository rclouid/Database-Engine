"""
REL1(COL1:INTEGER,COL2:VARCHAR)
Number of tuples:5

1111:Robert Adams:
1112:Charles Bailey:
1114:Richard Johnson:
1115:Graham Gooch:
1116:John Miller:

RENAMECOLS(NEWCOL1:INTEGER,NEWCOL2:VARCHAR)
Number of tuples:5

1111:Robert Adams:
1112:Charles Bailey:
1114:Richard Johnson:
1115:Graham Gooch:
1116:John Miller:

REL1(COL1:INTEGER,COL2:VARCHAR)
Number of tuples:5

1111:Robert Adams:
1112:Charles Bailey:
1114:Richard Johnson:
1115:Graham Gooch:
1116:John Miller:

REL2(COL1:INTEGER,COL2:VARCHAR)
Number of tuples:5

1113:John Smith:
1112:Charles Bailey:
1115:Graham Gooch:
1116:John Miller:
1117:Hugh Howell:

R1TIMESR2(REL1.COL1:INTEGER,REL1.COL2:VARCHAR,REL2.COL1:INTEGER,REL2.COL2:VARCHAR)
Number of tuples:25

1111:Robert Adams:1113:John Smith:
1111:Robert Adams:1112:Charles Bailey:
1111:Robert Adams:1115:Graham Gooch:
1111:Robert Adams:1116:John Miller:
1111:Robert Adams:1117:Hugh Howell:
1112:Charles Bailey:1113:John Smith:
1112:Charles Bailey:1112:Charles Bailey:
1112:Charles Bailey:1115:Graham Gooch:
1112:Charles Bailey:1116:John Miller:
1112:Charles Bailey:1117:Hugh Howell:
1114:Richard Johnson:1113:John Smith:
1114:Richard Johnson:1112:Charles Bailey:
1114:Richard Johnson:1115:Graham Gooch:
1114:Richard Johnson:1116:John Miller:
1114:Richard Johnson:1117:Hugh Howell:
1115:Graham Gooch:1113:John Smith:
1115:Graham Gooch:1112:Charles Bailey:
1115:Graham Gooch:1115:Graham Gooch:
1115:Graham Gooch:1116:John Miller:
1115:Graham Gooch:1117:Hugh Howell:
1116:John Miller:1113:John Smith:
1116:John Miller:1112:Charles Bailey:
1116:John Miller:1115:Graham Gooch:
1116:John Miller:1116:John Miller:
1116:John Miller:1117:Hugh Howell:
"""
from Database import *
from Relation import *
from Tuple import *

def main():
	db = Database()
	attr1 = ["COL1","COL2"]
	dom1 = ["INTEGER","VARCHAR"]
	r1 = Relation("REL1",attr1,dom1)
	t = Tuple(attr1,dom1)
	t.addComponent(1111)
	t.addComponent("Robert Adams")
	r1.addTuple(t)
	t = Tuple(attr1,dom1)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r1.addTuple(t)
	t = Tuple(attr1,dom1)
	t.addComponent(1114)
	t.addComponent("Richard Johnson")
	r1.addTuple(t)
	t = Tuple(attr1,dom1)
	t.addComponent(1115)
	t.addComponent("Graham Gooch")
	r1.addTuple(t)
	t = Tuple(attr1,dom1)
	t.addComponent(1116)
	t.addComponent("John Miller")
	r1.addTuple(t)
	db.addRelation(r1)

	attr2 = ["COL1","COL2"]
	dom2 = ["INTEGER","VARCHAR"]
	r2 = Relation("REL2",attr2,dom2)
	t = Tuple(attr2,dom2)
	t.addComponent(1113)
	t.addComponent("John Smith")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1115)
	t.addComponent("Graham Gooch")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1116)
	t.addComponent("John Miller")
	r2.addTuple(t)
	t = Tuple(attr2,dom2)
	t.addComponent(1117)
	t.addComponent("Hugh Howell")
	r2.addTuple(t)
	db.addRelation(r2)

	newColNames = ["NEWCOL1","NEWCOL2"]
	r3 = r1.rename(newColNames)
	r3.setName("RENAMECOLS")

	print(r1)
	print(r3)

	print(r1)
	print(r2)
	r4 = r1.times(r2)
	r4.setName("R1TIMESR2")
	print(r4)

main()
