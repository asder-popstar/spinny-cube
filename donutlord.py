import math
import os
import time

# Constants for 3D projection and scaling
A, B = 0, 0  # Rotation angles
R1 = 1.0  # Inner radius
R2 = 2.0  # Outer radius
K2 = 5.0  # Scaling factor for size
K1 = 40    # Field of view (distance from the viewer)
WIDTH = 80  # Start with a smaller width for debugging
HEIGHT = 40  # Start with a smaller height for debugging

# Function to clear the screen (works for Windows/Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop to render the spinning donut in 3D
while True:
    clear_screen()

    # Create a blank canvas (height x width grid)
    frame = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Loop through the angles j (around the donut) and i (for rotation)
    for j in range(0, 628, 4):  # Loop j with smaller steps
        for i in range(0, 628, 2):  # Loop i with a step of 2 for higher resolution
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2  # Add 2 to move the donut slightly away from the viewer
            D = 1 / (c * h * e + f * g + 5)  # Perspective correction
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(K2 * D * (l * h * m - t * n) + WIDTH / 2)  # X projection
            y = int(K2 * D * (l * h * n + t * m) + HEIGHT / 2)  # Y projection

            # Convert to int to find grid coordinates
            o = int(x)
            p = int(y)

            # Only plot points that are inside the bounds of the screen
            if 0 <= p < HEIGHT and 0 <= o < WIDTH:
                # Calculate shading for the 3D effect (light intensity)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
   
