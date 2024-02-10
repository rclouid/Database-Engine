import sys
from Database import *
from Relation import *
from Tuple import * 

def main():
    db = Database()
    db.initializeDatabase(sys.argv[1])
    ## Make a list of project numbers for projects that involve an employee whose 
    ## last name is "Smith", either as a worker or as a manager of the department that 
    ## controls the project.

    ##( project[pno](
    ##   (rename[essn](project[ssn](select[lname='Smith'](employee))) 
    ##    join 
    ##    works_on
    ##   )
    ##  )
    ## union
    ##  project[pnumber](
    ##   ( rename[dnum](project[dnumber](select[lname='Smith'](
    ##       (employee 
    ##        join   
    ##        rename[dname,dnumber,ssn,mgrstartdate](department)
    ##       )
    ##       )
    ##       )
    ##     ) 
    ##     join 
    ##     projects
    ##    )
    ##  )
    #)

    employee = db.getRelation("EMPLOYEE")
    projects = db.getRelation("PROJECTS")
    works_on = db.getRelation("WORKS_ON")
    department = db.getRelation("DEPARTMENT")

    r1 = employee.join(department.rename(["DNAME","DNUMBER","SSN","MGRSTARTDATE"]))
    r2 = r1.select("col", "LNAME", "=", "str","Smith").project(["DNUMBER"]).rename(["DNUM"])
    r3 = r2.join(projects).project(["PNUMBER"])
    r4 = employee.select("col", "LNAME", "=", "str","Smith").project(["SSN"]).rename(["ESSN"])
    r5 = r4.join(works_on).project(["PNO"])
    answer = r5.union(r3)
    answer.setName("ANSWER")

    print(answer)    
    

main()   