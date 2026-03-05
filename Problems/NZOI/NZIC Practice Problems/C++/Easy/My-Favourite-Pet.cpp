#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> pets;

    int tmp;
    while(cin >> tmp)
    {
        pets.push_back(tmp);
    }

    
    int best = 0;
    int best_index = 1;
    int index = 1;

    for (int i : pets)
    {
        if (i > best)
        {
            best = i;
            best_index = index;
        }

        index ++;
    }
    
    cout << "Pet " << best_index;
}