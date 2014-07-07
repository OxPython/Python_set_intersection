'''
Created on Jul 7, 2014

@author: root

How to get the common items from two sets in Python?

¿Cómo obtener los elementos comunes de dos sets en Python?

intersection(other, ...)
set & other & ...
Return a new set with elements common to the set and all others.
'''

#Create a set with values.
s = set([0,1,2,3])
print(s)

s2 = {1,6}
print(s2)

#get the common items
i = s.intersection(s2)
print(i)

#If there are not common items return empty set
#get the common items
s3 = {4,5}
i = s.intersection(s3)
print(i)

#You can use "&"
i = s & s2
print(i)