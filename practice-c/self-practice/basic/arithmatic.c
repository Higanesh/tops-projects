#include <stdio.h>

//all arithmatic operation

int res;
int add(int a, int b);
int sub(int a, int b);
int multi(int a, int b);
int div(int a, int b);
int modulo(int a, int b);

void main()
{
    int a,b;
    printf("enter a and b for arithmatic operation :\n");
    scanf("%d %d",&a, &b);
    printf("Sum of 2 numbers is: %d\n", add(a,b));
    printf("sub of 2 numbers is: %d\n", sub(a,b));
    printf("multi of 2 numbers is: %d\n", multi(a,b));
    printf("div of 2 numbers is: %d\n", div(a,b));
    printf("modulo of 2 numbers is: %d\n", modulo(a,b));
}

int add(int a, int b)
{
    res = a + b;
    return res;
}

int sub(int a, int b)
{
    res = a - b;
    return res;
}

int multi(int a, int b)
{
    res = a * b;
    return res;
}

int div(int a, int b)
{
    res = a / b;
    return res;
}

int modulo(int a, int b)
{
    res = a % b;
    return res;
}