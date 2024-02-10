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