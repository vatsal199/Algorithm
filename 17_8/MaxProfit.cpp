#include<iostream>
#include<stdio.h>

using namespace std;

class MaxProfit{
private:
    int *arr;
    int length;
public:
    MaxProfit(){
        length = 0;
    }
    MaxProfit(int *a,int n){
        arr = a;
        length = n;
    }
    int findProfit(){
        int maxP = arr[0];
        int i = 0;
        for(int j=1;j<length;j++){
            if(arr[j] - arr[i] > maxP){
                maxP = arr[j] - arr[i];
            }
            if(arr[i]>arr[j]){
                i = j;
            }
        }
        return maxP;
    }
};

int main(){
    int arr[]= {2,3,1,2,3,8,5,6};
    int len = sizeof(arr)/sizeof(int);
    MaxProfit m1 = MaxProfit(arr,len);
    int maxP = m1.findProfit();
    cout<<maxP;
    return 0;
}
