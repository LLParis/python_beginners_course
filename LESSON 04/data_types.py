# string data type

# literal assignment
first = "London"
last = "Paris"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
full_name = first + " " + last

print(full_name)

full_name += "!"
print(full_name)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the" + decade + "s."

# multiple lines
multiline = '''
Hey, how are you?    

I was just checking in.   

                                All good?

'''
print(multiline)

# escaping special characters
sentence = "I\"m back at work!\tHey!\n\nWhere\'s this at\\located?"
print(sentence)

# string methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                      "
multiline = "                            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print()
print()

# build a menu

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print()

# string index values
print(first[0])
print(first[-1])
print(first[0:-1])
print(first[0:])

# some methods return boolean data

print(first.startswith("L"))
print(first.endswith("n"))

# boolean data type needs to be proper case
my_value = True

x = bool(False)
print(type(x))
print(isinstance(my_value, bool))


# numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))






