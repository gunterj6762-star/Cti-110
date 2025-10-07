#JacobGunter
#10/07/2025
#P2LAB1
#This Program will calculate the diameter, circumference, and area of a circle


#First we will ask the user to input the diameter, circumference, and area

# Get radius input from the user as a float
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius ** 2

# Display the results with specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")