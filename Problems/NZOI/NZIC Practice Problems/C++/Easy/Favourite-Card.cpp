#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, s;

    cin >> n >> s;

    int index;

    for (int i = 0; i < n; i++)
    {
        int c;
        cin >> c;
        
        if (c == s)
        {
            cout << index;
            break;
        }

        index ++;
    }
    
    return 0;
}