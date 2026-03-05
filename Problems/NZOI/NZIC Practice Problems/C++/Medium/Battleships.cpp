#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_map<string, int> ships = {
        {"a", 1}, 
        {"b", 2}, 
        {"c", 3}, 
        {"d", 4}, 
        {"e", 5}, 
        {"f", 6}
    };

    unordered_map<string, int> health = ships;

    const int size = 10;
    vector<vector<string>> grid(size, vector<string>(size));

    for (int i = 0; i < size; i++) 
    {
        for (int j = 0; j < size; j++) 
        {
            cin >> grid[i][j];
        }
    }
    
    int x, y;

    while (cin >> x >> y && (x != -1 || y != -1))
    {
        string place = grid[y][x];

        if (place != "#") 
        {
            health[place]--;

            if (health[place] <= 0) 
            {
                cout << "Sunk " << place << "\n";
            } 

            else 
            {
                cout << "Hit " << place << "\n";
            }

            grid[y][x] = "#";

        } 

        else 
        {
            cout << "Miss" << "\n";
        }
    }
        
   return 0;
}