#include<stdio.h>
#include<iostream>

using namespace std;

class MergeSort{
private:
    int *arr;
    int length;
public:
    MergeSort(){length = 0;}
    MergeSort(int *a,int n){
        arr = a;
        length = n;
    }
    void printArr(){
        for(int i=0;i<length;i++)
            printf("%d ",arr[i]);
        cout<<endl;
    }
    void merge(int low,int mid,int high){
        int temp[length];
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
    void partation(int low,int high){
        int mid = (low+high)/2;
        if(low<high){
            partation(low,mid);
            partation(mid+1,high);
            merge(low,mid,high);
        }
    }
    int *getArr(){
        return arr;
    }
    void sort(){
        partation(0,length-1);
    }
};
class KSorted{
private:
    MergeSort m1;
    int *startIndex;
    int *stopIndex;
    int length;
    int K;
public:
    KSorted(int *a,int n,int *indices,int k){
        m1 = MergeSort(a,n);
        length = n;
        K = k;
        startIndex = new int[K];
        stopIndex = new int[K];
        int j = 0;
        for(int i=0;i<K*2;i+=2){
            *(startIndex+j) = *(indices+i);
            *(stopIndex+j) = *(indices+i+1);
            j++;
        }
    }

    void printArr(){
        int *arr = m1.getArr();
        for(int i=0;i<length;i++)
            printf("%d ",arr[i]);
        cout<<endl;
    }

    void merge(){
        while(K>1){
            mergeOneIteration();
        }
    }

    void mergeOneIteration(){
        int noOfMerge = 0;
        int lastInd[2];
        bool flag = false;
        if(K%2 == 0){
            noOfMerge = K/2;
            K = noOfMerge;
        }
        else{
            noOfMerge = (K-1)/2;
            lastInd[0] = startIndex[K-1];
            lastInd[1] = stopIndex[K-1];
            K = noOfMerge+1;
            flag = true;
        }
        int i=0;
        int boundIndex = 0;
        while(noOfMerge){
            m1.merge(startIndex[i],startIndex[i+1]-1,stopIndex[i+1]);
            *(startIndex+boundIndex) = *(startIndex+i);
            *(stopIndex+boundIndex) = *(stopIndex+i+1);
            boundIndex++;
            i += 2;
            noOfMerge--;
        }
        if(flag){
            startIndex[boundIndex] = lastInd[0];
            stopIndex[boundIndex] = lastInd[1];
        }
    }
};
int main(){
	// K sorted array in 1 array
	int arr[]={10,50,60,20,85,95,5,10};
	// start followed by end index of soretd array with respect to above declared array
	int ind[]={0,2,3,5,6,7};
	int len = sizeof(arr)/sizeof(int);
	int indLen = sizeof(ind)/(2*sizeof(int));

	KSorted k1 = KSorted(arr,len,ind,indLen);
	k1.printArr();
	k1.merge();
	k1.printArr();
	return 0;
}
