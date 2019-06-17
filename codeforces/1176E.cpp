#include <bits/stdc++.h>
#define INF 10e5

using namespace std;

vector<vector<int>> graph;
vector<int> nums;

void bfs(int start) {
    queue<int> queue;
    queue.push(start);
    nums[start] = 0;

    while(!queue.empty()) {
        int curr = queue.front();
        queue.pop();

        for(auto next: graph[curr]) {
            if(nums[next] == INF) {
                nums[next] = nums[curr] + 1;
                queue.push(next);
            }
        }

    }
}

int main(){
    ios::sync_with_stdio(false);
    int t, n, m, u, v;
    scanf("%d", &t);
    
    while(t--) {
        scanf("%d %d", &n, &m);
        graph = vector<vector<int>>(n);
        nums = vector<int>(n, INF);

        while(m--) {
            scanf("%d %d", &u, &v);
            --u; --v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        
        bfs(0);

        vector<int> even, odd;

        for(unsigned int i = 0; i < nums.size(); ++i) {
            if(nums[i]&1) odd.push_back(i+1);
            else even.push_back(i+1);
        }

        if(odd.size() > even.size()) {
            printf("%lu\n", even.size());
            for(auto node: even) printf("%d ", node);
        }
        else {
            printf("%lu\n", odd.size());
            for(auto node: odd) printf("%d ", node);
        }
        printf("\n");
    }

    return 0;
}