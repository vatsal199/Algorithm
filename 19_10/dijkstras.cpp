/*
node of heap: (distance,vertex)
node of graph: (vertex,weight)
n = no of vertex
m = no of edges
*/
#include<fstream>
#define cin fin

#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

class Heap{
private:
    vii arr;
    vi pos;
    int heap_size;
public:
    Heap(){
        heap_size = 0;
    }
    Heap(int n){
        arr.assign(n,ii());
        pos.assign(n,-1);
        heap_size = 0;
    }
    void bottomUpHeapify(int i){
        int parent = (i-1)/2;
        if(arr[parent].first > arr[i].first){
            int parent_vertex = arr[parent].second;
            int ithnode_vertex = arr[i].second;
            pos[parent_vertex] = i;
            pos[ithnode_vertex] = parent;
            swap(arr[i],arr[parent]);
            bottomUpHeapify(parent);
        }
    }
    void insert_key(int key,int v){
            arr[heap_size] = make_pair(key,v);
            pos[v] = heap_size;
            bottomUpHeapify(heap_size);
            heap_size++;
    }
    void decrease_key(int key,int v){
        int index = pos[v];
        arr[index].first = key;
        bottomUpHeapify(index);
    }
    bool isEmpty(){
        if(heap_size == 0)
            return true;
        return false;
    }
    void topDownHeapify(int i){
        int left = 2*i + 1;
        int right = 2*i + 2;
        int smallest;
        if(left<heap_size && arr[i].first > arr[left].first)
            smallest = left;
        else
            smallest = i;
        if(right<heap_size && arr[smallest].first > arr[right].first)
            smallest = right;
        if(smallest != i){
            int currNode_vertex = arr[i].second;
            int samllNode_vertex = arr[smallest].second;

            pos[currNode_vertex] = smallest;
            pos[samllNode_vertex] = i;

            swap(arr[i],arr[smallest]);
            topDownHeapify(smallest);
        }
    }
    ii getMinV(){
        ii minV = arr[0];
        swap(arr[0],arr[heap_size-1]);
        heap_size--;
        topDownHeapify(0);
        return minV;
    }
};
void printArr(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
dijktras(vector<vii> &graph,int n,int s){
    bool visited[n];
    int distance[n];
    for(int i=0;i<n;i++){
        distance[i] = INT_MAX;
        visited[i] = false;
    }
    Heap h1(n);
    h1.insert_key(0,s);
    visited[s] = true;
    while(!h1.isEmpty()){
        ii minV = h1.getMinV();

        int u = minV.second;
        int dis = minV.first;

        distance[u] = dis;

        for(int i = 0;i<graph[u].size();i++){

            int v = graph[u][i].first;
            int wuv = graph[u][i].second;

            if(distance[v] > distance[u] + wuv ){
                distance[v] = distance[u] + wuv;
                if(visited[v] == true){
                    h1.decrease_key(distance[v],v);
                }else{
                    h1.insert_key(distance[v],v);
                    visited[v] = true;
                }
            }
        }
    }
    printArr(distance,n);
}
int main()
{
    // -----------------------------------------------------------
    string filename = "C:/Users/vatsa/Desktop/input_graph.txt";
    ifstream fin(filename.c_str());
    if(!fin.is_open())
        cout<<"Unable to open file"<<endl;
    // -----------------------------------------------------------
    int TC;
    cin>>TC;
    while(TC--){
        int n,m;
        cin>>n>>m;
        vector<vii> graph(n);
        for(int i=0;i<m;i++){
            int a,b,w;
            cin>>a>>b>>w;
            graph[a].push_back(make_pair(b,w));
            graph[b].push_back(make_pair(a,w));
        }
        dijktras(graph,n,0);
    }
    return 0;
}

