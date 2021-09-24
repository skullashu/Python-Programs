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

#Checks if string characters is in alphanumeric
a = "My name is Ashriti."
b = a.isalnum()
print(b)

#Checks if string characters is in alphabets
a = "My name is Ashriti."
b = a.isalpha()
print(b)

#Checks if string characters has decimals
a = "\u0030" #unicode for 0
b = a.isdecimal()
print(b)

#Checks if string characters has digits
a = "6754863728"
b = a.isdigit()
print(b)

#Checks for valid identifiers
a = "Demo"
print(a.isidentifier())

#Joining all the items in a string
a = ["My", "name", "is", "Ashriti."]
b = "#".join(a)
print(b)

#Maketrans Method
a = "My name is Ashriti"
b = a.maketrans("riti", "utos")
print(a.translate(b))

#Partition Method
a = "My name is Ashriti"
b = a.partition("is")
print(b)

#Using if statement
a = "My name is Ashriti."
if "Ashriti" in a:
  print("Yes, 'Ashriti' is present")

#Finding last position of a specified character in a string
a = "My name is Ashriti."
b = a.rfind("Ashriti")
print(b)

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

#Swapcase of the string
a = "My name is Ashriti."
b = a.swapcase()
print(b)

#To find a specific value occurs the number of times
a = "My name is Ashriti. I, Ashriti is studying in SHUATS."
b = a.count("Ashriti", "is")
print(b)

#Checks whether the string ends with a particular value
a = "My name is Ashriti."
b = a.endswith("Ashriti.")
print(b)

#Checks whether the string starts with a specific value
a = "My name is Ashriti."
b = a.startswith("Ashriti.")
print(b)

#Expand the string to specific whitespaces
a = "M\ty n\ta\tm\te i\ts A\ts\th\tr\ti\tt\ti."
b = a.expandtabs()
print(b)

#Adding zeroes at the beginning of string
a = "My name is Ashriti."
b = a.zfill(30)
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

#String to list
a = "My name is Ashriti."
print(a.rsplit(","))

#Splitting a string into list where there is a line break
a = "My name is Ashriti.\nI am 22 yrs old."
b = a.splitlines()
print(b)

#Returns left justified version of the string
a = "My name is Ashriti."
b = a.ljust(30, "O")
print(b)

#Returns right justified version of the string
a = "My name is Ashriti."
b = a.rjust(30, "O")
print(b)

#Removes left characters of a string
a = ",,..,.,.,.00000My name is Ashriti."
b = a.lstrip(",.0")
print(b)

#Removes trailing characters of a string
a = "My name is Ashriti.,.,.,.,.,.,000000"
b = a.rstrip(",.0")
print(b)

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

#Adds an element at the specified position
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

#Reverses the order of the list
L1 = ["My","name","is","Ashriti"]
L1.reverse()
print(L1)

#Sorts the list
L1 = ["My","name","is","Ashriti"]
L1.sort()
print(L1)

