#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin >> ws;

    vector<string> words;

    for (int i = 0; i < n; i++)
    {
        string word;
        getline(cin, word);
        
        words.push_back(word);
    }

    char letter;
    cin >> letter;

    for (string i : words)
    {
        int counter = count(i.begin(), i.end(), letter);
        cout << counter << "\n";
    }
    
    return 0;
}