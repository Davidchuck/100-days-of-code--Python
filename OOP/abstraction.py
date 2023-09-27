#drawing abstract class for shapes
#then use the information to build real classes
class Shape:
    def __init__(self):
        self.name=""


    #Method
    def perimeter(self):
        #statements here
        pass

    #Method 2
    def area(self):
        #statements
        pass
    #Method 3 print statement

    def fact():
        #statement
        pass

#Real class
class circle(Shape):
    def __init__(self):
        self.name=""
        self.radius=0
        #self.pi=3.142
    #Method 1
    def perimeter_circle(self):
        radius=int(input("Enter the radius: ",))
        self.radius=radius
        perimeter=3.142*(self.radius*2)
        print(perimeter)

    #method 2
    def area_circle (self):
        radius=int(input("Enter the radius: ",))
        self.radius=radius
        area = 3.142 * ((self.radius)**2)
        print ("The Area of Circle is",area,"sq units")
    
    #method 3
    def fact(self):
        name=input("Enter the shape name")
        self.name=name
        print("The shapeis a", self.name)

#shape 2: Rectangle
class rectangle(Shape):
    def __init__ (self):
        self.name=""
        self.length=0
        self.width=0
    
    #Method
    def perimeter_rectangle (self):
        len=int(input("Enter the length"))
        wid=int(input("Enter the Width"))
        self.length=len
        self.width=wid
        perimeter_r=2*(self.length+self.width)
        print('Perimeter:',perimeter_r)

    #method 2
    def area_rectangle (self):
        len=int(input("Enter the length"))
        wid=int(input("Enter the Width"))
        self.length=len
        self.width=wid
        area_r=self.length+self.width
        print('Area:',area_r)

     #method 3
    def r_fact(self):
        name_r=input("Enter the shape name")
        self.name=name_r
        print("The shapeis a", self.name)
        
#create object

rect= rectangle()
circ= circle ()

#call the methods
print(circ.fact)
print(circ.perimeter_circle)
