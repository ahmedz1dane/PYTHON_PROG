def file_read(fname):
    txt = open(fname)
    print(txt.read())

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)

def file_read(fname):
    with open(fname) as f:
        content_list = f.readlines()
        print(content_list)

def longest_word(filename):
    with open (filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

def file_lengthy(fname):
    with open(fname) as f:
        for i, I in enumerate(f) :
            pass
    return i + 1

from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

print("1. Read contents of a file")
print("2. Read first and last lines of a file")
print("3. Read line by line and store in a list")
print("4. Find the longest word in a file")
print("5. Count the number of lines in a file")
print("6. Count the frequency of a word")
print("7. Read a random line in a file")
choice=int(input("Enter your choice:"))

if choice == 1:
    print("Reading text file..")
    file_read('MyTextFile.txt')
elif choice == 2:
    print("Reading first and last lines of a file..")
    file_read_from_head('MyTextFile.txt',2)
elif choice == 3:
    print("Reading line by line and store in a list..")
    file_read('MyTextFile.txt')
elif choice ==4:
    print("Finding the longest word..")
    print(longest_word('MyTextFile.txt'))
elif choice == 5:
    print("Counting the number of lines...")
    print("Number of lines in the file: ",file_lengthy("MyTextFile.txt"))
elif choice ==6:
    print("Counting the frequency of word..")
    print("Number of words in the file :",word_count("MyTextFile.txt"))
elif choice ==7:
    print("Reading a random line..")
    print(random_line('MyTextFile.txt'))
else:
    print("Invalid choice!")
