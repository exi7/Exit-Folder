import time

def generate_spiral(size):
    spiral = [[0] * size for _ in range(size)]  # Create a square grid

    x, y = size // 2, size // 2  # Start at the center
    num = 1
    dx, dy = 0, -1

    for _ in range(size * size):
        if 0 <= x < size and 0 <= y < size:
            spiral[y][x] = num
            num += 1

        # Calculate new coordinates
        nx, ny = x + dx, y + dy

        # Change direction if out of bounds or the cell is already filled
        if not (0 <= nx < size and 0 <= ny < size and spiral[ny][nx] == 0):
            dx, dy = -dy, dx  # Rotate right
            nx, ny = x + dx, y + dy

        x, y = nx, ny  # Update coordinates

    return spiral

def display_spiral_with_animation(spiral):
    size = len(spiral)
    display = [[" " for _ in range(size)] for _ in range(size)]  # Empty grid

    for y in range(size):
        for x in range(size):
            display[y][x] = f"{spiral[y][x]:02d}"  # Format numbers

            # Progressive display
            for row in display:
                print(" ".join(row))
            time.sleep(0.1)
            print("\n" * 5)  # Refresh effect

# User input
size = int(input("Enter the width of the spiral (odd number): "))
if size % 2 == 0:
    print("Please enter an odd number.")
else:
    spiral = generate_spiral(size)
    display_spiral_with_animation(spiral)
