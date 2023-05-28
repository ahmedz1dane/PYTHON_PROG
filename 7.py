def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            break
            print ("list contains an even number")
    else:
        print ("list does not contain an even number")
            
list = input("Enter the list elements seperated by whitespace: ").split()
print("list is in string format: ", list)
print("\CONVERTING THE LIST INTO A LIST OF INTEGERS.. \n")
for i in range(0, len (list)):
    list [i] = int(list[i])
print ("Integer List: ", list)
print("CHECKING WHETHER THE LIST CONTAINS AN EVEN NUMBER.. In")
contains_even_number(list)
