"""
BAR(BNAME:VARCHAR)
Number of tuples:4

Jillians:
Dugans:
ESPN Zone:
Charlies:

DRINKER(DNAME:VARCHAR)
Number of tuples:5

John:
Peter:
Donald:
Jeremy:
Clark:

SELLS(BAR:VARCHAR,BEER:VARCHAR,PRICE:INTEGER)
Number of tuples:9

Jillians:Bud:6:
Jillians:Michelob:6:
Jillians:Heineken:8:
Dugans:Bud:9:
Dugans:Michelob:10:
Dugans:Fosters:12:
ESPN Zone:Fosters:9:
Charlies:Heineken:10:
Charlies:Foster:10:
"""
from Database import *
from Relation import *
import sys

def main():
    db = Database()
    db.initializeDatabase(sys.argv[1])
    db.displaySchema()
    r1 = db.getRelation("BAR")
    print(r1)
    r2 = db.getRelation("DRINKER")
    print(r2)
    r3 = db.getRelation("SELLS")
    print(r3)

main()
