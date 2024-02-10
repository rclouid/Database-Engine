from Database import *
from Relation import *
from Tuple import *
"""
REL1(COL1:INTEGER,COL2:VARCHAR)
Number of tuples: 5

1111:Robert Adams:
1112:Charles Bailey:
1114:Richard Johnson:
1115:Graham Gooch:
1116:John Miller:

REL2(COL1:INTEGER,COL2:VARCHAR)
Number of tuples: 5

1113:John Smith:
1112:Charles Bailey:
1115:Graham Gooch:
1116:John Miller:
1117:Hugh Howell:

REL1_UNION_REL2(COL1:INTEGER,COL2:VARCHAR)
Number of tuples: 7

1111:Robert Adams:
1112:Charles Bailey:
1114:Richard Johnson:
1115:Graham Gooch:
1116:John Miller:
1113:John Smith:
1117:Hugh Howell:

REL1_INTERSECT_REL2(COL1:INTEGER,COL2:VARCHAR)
Number of tuples: 3

1112:Charles Bailey:
1115:Graham Gooch:
1116:John Miller:

REL1_MINUS_REL2(COL1:INTEGER,COL2:VARCHAR)
Number of tuples: 2

1111:Robert Adams:
1114:Richard Johnson:
"""
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

    r3 = r1.union(r2)
    r3.setName("REL1_UNION_REL2")
    r4 = r1.intersect(r2)
    r4.setName("REL1_INTERSECT_REL2")
    r5 = r1.minus(r2)
    r5.setName("REL1_MINUS_REL2")

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)

main()
