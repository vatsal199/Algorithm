/*
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
*/
#include<stdio.h>
#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;
// int len;
void print(int arr[],int low,int high){
    for(int i=low;i<high;i++)
        printf("%d ",arr[i]);
    printf("\n");
}
int partition(int arr[],int low,int high){
    int i=low+1,j=high;
    while(i<=j){
        while(i<=high && arr[i]<=arr[low])
            i++;
        while(j>= low+1 && arr[j]>arr[low])
            j--;
        if(i<j){

            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i-1],arr[low]);

    return i-1;
}
int randFindRank(int arr[],int low,int high,int rank){
    int p = rand()%(high-low+1)+low;
    swap(arr[p],arr[low]);
    int k = partition(arr,low,high);
    if(rank == high-k+1)
        return k;
    else if(rank < high-k+1)
        return randFindRank(arr,k+1,high,rank);
    else
        return randFindRank(arr,low,k-1,rank-(high-k+1));
}
void quicksort(int arr[],int low,int high,int arrLen){
    if(low<high){
        int median = randFindRank(arr,low,high,(high-low+1)/2);
        swap(arr[low],arr[median]);
        int i=partition(arr,low,high);
        quicksort(arr,low,i-1,arrLen);
        quicksort(arr,i+1,high,arrLen);
    }
}
int main(){
    // int arr[]={10,60,50,20,85,40,15};
    int maxVal=100;
    int arrLen;
    cin>>arrLen;
    int arr[arrLen];
	//len = sizeof(arr)/sizeof(int);
	for(int i=0;i<arrLen;i++){
        arr[i] = rand()%maxVal;
        //arr[i] = arrLen - i;
	}
	//print(arr,0,arrLen);
	//cout<<endl;
	const clock_t now  = clock();
	cout<<now<<endl;
	quicksort(arr,0,arrLen-1,arrLen);
	const clock_t then = clock();
	cout<<then<<endl;
	//print(arr,0,arrLen);
	//cout<<endl;
	cout<<then-now;
    return 0;
}
