#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> num;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        num.push_back(x);
    }

    set<int> num_set(num.begin(), num.end());

    for (int j : num_set)
    {
        int appearance = count(num.begin(), num.end(), j);

        if (appearance > 1)
        {
            cout << j << "\n";
        }
    }
    
    return 0;
}