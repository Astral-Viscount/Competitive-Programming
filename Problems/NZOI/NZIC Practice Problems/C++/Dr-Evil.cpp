#include <bits/stdc++.h>
using namespace std;

int main() {
    string word;
    getline(cin, word);

    string new_word;

    for (int i = word.size() - 1; i >= 0; i--)
    {
        new_word.push_back(word[i]);
    }
    
    cout << new_word;

    return 0;
}