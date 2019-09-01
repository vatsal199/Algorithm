/*
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
*/
#include<stdio.h>
#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

class QuickSort{
private:
    int *arr;
    int length;
public:
    QuickSort(){length = 0;}
    QuickSort(int *a,int n){
        arr = a;
        length = n;
    }

    void add(int x){
        arr[length++] = x;
    }

    void printArr(){
        for(int i=0;i<length;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }

    int partition(int low,int high){
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

    int randFindRank(int low,int high,int rank){
        int p = rand()%(high-low+1)+low;
        swap(arr[p],arr[low]);
        int k = partition(low,high);
        if(rank == high-k+1)
            return k;
        else if(rank < high-k+1)
            return randFindRank(k+1,high,rank);
        else
            return randFindRank(low,k-1,rank-(high-k+1));
    }

    void quickSort(int low,int high){
        if(low<high){
            int median = randFindRank(low,high,(high-low+1)/2);
            swap(arr[low],arr[median]);
            int i=partition(low,high);
            quickSort(low,i-1);
            quickSort(i+1,high);
        }
    }

    int *getArr(){
        return arr;
    }

    int getLength(){
        return length;
    }
};

class DeleteAllGTMedian {
private:
     QuickSort q1;
     int length;
public:
    DeleteAllGTMedian(int *a,int n){
        length = n;
        int *arr = a;
        q1 = QuickSort(arr,length);
        q1.quickSort(0,n-1);

    }

    void printArr(){
        int *arr = q1.getArr();
        for(int i=0;i<length;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }

    void deleteGT(){
        //QuickSort q1 = QuickSort(arr,length);
        int median = q1.randFindRank(0,length-1,length/2);
        //cout<<median<<endl;
        length -= median-1;
    }

};

int main(){
    int arr[]={5,4,3,2,1};
    int len = sizeof(arr)/sizeof(int);
    //d1.printArr();
    DeleteAllGTMedian d1 = DeleteAllGTMedian(arr,len);
    d1.printArr();
    d1.deleteGT();
    d1.printArr();
    d1.deleteGT();
    d1.printArr();
    return 0;
}
