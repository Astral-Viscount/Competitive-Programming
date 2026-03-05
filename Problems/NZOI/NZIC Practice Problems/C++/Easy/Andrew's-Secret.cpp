#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> num;
    for (int i = 0; i < 100; i++)
    {
        int tmp;
        cin >> tmp;
        num.push_back(tmp);
    }

    int sum = accumulate(num.begin(), num.end(), 0);
    int avg = sum / num.size();

    auto max_it = max_element(num.begin(), num.end());
    int max = *max_it;

    auto min_it = min_element(num.begin(), num.end());
    int min = *min_it;

    cout << min << " " << max << " "  << avg;
    
    return 0;
}