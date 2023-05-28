import matplotlib.pyplot as plt

lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
print("Enter the popularity of the following programming languages:")
print("1. Java \n2. Python \n3. PHP \n4. Javascript\n5. C#, and \n6. C++ ")
print("(Make sure that the sum of all values should be 100)")

popularity=[]
for i in lang:
    popularity.append(float(input (i+":")))
    
print("\n\n1. Plot Bar Chart \n2. Plot Pie Chart")
choice = int(input("Enter your choice:"))

if choice == 1:
    lang_pos = [i for i, _ in enumerate(lang)]
    plt.bar(lang_pos, popularity, color="blue")
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("Popularity of Programming Languages\n")
    plt.xticks(lang_pos, lang)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color="red")
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()
elif choice == 2:
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    explode = (0.1, 0, 0, 0,0,0)
    plt.pie(popularity, explode=explode, labels=lang, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
else:
    print("invalid input!")
