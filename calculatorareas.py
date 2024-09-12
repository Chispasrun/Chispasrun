# Import the math module to use math.pi for the circle area calculation
import math

# Function to calculate the area of a square
def calculate_square_area():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is {area}.")

# Function to calculate the area of a rectangle
def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area}.")

# Function to calculate the area of a triangle
def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print(f"The area of the triangle is {area}.")

# Function to calculate the area of a circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is {area}.")

# Main function to present the menu and call the appropriate area function
def main():
    while True:
        # Display the menu of shapes
        print("\nChoose a shape to calculate its area:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter the number of your choice: ")
        
        # Call the appropriate function based on the user's choice
        if choice == '1':
            calculate_square_area()
        elif choice == '2':
            calculate_rectangle_area()
        elif choice == '3':
            calculate_triangle_area()
        elif choice == '4':
            calculate_circle_area()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
