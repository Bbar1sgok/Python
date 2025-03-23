def determine_quadrilateral_type(a, b, c, d):
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "Side lengths must be greater than zero."

    if a == b == c == d:
        return "Square"
    elif a == c and b == d:
        return "Rectangle"
    else:
        return "Quadrilateral"


def determine_triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Side lengths must be greater than zero."

    if abs(a + b) > c and abs(a + c) > b and abs(b + c) > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or a == c or b == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Does not form a triangle."


shape = input("Which shape's type do you want to learn? ")

if shape.lower().strip() == "quadrilateral":
    print("Please enter the sides in order.")
    try:
        sides = [int(input(f"Side-{i + 1}: ")) for i in range(4)]
        print(determine_quadrilateral_type(*sides))
    except ValueError:
        print("Please enter a valid number.")

elif shape.lower().strip() == "triangle":
    try:
        sides = [int(input(f"Side-{i + 1}: ")) for i in range(3)]
        print(determine_triangle_type(*sides))
    except ValueError:
        print("Please enter a valid number.")

else:
    print("Invalid shape.")
