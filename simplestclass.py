#!/usr/bin/python
# Filename: simplestclass.py

class Person:
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print 'Hello,how are you?',self.name

p = Person('Swaroop')
p.sayHi()

#Person('zhai').sayHi()
