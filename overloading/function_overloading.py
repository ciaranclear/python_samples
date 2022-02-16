from multipledispatch import dispatch

#passing one parameter
@dispatch(int,int)
def product(first, second):
    result = first*second
    print(result)

#passing two parameters
@dispatch(int,int,int)
def product(first, second , third):
    result = first*second*third
    print(result)

#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first, second, third):
    result = first*second*third
    print(result)

#calling product method with 2 arguments
product(2,3,2) #this will give output of 12
product(2.2,3.4,2.3) #this will give output of 17.98599

from functools import singledispatch

@singledispatch
def fun(s):
    print(s)

@fun.register(int)
def _(s):
    print(s * 2)

@fun.register(list)
def _(s):
    for i, e in enumerate(s):
        print(i, e)

fun("GeeksforGeeks")
fun(10)
fun(['g','e','e','k','s'])

from decimal import Decimal

@singledispatch
def fun(s):
    print(s)

@fun.register(float)
@fun.register(Decimal)
def _(s):
    print(round(s, 2))

fun(2.34)
fun(Decimal(4.987))

from datetime import datetime, date, time

@singledispatch
def format(arg):
    return arg

@format.register
def _(arg: date):
    return f"{arg.day}-{arg.month}-{arg.year}"

@format.register
def _(arg: datetime):
    return f"{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}:{arg.second}"

@format.register(time)
def _(arg):
    return f"{arg.hour}:{arg.minute}:{arg.second}"

print(format("Today"))

print(format(date(2021, 5, 26)))

print(format(datetime(2021, 5, 26, 17, 25, 10)))

print(format(time(19, 22, 15)))


from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    def format(self, arg):
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")

    @format.register
    def _(self, arg: date):
        return f"{arg.day}-{arg.month}-{arg.year}"

    @format.register
    def _(self, arg: time):
        return f"{arg.hour}:{arg.minute}:{arg.second}"


f = Formatter()
print(f.format(date(2021, 5, 26)))

print(f.format(time(19, 22, 15)))


@dispatch((list, tuple), (str, int))
def concatenate(a, b):
    return list(a) + [b]

print(concatenate(["a", "b"], "c"))
# ['a', 'b', 'c']
print(concatenate(("a", "b"), 1))
# ['a', 'b', 1]

@singledispatch
def myFun(*args):
    print(f"default for myFun {args}")

@myFun.register
def _(a: int, *args):
    print(f"myFun int {args}")

@myFun.register
def _(a: float, *args):
    print(f"myFun float {args}")

a = ['a','b','c']
myFun(a[0], a)

b = [1,2,3,4,5]
myFun(b[0], b)

c = [1.0,2.0,3.5,4.7]
myFun(c[0], c)

myFun(9, 8, 7, 6, 5)

from typing import Any

def bigFunc(a: int) -> Any:
    if(a == 1):
        return 1
    elif(a == 2):
        return 2.0
    elif(a == 3):
        return "3"
    else:
        return"None"

print(bigFunc(1))
print(bigFunc(2))
print(bigFunc(3))
print(bigFunc(4))


