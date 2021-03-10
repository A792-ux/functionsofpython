def my_function():
  print('Hello, world!How was your day hombres')
my_function()

def sum(x,y):
  a=x+y
  print("The sum is",a)
sum(400,550)
sum(230,33)
sum(501,958)


def sum(x, y):
  a=x+y
  return a
print(sum(10,20))

def product(a,b):
  c=a*b
  print("the product is",c)
product(30,4)

def quotient(x,y):
  a=x/y
  print("the quotient is",a)
quotient(100,4)
#arguments
def courses(*args):
  for subject in args:
    print(subject)
courses("Big Data", "CCNA", "OOP2", "Sotfware Engineering")  
def courses(*args):
  for subject in args:
    return subject
print(courses("Economics", "Business", "Accountancy"))
#keyword arguments
def courses(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}" .format(key,value))
courses(first="Big Data",second="CCNA",third="HCIA")
#default parameter value
def kenya(county=" Siaya"):
  print("I am from" + county)
kenya()
kenya(" Nairobi")
kenya(" Kiambu")
kenya(" Kisumu")
