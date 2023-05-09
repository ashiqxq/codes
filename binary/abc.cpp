#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
#define endl "\n"
#define endl "\n"
#define lli long long int
#define vi vector<int>
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define deb(x) cout<< #x << " " << x << "\n";
#define MAX 9223372036854775807
#define MIN -9223372036854775807
#define PI 3.141592653589
const lli INF = 1e18L + 5;
const lli mod = 1e9 + 7;
#define setbits(n) __builtin_popcountll(n)
 
vi ar[100001];
int disc[100001];
int low[100001];
int vis[100001];
vector<pi> ans; 
int timer, flag;
void dfs(int node, int parent){
	vis[node] = 1, disc[node] = low[node] = timer++;
	for (int child:ar[node]){
		if (child==parent) continue;
		if (vis[child]==1) {
			// found backedge
		low[node] = min(disc[child], low[node]);
		if (disc[node]>disc[child]){
			ans.push_back({node, child});
		}
		}
		else{
			dfs(child, node);
			if (low[child] > disc[node]){
				// found bridge
				flag = 1;
				return;
			}
			ans.push_back({node, child});
			low[node] = min(low[node], low[child]);
		}
	}
}
 
int main(){
	int n, m, x, y;
	cin >> n >> m;
	while (m--)
	cin >>x>>y, ar[x].push_back(y), ar[y].push_back(x);
	flag = 0;
	ans.clear();
	dfs(1, -1);
	if (flag==1) cout << 0 << endl;
	else{
		cout << endl;
		for (pi a:ans) cout << a.first <<" "<<a.second<<endl;
	}
}