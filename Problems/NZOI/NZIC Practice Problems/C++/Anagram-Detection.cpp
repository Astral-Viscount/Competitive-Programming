#include <bits/stdc++.h>
using namespace std;

int main() {
    string word, anagram;
    getline(cin, word);
    getline(cin, anagram);

    sort(word.begin(), word.end());
    sort(anagram.begin(), anagram.end());

    if (word == anagram)
    {
        cout << "yes";
    }
    else
    {
        cout << "no";
    }

    return 0;
}