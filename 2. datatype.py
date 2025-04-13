#DATATYPES
# String: "This is Priya" 
# Integer: 1, 23
# Float: 2.2, 43.3

print ("This is priya")
print(123)
print(2.2)
print("priya22206")

# Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry", 1, True ]
print(mylist)
emp = ["Priya", 1, "India", 111105.7 ]
print(emp)
print(emp[2])

# A tuple is a collection which is ordered and unchangeable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[1])

# A set is a collection which is unordered, unchangeable*, and unindexed.
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
for x in thisset:
  print(x)

# Dictionaries are used to store data values in key:value pairs.
thisdict = {
  "brand": "TATA",
  "model": "Punch",
  "year": 2022
}
print(thisdict)
x = thisdict["model"] #Punch
print(x)