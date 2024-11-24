#include<stdio.h>

void main()
{
    short s = 200;
    int i = 20;
    float f = 24.43;
    double d = 23.41;
    long l = 32334;
    char c = 'g';
    
    printf("size of short is : %d\n",sizeof(s));
    printf("size of integer is : %d\n",sizeof(i));
    printf("size of floating point is : %d\n",sizeof(f));
    printf("size of double is : %d\n",sizeof(d));
    printf("size of long integer is : %d\n",sizeof(l));
    printf("size of character is :%d\n",sizeof(c));   
}