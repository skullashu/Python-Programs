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

#Lower Case
a = "My name is Ashriti."
print(a.lower())

#Remove Whitespace
a = "  My name is Ashriti. "
print(a.strip())

#Replace String
a = "My name is Ashriti."
print(a.replace("Ashriti", "Ashu"))

#Split String
a = "My name is Ashriti."
print(a.split(","))

