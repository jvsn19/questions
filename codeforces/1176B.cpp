#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    unsigned long t, n, num;
    scanf("%lu", &t);

    while(t--) {
        scanf("%lu", &n);
        vector<int> arr;
        
        while(n--) {
            scanf("%lu", &num);
            arr.push_back(num%3);
        }

        vector<int> count(3, 0);
        for(auto num: arr) ++count[num];

        int answer = count[0];
        answer += min(count[1], count[2]);
        answer += max(0, abs(count[1] - count[2])/3);
        printf("%d\n", answer);
    }
    return 0;
}