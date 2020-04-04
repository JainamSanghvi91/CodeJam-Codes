#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
	cin>>t;
	while(t--){
        int n;
        int k;
        vector<int> a[n];
        for(int i=1;i<=n;i++){
            a[0].push_back(i);
        }
        for(int j=0;j<n;j++){
            for(int p=0;p<n;p++){
                swap(a[0][j],a[0][p]);
                cout<<"j is "<<j<<endl;
                for(int i=0;i<n;i++){
                    cout<<a[0][i]<<" ";
                }
                cout<<endl;
            }
        }
	}
	return 0;
}