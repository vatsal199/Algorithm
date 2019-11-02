/*
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
*/

#include<fstream>
#define cin fin

#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,ii> iii;

typedef vector<int> vi;


class Union_Find{
    vi parent;
    vi rnk;

public:
    Union_Find(){}
    void make_set(int n){
        for(int i=0;i<n;i++)
            parent.push_back(i);
        rnk.assign(n,1);
    }
    int find_set(int i){
        while(i != parent[i]){
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        return i;
    }

    bool isSameSet(int i,int j){
        return find_set(i) == find_set(j);
    }
    void unite(int i,int j){
        int p = find_set(i);
        int q = find_set(j);

        if(rnk[p] > rnk[q]){
            parent[q] = p;
        }else{
            parent[p] = q;
            if(rnk[p] == rnk[q])
                rnk[q]++;
        }
    }
};
int main()
{
    // -----------------------------------------------------------
    string filename = "./input_graph.txt";
    ifstream fin(filename.c_str());
    if(!fin.is_open())
        cout<<"Unable to open file"<<endl;
    // -----------------------------------------------------------
    int TC;
    cin>>TC;
    while(TC--){
        int n,m;
        cin>>n>>m;
        vector<iii> graph(m);
        int w,u,v;
        for(int i=0;i<m;i++){
            cin>>w>>u>>v;
            graph[i] = iii(w,ii(u,v));
        }
        sort(graph.begin(),graph.end());
        Union_Find u1;
        u1.make_set(n);
        for(int i=0;i<m;i++){
            u = graph[i].second.first;
            v = graph[i].second.second;
            w = graph[i].first;
            if(u1.find_set(u) != u1.find_set(v)){
                cout<<w<<" "<<u<<" "<<v<<endl;
                u1.unite(u,v);
            }
        }
    }
    return 0;
}
