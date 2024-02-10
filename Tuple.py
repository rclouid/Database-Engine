class Tuple:
	def __init__(self,attributes,domains):
		self.attributes = [a.upper() for a in attributes]
		self.domains = [d.upper() for d in domains]
		self.tuple = []

	def setAttributes(self, attr):
		self.attributes = attr
	def setDomains(self, domains):
		self.domains = domains
	# Add a tuple component to the end of the tuple
	def addComponent(self, comp):
		self.tuple.append(comp)

	# Return True if this tuple is equal to compareTuple; False otherwise
	# make sure the schemas are the same; return False if schema's are not same
	def equals(self, compareTuple):
		if(len(self.attributes) != len(compareTuple.attributes)):
			return False
		i = 0
		for type in self.domains:
			if type != compareTuple.domains[i]:
				return False
			i+= 1
		i = 0	
		for component in self.tuple:
			if component != compareTuple.tuple[i]:
				return False
			i += 1
		return True	
	
	## This method combines two tuples into one and assigns a new schema to the 
	## result tuple; the method returns the new tuple
	## e.g. t1 = <"jones",20,200> and t2=<1,2,2.5>
	## then t1.concatenate(t2,attr,dom) will be <"jones",20,200,1,2,2.5>
	## with schema attr = <A, R.B, R.C, S.B, S.C, D>
	## and dom = <VARCHAR,INTEGER,INTEGER,INTEGER,INTEGER,DECIMAL>
	def concatenate(self, t, attrs, doms):
		tup = Tuple(attrs,doms)
		for comp in self.tuple:
			tup.addComponent(comp)
		for comp in t.tuple:
			tup.addComponent(comp)	
		return tup	
	
	#This method creates a new copy of the tuple with the attributes set to attr and returns it.	
	def clone(self, attr):
		cloneTup = Tuple(attr,self.domains)
		for comp in self.tuple: cloneTup.tuple.append(comp)
		return cloneTup
	
	## This method takes as input a list of column names, each of which
	## belonging to self.attributes, and returns a new tuple with only those
	## components that correspond to the column names in cnames.
	## self is a tuple object
	def project(self, cnames):
		doms = []
		for colname in cnames: 
			for cName in self.attributes:
				if(colname == cName):
					doms.append(self.domains[self.attributes.index(cName)]) 
		tup = Tuple(cnames, doms)
		for colname in cnames:
			tup.addComponent(self.tuple[self.attributes.index(colname)])
		return tup
	
  	# lopType="col" and ropType="num"
  	# lopType="col" and ropType="str"
	# lopType="col" and ropType="col"
	# lopType="num" and ropType="num"
  	# lopType="num" and ropType="col"
	# lopType="str" and ropType="str"
  	# lopType="str" and ropType="col"
	def select(self,lopType,lopValue,comparison,ropType,ropValue):	
		if comparison == "=":
			comparison = "=="
		elif comparison == "<>":
			comparison = "!="
		if lopType == "col":
			colIndex = self.attributes.index(lopValue)   #index of the left column name
			if ropType == "num":
				return eval(str(self.tuple[colIndex])  + comparison + str(ropValue)) 
			elif ropType == "str":
				if comparison == "<":
					return self.tuple[colIndex] < ropValue
				elif comparison == "<=":
					return self.tuple[colIndex] <= ropValue
				elif comparison == "==":
					return self.tuple[colIndex] == ropValue
				elif comparison == ">":
					return self.tuple[colIndex] > ropValue
				elif comparison == ">=":
					return self.tuple[colIndex] >= ropValue
				elif comparison == "!=":
					return self.tuple[colIndex] != ropValue
			elif ropType == "col":   #comparing values at left and right columns
				rColIndex = self.attributes.index(ropValue)   #index of the right column name
				if comparison == "<":
					return self.tuple[colIndex] < self.tuple[rColIndex]
				elif comparison == "<=":
					return self.tuple[colIndex] <= self.tuple[rColIndex]
				elif comparison == "==":
					return self.tuple[colIndex] == self.tuple[rColIndex]
				elif comparison == ">":
					return self.tuple[colIndex] > self.tuple[rColIndex]
				elif comparison == ">=":
					return self.tuple[colIndex] >= self.tuple[rColIndex]
				elif comparison == "!=":
					return self.tuple[colIndex] != self.tuple[rColIndex]
		elif lopType == "num":
			if ropType == "num":
				return eval(str(lopType) + comparison + str(ropValue)) 
			if ropType == "col":
				colIndex = self.attributes.index(ropValue)   #index of the column name
				return eval(str(lopType) + comparison + str(self.tuple[colIndex])) 
		elif lopType == "str":
			if ropType == "str":
				if comparison == "<":
					return lopValue < ropValue
				elif comparison == "<=":
					return lopValue <= ropValue
				elif comparison == "==":
					return lopValue == ropValue
				elif comparison == ">":
					return lopValue > ropValue
				elif comparison == ">=":
					return lopValue >= ropValue
				elif comparison == "!=":
					return lopValue != ropValue
			elif ropType == "col": #comparing str to the tuple at the index of the column name
				colIndex = self.attributes.index(ropValue)   #index of the column name
				if comparison == "<":
					return lopValue < self.tuple[colIndex]
				elif comparison == "<=":
					return lopValue <= self.tuple[colIndex]
				elif comparison == "==":
					return lopValue == self.tuple[colIndex]
				elif comparison == ">":
					return lopValue > self.tuple[colIndex]
				elif comparison == ">=":
					return lopValue >= self.tuple[colIndex]
				elif comparison == "!=":
					return lopValue != self.tuple[colIndex] 
	
	## collect information about "common" attributes and their positions in the respective lists.
    ## Verify if the two tuples can join; if not return None
    ## If tuples can join then produce the joined tuple and return it.
	def join(self,t2):
		commonAttr = []
		for sAttr in self.attributes:
			if sAttr in t2.attributes:
				commonAttr.append(sAttr)
		if len(commonAttr) == 0:  #if there is no common element
			return None	
		t2Clone = t2.clone(t2.attributes)
		for common in commonAttr:
			sIndex = self.attributes.index(common)
			t2Index = t2.attributes.index(common)
			if self.tuple[sIndex] == t2.tuple[t2Index]:
				t2Clone.attributes.remove(common)
				t2Clone.domains.pop(t2Index) 
				t2Clone.tuple.pop(t2Index) #remove it at the index of common in tuple, t2Clone
			else:
				return None		
		newAttr = self.attributes + t2Clone.attributes
		newDom = self.domains + t2Clone.attributes	
		joinedTup = self.concatenate(t2Clone,newAttr,newDom)
		return joinedTup 	
		
	# Return String representation of tuple; See output of run for format.
	def  __str__(self):
		str1 = ""
		for comp in self.tuple:
			str1 = str1 + str(comp)+ ":"	
		return  str1



