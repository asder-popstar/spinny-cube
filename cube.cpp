#include <iostream>
#include <cmath>
#include <vector>
#include <thread>
#include <chrono>

using namespace std;

const int width = 40, height = 20;
const float PI = 3.14159;

// Function to clear the screen (Windows: "cls", Linux/Mac: "clear")
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// 3D Rotation Function
void rotateCube(float angleX, float angleY) {
    float cube[8][3] = { // 3D Cube Vertices
        {-1, -1, -1}, {1, -1, -1}, {1, 1, -1}, {-1, 1, -1},
        {-1, -1,  1}, {1, -1,  1}, {1, 1,  1}, {-1, 1,  1}
    };
    
    vector<pair<int, int>> projected(8); // Store projected 2D coordinates

    for (int i = 0; i < 8; i++) {
        // Rotation around X-axis
        float y = cube[i][1] * cos(angleX) - cube[i][2] * sin(angleX);
        float z = cube[i][1] * sin(angleX) + cube[i][2] * cos(angleX);

        // Rotation around Y-axis
        float x = cube[i][0] * cos(angleY) - z * sin(angleY);
        z = cube[i][0] * sin(angleY) + z * cos(angleY);

        // Projection onto 2D screen
        float distance = 4;
        float scale = 10;
        int screenX = (int)(x * scale / (z + distance) * 2 + width / 2);
        int screenY = (int)(y * scale / (z + distance) + height / 2);
        projected[i] = {screenX, screenY};
    }

    // Cube edges
    int edges[12][2] = {
        {0,1}, {1,2}, {2,3}, {3,0}, // Front face
        {4,5}, {5,6}, {6,7}, {7,4}, // Back face
        {0,4}, {1,5}, {2,6}, {3,7}  // Connecting edges
    };

    // Draw frame
    vector<string> screen(height, string(width, ' '));
    for (auto& edge : edges) {
        int x1 = projected[edge[0]].first, y1 = projected[edge[0]].second;
        int x2 = projected[edge[1]].first, y2 = projected[edge[1]].second;

        // Simple Bresenham's line algorithm to draw edges
        int dx = abs(x2 - x1), dy = abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1, sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy;

        while (true) {
            if (x1 >= 0 && x1 < width && y1 >= 0 && y1 < height)
                screen[y1][x1] = '#';

            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) { err -= dy; x1 += sx; }
            if (e2 < dx) { err += dx; y1 += sy; }
        }
    }

    // Print frame
    clearScreen();
    for (const auto& line : screen) cout << line << endl;
}

int main() {
    float angleX = 0, angleY = 0;

    while (true) {
        rotateCube(angleX, angleY);
        angleX += 0.1f;  // Adjust speed of rotation
        angleY += 0.1f;
        this_thread::sleep_for(chrono::milliseconds(100));  // Control frame rate
    }

    return 0;
}
