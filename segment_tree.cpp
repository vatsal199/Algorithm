#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

class SegTree{
		vector<int> A,st;
		int n;
		int left(int i){return (i<<1);}
		int right(int i){return (i<<1)+1;}
		void build(int p,int L,int R){
			if(L==R)
				st[p]=L;
			else{
				build(left(p),L,(L+R)/2);
				build(right(p),(L+R)/2 + 1,R);
				int p1=st[left(p)];
				int p2=st[right(p)];
				st[p]=(A[p1]<=A[p2])?p1:p2;
			}
		}
		int rmq(int p,int L,int R,int i,int j){
			if(i>R || j<L) return -1;
			if(i<=L && j>=R) return st[p];
			int p1=rmq(left(p),L,(L+R)/2,i,j);
			int p2=rmq(right(p),(L+R)/2 +1,R,i,j);
			if(p1==-1) return p2;
			if(p2==-1) return p1;
			return (A[p1]<=A[p2])?p1:p2;
		}
	public:
		SegTree(vector<int> &_A){
			A=_A;
			n=A.size();
			st.assign(4*n,0);
			build(1,0,n-1);
		}
		int RMQ(int i,int j){
			return rmq(1,1,n-1,i,j);
		}
};

int main(){
	int arr[] = { 18, 17, 13, 19, 15, 11, 20 };
	vector<int> A(arr,arr+7);
	SegTree s(A);
	printf("%d\n",s.RMQ(1,3));
	printf("%d\n",s.RMQ(4,6));
	return 0;
}
