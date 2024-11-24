#include <stdio.h>

//all arithmatic operation

int a;
int equalEqualTo(int a);
int plusEqualTo(int a);
int minusEqualTo(int a);
int multiEqualTo(int a);
int divEqualTo(int a);
int moduloEqualTo(int a);

void main()
{
    printf("enter 'a' for assignment operation :\n");
    scanf("%d",&a);
    printf("equal equal to is: %d\n", equalEqualTo(a));
    printf("plus equal to is: %d\n", plusEqualTo(a));
    printf("minus equal to is: %d\n", minusEqualTo(a));
    printf("multi equal to is: %d\n", multiEqualTo(a));
    printf("div equal to is: %d\n", divEqualTo(a));
    printf("modulo equal to is: %d\n", moduloEqualTo(a));
}

int equalEqualTo(int a)
{
    a = 10;
    return a;
}

int plusEqualTo(int a)
{
    a += 10;
    return a;
}

int minusEqualTo(int a)
{
    a -= 10;
    return a;
}

int multiEqualTo(int a)
{
    a *= 10;
    return a;
}

int divEqualTo(int a)
{
    a /= 10;
    return a;
}

int moduloEqualTo(int a)
{
    a %= 10;
    return a;
}