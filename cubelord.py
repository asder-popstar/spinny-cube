import math
import os
import time

# Constants
A, B = 0, 0
R1 = 1
R2 = 2
K2 = 5
K1 = 40

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Initialize the frame
    frame = [[' ' for _ in range(80)] for _ in range(40)]

    # Loop over the circle
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(K2 * D * (l * h * m - t * n) + 40)
            y = int(K2 * D * (l * h * n + t * m) + 12)
            o = int(x)
            p = int(y)
            if 0 <= p < 40 and 0 <= o < 80:
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if N > 0:
                    frame[p][o] = '.,-~:;=!*#$@'[N % 12]

    # Print the frame
    for row in frame:
        print(''.join(row))

    # Update angles
    A += 0.04
    B += 0.02

    # Delay
    time.sleep(0.05)
