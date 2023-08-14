#calculating the surface area of a cylinder,
#Formula 2 pi r*r + 2pi dh

print("input the following")

print("enter pi measurement")
pi=float(input())

print("Enter the radius")
r=int(input())

print("Enter the height")
h=int(input())

#SA of a closed cylinder
SA=2*(pi*r*r) + (pi*h*(r+r))
print("The closed surface area is", SA)

