class Triangle:
    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse

    def calculate_area(self):
        #s = (self.a + self.b + self.c) / 2
        area = 0.5*((self.base))* self.height
        return area

    def calculate_perimeter(self):
        perimeter = self.base + self.height + self.hypotenuse
        return perimeter

class Pyramid:
    def __init__(self, base_triangle, pheight):
        self.base_triangle = base_triangle
        self.pheight = pheight

    def calculate_volume(self):
        base_area = self.base_triangle.calculate_area()
        volume = (1/3) * base_area * self.pheight
        return volume

    def calculate_surface_area(self):
        base_perimeter = self.base_triangle.calculate_perimeter()
        base_area = self.base_triangle.calculate_area()
        side_area = 0.5 * base_perimeter * self.pheight
        total_surface_area = base_area + side_area
        return total_surface_area

# Input the sides of the triangle
side_a = float(input("Enter the base: "))
side_b = float(input("Enter the Height: "))
side_c = float(input("Enter the Hypotenuse: "))

# Input the height of the pyramid
pyramid_height = float(input("Enter the height of the pyramid: "))

# Create a Triangle object
triangle = Triangle(side_a, side_b, side_c)

# Create a Pyramid object with the base triangle and height
pyramid = Pyramid(Triangle, pyramid_height)

# Calculate and display the results
print("Triangle Area:", triangle.calculate_area())
print("Triangle Perimeter:", triangle.calculate_perimeter())
print("Pyramid Volume:", pyramid.calculate_volume())
print("Pyramid Surface Area:", pyramid.calculate_surface_area())