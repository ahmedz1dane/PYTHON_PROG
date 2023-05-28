lower_bound = int(input("Enter the starting element of the series: "))
upper_bound = int(input("Enter the ending element of the series: "))
step_count = int(input("Enter the step count value: "))


series = [*range(lower_bound, upper_bound, step_count)]
print("Series: ", series)


sum=0


for i in range(len(series)):
    sum = sum + series[i]


print("The sum of series {2} of length {0} is {1}".format(len(series), sum, series))
