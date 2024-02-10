import sys
from Database import *
from Relation import *
from Tuple import * 

def main():
    db = Database()
    db.initializeDatabase(sys.argv[1])
    ## List the names of all employees with two or more dependents.

        ##project[lname,fname](
        ##(rename[ssn](
        ##    project[essn1](
        ##     select[essn1=essn2 and dname1<>dname2](
        ##        (rename[essn1,dname1](project[essn,dependent_name](dependent))
        ##         times
        ##         rename[essn2,dname2](project[essn,dependent_name](dependent)))
        ##        )
         ##     )
        ##    )
        ##join
        ##employee)
        ##);

    employee = db.getRelation("EMPLOYEE")
    dependent = db.getRelation("DEPENDENT")

    r1 = dependent.project(["ESSN","DEPENDENT_NAME"]).rename(["ESSN1", "DNAME1"])
    r2 = dependent.project(["ESSN","DEPENDENT_NAME"]).rename(["ESSN2", "DNAME2"])
    r3 = r1.times(r2).select("col", "ESSN1", "=", "col", "ESSN2").select("col", "DNAME1", "<>", "col", "DNAME2")
    
    r4 = r3.project(["ESSN1"]).rename(["SSN"]).join(employee)
    answer = r4.project(["LNAME", "FNAME"])
    answer.setName("ANSWER")

    print(answer)
main()        