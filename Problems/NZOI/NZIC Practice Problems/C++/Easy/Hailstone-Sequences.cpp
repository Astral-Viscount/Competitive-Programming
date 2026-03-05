#include <bits/stdc++.h>
using namespace std;

int sequence(int n);

int main() {
    
    vector<int> num;

    int tmp;
    while (cin >> tmp && tmp != 0)
    {
        num.push_back(tmp);
    }
    
    for (int i : num)
    {
        cout << sequence(i) << "\n";
    }
    
    return 0;
}

int sequence(int n)
{
    int count = 0;

    while (n != 1)
    {
        if (n % 2 != 0)
        {
            n = (3 * n) + 1;
            count ++;
        }
        else
        {
            n = n / 2;
            count ++;
        }
    }
    
    return count;
}