print("hello world")
a=12
b=78
c=4
temp=a
a=b
b=c
c=temp
print(a)
print(b)
print(c)
name="BHAGYASHREE"
# print(name)
a=input("enter the value:")
print(a)
b="5"
print(b)
print(type(a))
print(type(b))
a=int(input("enter the value"))
print(a)
b=float(input("enter the value"))
print(b)
print(type(a))
print(type(b))
c=complex (input("enter the value"))
print(c)
print(type(c))
name=("bhagya","patil",35,67)
print(name)
ages=[56,367,8,98]
print(ages)
print(type(name))
print(type(ages))
books={
    'bookname':'maxin',
    'published':'1997'
}
print(books)
print(type(books))
a=int(input("enter the value:"))
if a>=18:
 print("yoyu sre eligible to vote")
b=int(input("enter the vslue:"))
if b%2==0:
    print("the number is even")
else:
    print("the number is odd")
a=int(input("enter the value:"))
if a>=90:
    print("first class")
elif a>=80:
    print("second class")
else:
    print("third class")
name=str(input("enter the name:"))
age=int(input("|enter the age:"))
if name=="_":
    print("you are not entered the name,please re enter the name")
elif age>=18:
    print("you are eligible to booking the ticket")
else:
    print("not eligible")