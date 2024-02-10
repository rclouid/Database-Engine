import sys
from Database import *
from Relation import *
from Tuple import * 

def main():
    db = Database()
    db.initializeDatabase(sys.argv[1])
    ##List the names of managers who have at least one dependent.

    ##project[lname,fname](
    ##((rename[ssn](project[mgrssn](department))
        ##join
        ##rename[ssn](project[essn](dependent))
    ##)
    ##join
    ##employee
    ## )
    ##);

    employee = db.getRelation("EMPLOYEE")
    department = db.getRelation("DEPARTMENT")
    dependent = db.getRelation("DEPENDENT")

    r1 = department.project(["MGRSSN"]).rename(["SSN"])
    r2 = dependent.project(["ESSN"]).rename(["SSN"])
    r3 = r1.join(r2).join(employee)
    answer = r3.project(["LNAME", "FNAME"])
    answer.setName("ANSWER")

    print(answer) 

main()    