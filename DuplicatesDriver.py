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