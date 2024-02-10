from Tuple import *
class Relation: 

	def __init__(self,name,attributes,domains):
		self.name = name.upper() # name of relation
		self.attributes = [a.upper() for a in attributes] # list of names of attributes
		self.domains = [d.upper() for d in domains] # list of "INTEGER", "DECIMAL", "VARCHAR"
		self.table = [] # list of tuple objects

	# Returns True if attribute with name aname exists in relation schema;
	# False otherwise
	def attribute_exists(self, aname):
		return aname not in self.attributes

	# Returns attribute domain of attribute aname; return None if not present
	def attribute_type(self, aname):
		index = self.attributes.find(aname)
		if index >= 0:
			return self.domains[index]
		return None

	# Get name of relation to rname
	def getName(self):
		return self.name 
	# Set name of relation to rname
	def setName(self, rname):
		self.name = rname
	def getDomains(self):
		return self.domains
	def getAttributes(self):
		return self.attributes
	def setAttributes(self, attr):
		self.attributes = attr

	# Add tuple tup to relation; Duplicates are fine.
	def addTuple(self,tup):
		self.table.append(tup)

	# Remove duplicate tuples from this relation
	def removeDuplicates(self):
		for component in self.table:
			i = self.table.index(component) + 1
			while i < len(self.table):
				if component.equals(self.table[i]):  
					self.table.pop(i)
					i = i - 1
				i = i + 1
	#This method returns True if tuple t is present in relation and False otherwise.
	def member(self, t):
		for tup in self.table:
			if(tup.equals(t)):
				return True
		return False
	
	#This method returns the union of two relations (self and r2); It should remove duplicates before returning. Clone the tuples from the input
	def union(self, r2):
		unionRel = Relation(self.name, self.attributes, self.domains)
		for tup in self.table: 
			tup.setDomains(self.domains)
			unionRel.addTuple(tup.clone(self.attributes))
		for tup in r2.table: 
			tup.setDomains(self.domains)
			unionRel.addTuple(tup.clone(self.attributes))
		unionRel.removeDuplicates()
		return unionRel
	
	#This method returns the intersection of two relations (self and r2); Clone the tuples from the input relations and then add to output.
	def intersect(self, r2):
		interRel = Relation(self.name, self.attributes, self.domains)
		for tup in r2.table: 
			if self.member(tup):
				interRel.addTuple(tup.clone(self.attributes))
		interRel.removeDuplicates()
		return interRel
	
	#This method returns the difference of two relations (self and r2); Clone the tuples from the input relations and then add to output.
	def minus(self,r2):
		minusRel = Relation(self.name, self.attributes, self.domains)
		for tup in self.table: 
			if not(r2.member(tup)):
				minusRel.addTuple(tup.clone(self.attributes))		
		minusRel.removeDuplicates()
		return minusRel
	
	## The rename method takes as parameter an array list of new column names, cnames, 
	## and returns a new relation object that contains the same set of tuples, but with
	## new columns names. We can assume that the size of cnames is same as size of this.attributes
	def rename(self,cnames):
		attrs = []
		doms = []
		for i in cnames: attrs.append(i)
		for j in self.domains: doms.append(j)
		rel = Relation(self.name,attrs,doms)
		for tup in self.table: rel.addTuple(tup.clone(attrs))
		return rel
	
	## The times method returns the cartesian product of two relations.
	## As an example, let R and S be the following two relations:
	## R(A:VARCHAR, B:INTEGER, C:INTEGER) and S(B:INTEGER, C:INTEGER, D:DECIMAL)
	## and let R contain the tuples {<jones",20,200>, <smith",30,300> and
	## let S contian the tuples {<1,2,2.5>, <100,200,3.86>}
	## The R times S would have the schema 
	## R_TIMES_S(A:VARCHAR, R.B:INTEGER, R.C:INTEGER, S.B:INTEGER, S.C:INTEGER, D:DECIMAL)
	## and the tuples: {<jones",20,200,1,2,2.5>, <jones",20,200,100,200,3.86>,
	##                  <smith",30,300,1,2,2.5>, <smith",30,300,100,200,3.86>}
	## Notice the tuples in the output are formed by combining tuples in the
	## input relations in all possible ways, maintaining the order of columns
	def times(self,r2):
		attrs = []
		doms = []
		for name in self.attributes: 
			if name in r2.attributes:
				attrs.append(self.getName() + "." + name)
			else:
				attrs.append(name)	
		for i in self.domains: doms.append(i)		
		for name in r2.attributes:
			if name in self.attributes:
				attrs.append(r2.getName() + "." + name)
			else:
				attrs.append(name)	
		for i in r2.domains: doms.append(i)		
		rel = Relation(self.getName(), attrs, doms)	
		for t1 in self.table:
			for t2 in r2.table:
				rel.addTuple(t1.concatenate(t2, attrs, doms))
		return rel

	## This methods takes as input a list of column names, each of which
	## belonging to self.attributes, and returns a relation whose tuples are
	## formed by projecting the columns from cnames.
	## Example: R(A:INTEGER, B:INTEGER, C:DECIMAL) with tuples
	## {(10,20,3.5),(11,22,7.8),(10,25,3.5)}
	## Then, with cnames = {A,C}, the output relation should
	## have schema (A:INTEGER, C:DECIMAL) and tuples
	## {(10,3.5),(11,7.8)}
	## Note that after projection one may get duplicate tuples, which should
	## be removed.
	def project(self, cnames):
		doms = []
		for colname in cnames: 
			for cName in self.attributes:
				if(cName == colname):
					doms.append(self.domains[self.attributes.index(cName)])
		rel = Relation(self.getName(), cnames, doms)
		for tuple in self.table:
			tup = tuple.project(cnames)
			rel.addTuple(tup)
		rel.removeDuplicates()
		return rel
	
	# This method takes as input a comparison condition as explained earlier and returns
	# a new relation that contains only those tuples that satisfies the comparison condition.
	def select(self,lopType,lopValue,comparison,ropType,ropValue):
		rel = Relation(self.getName(), self.attributes, self.domains)
		for tup in self.table:
			if tup.select(lopType,lopValue,comparison,ropType,ropValue):
				rel.addTuple(tup)				
		return rel		
	
	## The join operator combines two relations into one based on common columns in the two relations
  	## The schema of the join relation contains all columns of the first relation followed by all columns
  	## of the second relation, somewhat like the times operator, except that the common columns appear only
  	## once in the join relation (keep first occurrence)
  	## Two tuples join with each other only if they have the same values under the common columns.
	def join(self,r2):
		attr = self.attributes
		dom = self.domains
		for i in r2.attributes:
			if i not in attr:
				attr.append(i)
				dom.append(r2.domains[r2.attributes.index(i)])
		rel = Relation(self.getName(), attr, dom)
		for tup in self.table:
			for tup2 in r2.table:
				joinTup = tup.join(tup2)
				if joinTup != None:
					rel.addTuple(joinTup)
		return rel

    # Return relation schema as String
	def displaySchema(self):
		str = self.getName() + '('      
		i = 0
		for x in self.attributes:
			str = str + x + ":" + self.domains[i] 
			if self.attributes.index(x) != len(self.attributes) - 1:
				str = str + ","
			else:
				str = str + ")"
			i += 1
		return str
	
	# Return String version of relation; See output of run for format.
	def __str__(self):
		str1 = "\nNumber of tuples:" + str(len(self.table)) + "\n\n" 
		for tup in self.table:
			str1 = str1 + str(tup) + "\n"    	
		return self.displaySchema() +  str1 + "\n"	 
