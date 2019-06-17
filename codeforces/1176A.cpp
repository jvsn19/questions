#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;

int numTasks(ull n) {
    int answer = 0;

    while(n%2 == 0) {
        ++answer;
        n /= 2;
    }

    while(n%3 == 0) {
        answer += 2;
        n /= 3;
    }

    while(n%5 == 0) {
        answer += 3;
        n /= 5;
    } 
    return n == 1 ? answer : -1;
}

int main() {
    ull t, n;
    cin >> t;

    while(t--) {
        cin >> n;
        cout << numTasks(n) << endl;
    }

    return 0;
}