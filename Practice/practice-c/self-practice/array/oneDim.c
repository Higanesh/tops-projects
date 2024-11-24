// Online C compiler to run C program online
#include <stdio.h>

int main() {
    
    int arr[10],len;
    printf("enter how many number of element you want in array\n");
    scanf("%d",&len);
    
    //int len = sizeof(arr) / sizeof(arr[0]);
    
    for(int i = 0; i < len; i++)
    {
        printf("Enter element[%d]: ",i);
        scanf("%d",&arr[i]);
    }
    
    for(int i = 0; i < len; i++)
    {
        printf("Element[%d]: %d\n",i,arr[i]);
    }
    return 0;
}