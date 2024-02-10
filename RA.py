import sys
from RAParser import parser
from Database import *
from Relation import *
from Tuple import *
from Node import *

def execute_file(filename, db):
  try:
      with open(filename) as f:
          data = f.read().splitlines();
      result = " ".join(list(filter(lambda x: len(x)>0 and x[0]!="#",data)))
      try:
          tree = parser.parse(result)
          set_temp_table_names(tree)
          msg = semantic_checks(tree,db)
          if msg == 'OK':
              print()
              print(evaluate_query(tree,db))
              print()
          else:
              print(msg)
      except Exception as inst:
          print(inst.args[0])
  except FileNotFoundError:
    print("FileNotFoundError: A file with name " + "'" + \
          filename + "' cannot be found")

def read_input():
  result = ''
  data = input('RA: ').strip() 
  while True:
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
      data = input('> ').strip() 
  return result

# In this function you will set the value of Node.relation_name for each node
# of the input tree to a unique value. You can choose to use a glocal variable
# called count, initially set to 0, and each time you need a new relation name,
# you can generate the string "temp_"+str(count). count can be incremented each
# time by 1. This will allow you to generate a unique relation name for each node
# in the tree (temp_0, temp_1, temp_2, etc.
count = 0
def set_temp_table_names(tree):
  global count
  if tree.node_type == "relation":
     return tree
  elif tree.node_type == "select" or tree.node_type == "project" or tree.node_type == "rename":
    set_temp_table_names(tree.left_child)
    tree.relation_name = "temp_" + str(count)
    count += 1
  elif tree.node_type == "union" or tree.node_type == "intersect" or tree.node_type == "minus" or tree.node_type == "join" or tree.node_type == "times":
    set_temp_table_names(tree.left_child)
    set_temp_table_names(tree.right_child)
    tree.relation_name = "temp_" + str(count)
    count += 1
  else: 
     return "That type does not exist"
	

