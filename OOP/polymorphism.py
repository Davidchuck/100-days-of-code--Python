#Existence of an object in more than one form.
#Example 1: Shapes

#case study 1
class circle:
     #constructor
     def __init__(self):
          self.pi=3.142
          self.radius=0

    #method get radius
     def setRadius(self):
          radius= int(input("enter the radius: ", ))
          self.radius=radius
          print("the radius is: ", self.radius)

#form 1 cylinder
class cylinder(circle):
     
     #form
     def render(self):
         # print("This is a cylinder")
          height=int(input("Enter the height"))
          vol=self.pi*self.radius*self.radius*height
          print("volume is ", vol)

#form 2: sphere
class sphere(circle):
     #method
     def render(self):
          #print("This is a sphere")
          surface=(4/3*self.radius*self.radius*self.radius*self.pi)
          print("surface area", surface)

#create object
sphere1 =sphere()
cylinder1=cylinder()

#methods
print(sphere1.setRadius())
print(sphere1.render())
#print(sphere1.surfaceArea())

     
    

