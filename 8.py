class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self) :
        self.x = start
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1;
        return x
start, limit = input("Enter the first and last number to iterarte: ").split()
start = int(start)
limit = int(limit)

if limit >= start:
    for i in Test(limit):
        print (i)
else:
    print("Invalid input! \nNote: last number should be larger than the first number.")
