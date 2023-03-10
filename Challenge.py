from math import tan, pi

def get_polygon_area(sides:list, regular:bool) -> float:
    if regular:
        # Finds area using generalised regular polygon formula
        return (sides[0]*sides[0]*len(sides))/(4*tan((pi/len(sides))))
    else:
        # Finds approximate area for irregular polygons
        return (len(sides)*(sum(sides)/2))/2

# Get user input, any non-integer inputs will simply be ignored
print("Is the room shape a regular polygon? (y/n):")
regular = input("> ") == "y"

print("\nEnter the length of each wall in the room in metres.")
print("Use commas (,) to separate each wall:")
walls = [int(l) for l in input("> ").replace(" ", "").split(",") if l.isnumeric()]

print(f"Your walls: {walls}")
print("\nEnter the height of the room in metres:")
height = int(input("> "))

# Calculate area of the floor plan
floor_plan = round(get_polygon_area(walls, regular),2)
print("\nArea of the floor plan:", floor_plan, "m^2")

# Calculate paint required to cover the walls
paint_required = sum([length*height for length in walls])
print("\nPaint needed to cover all the walls:", paint_required, "m^2")

# Calculate volume of room
print("\nVolume of the room:", round(floor_plan*height,2), "m^3")
