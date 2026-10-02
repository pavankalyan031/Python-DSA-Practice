# def add(a,b):
#     return a+b
# ans=add(2,3)
# print(ans)

def one():
    print("One Start")
    two()
    print("One End")


def two():
    print("Two Start")
    three()
    print("Two End")


def three():
    print("Three")


one()