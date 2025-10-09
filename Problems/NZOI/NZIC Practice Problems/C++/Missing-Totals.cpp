#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int n;
    cin >> n;

    int total;

    for (int i = 0; i < n; i++)
    {
        int p, d;
        cin >> p >> d;

        if (d > p)
        {
            continue;
        }
        else
        {
            total += p - d;
        }
    }

    cout << total;

    return 0;
}