# Perform semantic checks on each node of the tree. 
# Also, set tree.attributes and tree.domains along the way on each node of the tree.
# return "OK" or ERROR message
def semantic_checks(tree, db):
    #checks for relation
    if (tree.node_type == "relation"):
       if (db.getRelation(tree.get_relation_name()) == None):
          return "Relation '" + tree.get_relation_name() + "' does not exist in the database"
       tree.attributes = db.getRelation(tree.get_relation_name()).getAttributes()
       tree.domains = db.getRelation(tree.get_relation_name()).getDomains()
       return 'OK'
    #checks for union, intersect, minus
    elif (tree.node_type == "union" or tree.node_type == "intersect" or tree.node_type == "minus"):
       mesg1 = semantic_checks(tree.left_child, db)
       if mesg1 != 'OK':
          return mesg1
       mesg2 = semantic_checks(tree.right_child, db)
       if mesg2 != 'OK':
          return mesg2  
       if len(tree.left_child.attributes) != len(tree.right_child.attributes):
          return "Semantic Error: Incompatible Relations - different number of columns"
       index = 0
       for type in tree.left_child.domains:
          if (type != tree.right_child.domains[index]):
             return "Semantic Error: Incompatible Relations - the datatypes are not the same"
          index+=1
       tree.attributes = []
       tree.domains = []
       if (tree.node_type == "union" ):
          tree.attributes = tree.left_child.attributes
          tree.domains = tree.left_child.domains
          return 'OK'
       elif (tree.node_type == "intersect"):
          for attr in tree.left_child.attributes:
             if attr in tree.right_child.attributes:
                tree.attributes.append(attr)
                tree.domains.append(tree.right_child.domains[tree.right_child.attributes.index(attr)])
          return 'OK'
       elif (tree.node_type == "minus"):
         l = evaluate_query(tree.left_child, db)
         r = evaluate_query(tree.right_child, db)
         tree.attributes = l.minus(r).attributes
         tree.domains = l.minus(r).domains
         return 'OK'
   #since there is no possible semantic check for times - setting the atrributes and domains
    elif tree.node_type == "times":
         mesg1 = semantic_checks(tree.left_child, db)
         if mesg1 != 'OK':
          return mesg1
         mesg2 = semantic_checks(tree.right_child, db)
         if mesg2 != 'OK':
            return mesg2 
         tree.attributes = []
         tree.domains = []
         for name in tree.left_child.attributes: 
            if name in tree.right_child.attributes:
               tree.attributes.append(tree.left_child.relation_name + "." + name)
            else:
               tree.attributes.append(name)
         for i in tree.left_child.domains: tree.domains.append(i)		
         for name in tree.right_child.attributes:
            if name in tree.left_child.attributes:
               tree.attributes.append(tree.right_child.relation_name + "." + name)
            else:
               tree.attributes.append(name)	
         for i in tree.right_child.domains: tree.domains.append(i)		
         return 'OK'
   #checks for project
    elif tree.node_type == "project":
       mesg = semantic_checks(tree.left_child, db)
       if mesg != 'OK':
          return mesg
       for name in tree.columns:
          if name not in tree.left_child.attributes:
             return "Semantic Error (Project): Attribute '" + name + "' does not exist"
          if tree.columns.count(name) > 1:
            return "Semantic Error (Project): Duplicate Attributes"
          tree.attributes = tree.columns
          tree.domains = []
          for col in tree.columns:
             tree.domains.append(tree.left_child.domains[tree.left_child.attributes.index(col)])
          return 'OK'
   #checks for rename
    elif tree.node_type == "rename":
      mesg = semantic_checks(tree.left_child, db)
      if mesg != 'OK':
          return mesg
      if len(tree.columns) != len(tree.left_child.attributes):
          return "Semantic Error (Rename): Not a valid number of attributes"
      if len(tree.columns) != len(set(tree.columns)):
          return "Semantic Error (Rename): Duplicate Attributes"
      tree.attributes = tree.columns
      tree.domains = tree.left_child.domains
      return 'OK'
   #checks for select
   #check if tree.conditions is in tree.left_child.attributes right
   # tree.conditions is the list of conditions for SELECT [(lop,lot,c,rop,rot)..]
    elif tree.node_type == "select":
       mesg = semantic_checks(tree.left_child, db) 
       if mesg != 'OK':
          return mesg
       rows = len(tree.conditions)
       #while loop to iterate over the rows of tree.conditions
       i = 0
       while i in range(rows):
         #if the left operand is a col and the right operand is not a col
         lIndexDom = tree.left_child.domains[tree.left_child.attributes.index(tree.conditions[i][1])] 
         if lIndexDom == 'VARCHAR':
            lIndexDom = 'str'
         elif lIndexDom == "INTEGER":
            lIndexDom = 'num'
         if tree.conditions[i][0] == "col" and tree.conditions[i][3] != "col" :
            if tree.conditions[i][1] not in tree.left_child.attributes:
               return "Semantic Error (Select): Left Operand is not a valid column name"
            elif  lIndexDom != tree.conditions[i][3]:
               return "Semantic Error (Select): Data types do not match in comparison"              
         #if the right operand is a col and the left operand is not a col
         elif tree.conditions[i][3] == "col" and tree.conditions[i][0] != "col" : 
            rIndexDom = tree.left_child.domains[tree.left_child.attributes.index(tree.conditions[i][4])] 
            if rIndexDom == 'VARCHAR':
               rIndexDom = 'str'
            elif lIndexDom == "INTEGER":
               rIndexDom = 'num' 
            if tree.conditions[i][4] not in tree.left_child.attributes:
               return "Semantic Error (Select): Right Operand is not a valid column name"
            elif  rIndexDom != tree.conditions[i][1]:
               return "Semantic Error (Select): Data types do not match in comparison"
         
         # if both operands are col 
         elif tree.conditions[i][0] == "col" and tree.conditions[i][3] == "col" :
            lIndexDom = tree.left_child.domains[tree.left_child.attributes.index(tree.conditions[i][1])] 
            rIndexDom = tree.left_child.domains[tree.left_child.attributes.index(tree.conditions[i][4])] 
            if tree.conditions[i][1] not in tree.left_child.attributes:
               return "Semantic Error (Select): Left Operand is not a valid column name"
            elif tree.conditions[i][4] not in tree.left_child.attributes:
               return "Semantic Error (Select): Right Operand is not a valid column name"
            elif (lIndexDom != rIndexDom):
               return "Semantic Error (Select): Data types do not match in comparison"
         i+=1
       tree.attributes = tree.left_child.attributes
       tree.domains = tree.left_child.domains
       return 'OK'  
    #checks for join
    elif tree.node_type == "join":
       mesg1 = semantic_checks(tree.left_child, db)
       if mesg1 != 'OK':
          return mesg1
       mesg2 = semantic_checks(tree.right_child, db)
       if mesg2 != 'OK':
          return mesg2       
       commonAttr = []
       for sAttr in tree.left_child.attributes:
          if sAttr in tree.right_child.attributes:
             commonAttr.append(sAttr)
       for name in commonAttr:   
          if tree.left_child.domains[tree.left_child.attributes.index(name)] != tree.right_child.domains[tree.right_child.attributes.index(name)]:
             return "Semantic Error (Join): Common columns have different data types"
       l = evaluate_query(tree.left_child, db)
       r = evaluate_query(tree.right_child, db)
       tree.attributes =   l.join(r).attributes
       tree.domains = l.join(r).domains
       return 'OK'
    else:
       return "Wierd unknown error"

