#passing a list as an argument
def my_function(food):
  for x in food:
    print(x)
fruits=["apple", "banana", "cherry"] 
my_function(fruits)
#dictionary
student={
"name":"boeri",
"RegNo":"bcom-01-0043/19",

}
print(student)
#area of a circle
def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
num=float(input("Enter r value:"))
print("Area is %.6f" % findArea(num)); 
#area of a rectangle
def product(l,w):
  a=l*w
  print("the area of the rectangle is",a,)
product(30,10)

def AreaOfRectangle(Length,Width):
  Area=Length*Width
  print("\n Area of a Rectangle is: %.2f" %Area)
Length=float(input("Enter the l value:")) 
Width=float(input("Enter the w value:"))