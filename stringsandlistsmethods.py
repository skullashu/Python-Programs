#Declaring a string
print("Hello, World!")

#Assign String to a Variable
a = "Hello, sir!"
print(a)

#Multiline Strings
a = """He could not help himself in this situation.
He must have to recover from this situation for his bright future."""
print(a)

Or,
a = '''He could not help himself in this situation.
He must have to recover from this situation for his bright future.'''
print(a)

#Strings are Arrays
a = "My name is Ashriti."
print(a[1])

#Looping Through a String
for x in "Ashriti":
  print(x)

#String Length
a = "Ashriti."
print(len(a))

#Check String
a = "My name is Ashriti."
print("Ashriti" in a)

#Using if statement
a = "My name is Ashriti."
if "Ashriti" in a:
  print("Yes, 'Ashriti' is present")

#Slicing Strings
a = "My name is Ashriti."
print(a[3:9])

#Slice From the Start
a = "My name is Ashriti."
print(a[:9])

#Slice To the End
a = "My name is Ashriti."
print(a[3:])

#Negative Indexing
a = "My name is Ashriti."
print(a[-3:-9])

#Modify Strings
#Upper Case
a = "My name is Ashriti."
print(a.upper())

Or,
a = "My name is Ashriti."
b = a.capitalize()
print(b)

#Lower Case
a = "My name is Ashriti."
print(a.lower())

Or,
a = "My name is Ashriti."
b = a.casefold()
print(b)

#Centered String
a = "My name is Ashriti."
b = a.centre(30)
print(b)

Or,
a = "My name is Ashriti."
b = a.centre(30,"0")
print(b)


#Remove Whitespace
a = "  My name is Ashriti. "
print(a.strip())

#Replace String
a = "My name is Ashriti."
print(a.replace("Ashriti", "Ashu"))

#Split String
a = "My name is Ashriti."
print(a.split(","))

#String Concatenation
a = "My name "
b = "is Ashriti."
c = a+b
print(c)

#Adding space between two strings
a = "My name"
b = "is Ashriti."
c = a+" "+b
print(c)

#String Format
b = "is Ashriti."
a = "My name "+b
print(a)

Or,
b = "is Ashriti."
a = "My name {}"
print(a.format(b))



#Declaring a list
L1 = ["My","name","is","Ashriti"]
print(L1)

Or,
L1 = list(("My","name","is","Ashriti"))
print(L1)

#List Length
L1 = ["My","name","is","Ashriti"]
print(len(L1))

#Add an element at the end of the list
L1 = ["My","name","is"]
L1.append("Ashriti")
print(L1)

#Removes all the elements from the list
L1 = ["My","name","is","Ashriti"]
L1.clear()
print(L1)

#Makes a copy of the list
L1 = ["My","name","is","Ashriti"]
x = L1.copy()
print(x)

#Gives the number of elements with specified value
L1 = ["My","name","is","Ashriti"]
x = L1.count("Ashriti")
print(x)

#Adding elements of a list to the current list
L1 = ["My","name","is"]
L2 = ["Ashriti"]
L1.extend(L2)
print(L1)

#Returns the index of the first element with the specified value
L1 = ["My","name","is","Ashriti"]
x = L1.index("Ashriti")
print(x)

#	Adds an element at the specified position
L1 = ["My","name","is"]
L1.insert(3,"Ashriti")
print(L1)

#Removes the element at the specified position
L1 = ["My","name","is","Ashriti"]
L1.pop(2)
print(L1)

#Removes the item with the specified value
L1 = ["My","name","is","Ashriti"]
L1.remove("Ashriti")
print(L1)

#	Reverses the order of the list
L1 = ["My","name","is","Ashriti"]
L1.reverse()
print(L1)

#Sorts the list
L1 = ["My","name","is","Ashriti"]
L1.sort()
print(L1)