# This function evaluates the query expressed in the tree and returns the
# Relation object that corresponds to the "root" node in the tree.
def evaluate_query(tree, db):
   # if tree.left_child == None and tree.right_child == None:  # base case
   if tree.node_type == "relation":  # base case
      return db.getRelation(tree.get_relation_name())
   # tree.conditions is the list of conditions for SELECT [(lop,lot,c,rop,rot)..]
   # select[name='John' and age<25](students)
   # Ex: "[('col', 'name', '=', 'str', 'John'), ('col','age','<',num,'25')]"
   elif tree.node_type == "select":
      l = evaluate_query(tree.left_child, db)
      i = 0
      #for each row in tree.conditions
      while i in range(len(tree.conditions)):
         l = l.select(tree.conditions[i][0], tree.conditions[i][1], tree.conditions[i][2], tree.conditions[i][3], tree.conditions[i][4])
         i+=1
      return l
   elif tree.node_type == "project":
      l = evaluate_query(tree.left_child, db)
      s = l.project(tree.columns)
      return s
   elif tree.node_type == "rename":
      l = evaluate_query(tree.left_child, db)
      s = l.rename(tree.columns)
      return s
   elif tree.node_type == "join":
      l = evaluate_query(tree.left_child, db)
      r = evaluate_query(tree.right_child, db)
      s = l.join(r)
      return s
   elif tree.node_type == "union":
      l = evaluate_query(tree.left_child, db)
      r = evaluate_query(tree.right_child, db)
      s = l.union(r)
      return s
   elif tree.node_type == "intersect":
      l = evaluate_query(tree.left_child, db)
      r = evaluate_query(tree.right_child, db)
      s = l.intersect(r)
      return s
   elif tree.node_type == "minus":
      l = evaluate_query(tree.left_child, db)
      r = evaluate_query(tree.right_child, db)
      s = l.minus(r)
      return s
   elif tree.node_type == "times":
      l = evaluate_query(tree.left_child, db)
      r = evaluate_query(tree.right_child, db)
      s = l.times(r)
      return s
   
def main():
  db = Database()
  db.initializeDatabase(sys.argv[1])

  while True:
    data = read_input() 
    if data == 'schema;':
      print(db.displaySchema())
      continue
    if data.strip().split()[0] == "source":
      filename = data.strip().split()[1][:-1]
      execute_file(filename, db)
      continue
    if data == 'help;' or data == "h;":
        print("\nschema; 		# to see schema")
        print("source filename; 	# to run query in file")
        print("exit; or quit; or q; 	# to exit\n")
        continue
    if data == 'exit;' or data == "quit;" or data == "q;":
      break
    try:
      tree = parser.parse(data)
    except Exception as inst:
      print(inst.args[0])
      continue
    #print("********************************")
    #tree.print_tree(0)
    #print("********************************")
    set_temp_table_names(tree)
    msg = semantic_checks(tree,db)
    #print("********************************")
    #tree.print_tree(0)
    #print("********************************")
    if msg == 'OK':
        #print('Passed semantic checks')
        print()
        r = evaluate_query(tree,db)
        r.setName("ANSWER")
        print(r) 
    else:
        print(msg)
if __name__ == '__main__':  
  main()