#include <bits/stdc++.h>

using namespace std;

// const int N=1e5+5;
// vector<int> graph[N];
// int vis[N];
// void dfs(int node){
//     vis[node]=1;
//     for(int child:graph[node]){
//         if(vis[child]!=1){
//             dfs(child);
//         }
//     }
// }

int main()
{
    long long int o, i, j, k, t, n;
    cin >> t;
	for(o=0;o<t;o++){
        int n;
        int k;
        cin>>n>>k;
        vector<int> a[n];
        for(int i=1;i<=n;i++){
            a[0].push_back(i);
        }
        vector<string> p;
        for(int j=0;j<n;j++){
            for(int p=0;p<n;p++){
                string s;
                swap(a[0][j],a[0][p]);
                cout<<"j is "<<j<<endl;
                for(int i=0;i<n;i++){
                    s+=char(a[0][i]+48);
                }
                cout<<s<<endl;
            }
        }
	}
}