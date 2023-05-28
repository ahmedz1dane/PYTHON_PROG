l = []
print("CREATING LIST..")
a, b, c, d = [int(i) for i in input("Enter 4 values to insert in the list: ").split()]
print("ADDING ELEMENTS INTO THE LIST..")
l.append(a)
l.append(b)
l.append(c)
l.append(d)
print("After adding {0}, {1}, {2}, and {3} in the list: ".format(a, b, c, d),l)
print("length of the list is ", len(l))
print()
l.pop()
print("POPPING AN ELEMENT FROM THE LIST..")
print("Popped one element from list: ",l)
print("length of the list is ",len(l))
print()

s = set()
print("CREATING SET..")
s.add(a)
s.add(b)
s.add(c)
s.add(d)
print("Adding inputs {0}, {1}, {2}, and {3} to the set: ".format(a, b, c, d), s)
s.remove(b)
print("Removing {0} from the set: ".format(b), s)
print()

t = tuple(l)
print("CREATING TUPLE FROM THE LIST..")
print("Tuple: ", t)
print("Tuples are immutable so no operations can be performed on it.")
print()


d = {}
print("CREATING DICTIONARY..")
d['20MCA27'] = 'ADA LAB'
d['20MCA28'] = 'PYTHON LAB'
d['20MCA29'] = 'WEB LAB'
print("Dictonary: ", d)
ele = d['20MCA27']
del d['20MCA27']
print("Removing {0} from the dictionary: ".format(ele), d)
