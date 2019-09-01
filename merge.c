/*
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
*/
#include<stdio.h>
int len;
void print(int arr[],int len){
    for(int i=0;i<len;i++)
        printf("%d ",arr[i]);
}
void merge(int arr[],int low,int mid,int high){
    int temp[len];
    int p=mid+1;
    int q=low;
    int index = low;
    while(q<=mid && p<=high){
        if(arr[q]<=arr[p])
            temp[index++] = arr[q++];
        else
            temp[index++] = arr[p++];
    }
    while(q<=mid)
        temp[index++] = arr[q++];
    while(p<=high)
        temp[index++] = arr[p++];
    for(int i=low;i<index;i++)
        arr[i] = temp[i];
}
void partation(int arr[],int low,int high){
    int mid = (low+high)/2;
    //printf("%d %d %d",low,mid,high);
    if(low<high){
        partation(arr,low,mid);
        partation(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}
int main(){
    //int len = 6;
	int arr[]={10,60,50,20,85,40};
	len = sizeof(arr)/sizeof(int);
	partation(arr,0,len-1);
	print(arr,len);
	return 0;
}
