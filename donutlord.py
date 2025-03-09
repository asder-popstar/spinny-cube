import math
import os
import time

# Constants for rotation and scaling
A, B = 0, 0
R1 = 1.0  # Inner radius
R2 = 2.0  # Outer radius
K2 = 5.0  # Scaling factor
K1 = 40    # Field of view

# Clear the screen for every frame (works on Windows/Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop to create the spinning donut
while True:
    clear_screen()

    # Initialize the frame (resolution of 40x80)
    frame = [[' ' for _ in range(80)] for _ in range(40)]

    # Loop through angles i (around the donut) and j (for rotation)
    for j in range(0, 628, 4):  # Loop j with smaller steps for more precision
        for i in range(0, 628, 2):  # Loop i with a step of 2 for better resolution
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)  # A factor for projection
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(K2 * D * (l * h * m - t * n) + 40)  # X projection
            y = int(K2 * D * (l * h * n + t * m) + 12)  # Y projection

            # Convert to int to find the grid coordinates
            o = int(x)
            p = int(y)

            # Make sure the coordinates are within the bounds
            if 0 <= p < 40 and 0 <= o < 80:
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # Calculate brightness
                if N > 0:
                    frame[p][o] = '.,-~:;=!*#$@'[N % 12]  # Use characters for shading

    # Print the frame
    for row in frame:
        print(''.join(row))

    # Update the angles for rotation
    A += 0.04
    B += 0.02

    # Add a small delay for smooth animation
    time.sleep(0.05)
