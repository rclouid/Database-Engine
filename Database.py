from Relation import *
from Tuple import *
class Database:

	def __init__(self):
		self.relations = {}

	# Add relation r to Dictionary if relation does not already exists.
	# return True on successful add; False otherwise
	def addRelation(self,r):
		if r.name not in self.relations:
			self.relations[r.name] = r 
			return True
		return False


	# Delete relation with name rname from Dictionary if relation exists. 
	# return True on successful delete; False otherwise
	def deleteRelation(self,rname):
		deletedRelation = self.relations.pop(rname)
		if( deletedRelation == rname):
			return True
		return False

	# Retrieve and return relation with name rname from Dictionary.
	# return None if it does not exist.
	def getRelation(self, rname):
		return self.relations.get(rname)
	
	# Create the database object by reading data from several files in directory dir
	def initializeDatabase(self, dir):
		f1 = open("./" + dir + "/catalog.dat","r")
		nrels = int(f1.readline().strip())
		for i in range(nrels):
			rname = f1.readline().strip()
			natrributes = int(f1.readline())
			attributes = []
			domains = []
			for j  in range(natrributes):
				aname = f1.readline().strip()
				adom = f1.readline().strip()
				attributes.append(aname)
				domains.append(adom)
			rel = Relation(rname,attributes,domains)	
			f2 = open("./" + dir + "/" + rname + ".dat","r")
			nTuples = int(f2.readline().strip())
			for k in range(nTuples):
				tup = Tuple(attributes, domains)
				for l in range(len(attributes)):
					comp = f2.readline().strip()
					if domains[l] == "INTEGER":
						comp = int(comp)
					elif domains[l] == "DECIMAL":
						comp = float(comp)	
					else:
						pass
					tup.addComponent(comp)
				rel.addTuple(tup)
			f2.close()
			self.addRelation(rel)
		f1.close()
		
	# Return database schema as a String
	def displaySchema(self):
		str = "\n"
		for rname in self.relations:
			rel = self.getRelation(rname)
			str = str + rel.displaySchema() + "\n"  
		return str 
		

