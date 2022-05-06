#include <stdio.h>


void swap(int * A, int i, int j){
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

void printArray(int * A, int n){
    int i;
    for(i=0; i < n; i++){
        printf("%d ", A[i]);
    }
    printf("\n");

}

void perm(int * A, int p, int q){
    if (p == q){
        printArray(A, q + 1);
    }
    else{
        int i;
        for (i = p; i < q + 1; i++){
            swap(A, p, i);
            perm(A, p+1, q);
            swap(A, p, i);
        }
    }

}

int main(){
    int A[] = {1,2,3};
    perm(A, 0, 2);
    return 0;
}