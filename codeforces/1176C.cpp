#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    scanf("%d", &n);

    unordered_map<int, int> countNum;

    unordered_map<int, int> previous ({
        {8, 4},
        {15, 8},
        {16, 15},
        {23, 16},
        {42, 23},
    });

    for(int i = 0; i < n; ++i) {
        int num;
        scanf("%d", &num);
        
        if(num == 4) ++countNum[4];
        
        else {
            if(countNum[previous[num]] > 0) {
                --countNum[previous[num]];
                ++countNum[num];
            }   
        }
    }

    printf("%d\n", n-countNum[42]*6);
    return 0;
}