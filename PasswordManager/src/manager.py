#!/usr/bin/env python

from records import Data
import getpass

class Manager :
	
	def load(self, xmlFileName):
		doc = etree.parse(xmlFileName)
		print doc
		print doc.find('data')
		
	
	def __init__(self) :
		self.store = []		
	
	def enter(self) : 
		acc = raw_input(">> Enter account name : ")
		usr = raw_input(">> Enter username/loginID : ")
		pwd = getpass.getpass(">> Enter password : ")
		inp = raw_input(">> Enter y if you want to enter more info? ")
		data = Data(acc, usr, pwd)

		if inp == 'y' :
			details = raw_input(">> Enter details : ")
			data.addMoreDetails(details)
		self.add(data)

	def add(self, dataObject) :
		self.store.append(dataObject)
	
	def find(self, account) :
		for aDataObject in self.store : 
			if aDataObject.id == account :
				return aDataObject
	
	def printAll(self) :
		for aDataObject in self.store : 
			aDataObject.printMe()
 
	def edit(self) : 
		account = raw_input("Enter the account name to edit : ")
		dataObj = self.find(account)
		self.store.remove(dataObj)
		print "Please ree-enter all details for "+account
		self.enter()
		
	def destroy(self) :
		if raw_input(">> Enter y if you really want to delete all your data : ") == 'y' :
			del self.store[:] 
		else : 
			print(">> Delete operation cancelled ....")
			

		
		
	

