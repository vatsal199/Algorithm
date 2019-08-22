#include<algorithm>
#include<cstdio>
#include<math.h>
#include<iostream>
#include<vector>
using namespace std;
int XpowN(int x,int n){
    if(n>0){
        if(n%2 == 0){
            int temp = XpowN(x,n/2);
            return temp*temp;
        }
        else
            return x*XpowN(x,n-1);
    }
    else
        return 1;

}
int main(){
    //cout<<"Hello World\n";
   // printf("Hello World");
   cout<<XpowN(2,5);
    return 0;
}
