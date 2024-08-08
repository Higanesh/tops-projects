#include<stdio.h>

//all arithmatic operation

int a,b,res;
int equalToEqualTo(int a, int b);
int notEqualTo(int a, int b);
int lessThan(int a, int b);
int lessThanEqualTo(int a, int b);
int greaterThan(int a, int b);
int greaterThanEqualTo(int a, int b);

void main()
{
    printf("enter 'a' and 'b' for assignment operation :\n");
    scanf("%d%d",&a,&b);
    printf("equal to equal to is: %d\n", equalToEqualTo(a,b));
    printf("not equal to is: %d\n", notEqualTo(a,b));
    printf("less than is: %d\n", lessThan(a,b));
    printf("less than equal to is: %d\n", lessThanEqualTo(a,b));
    printf("greater than is: %d\n", greaterThan(a,b));
    printf("greater than equal to is: %d\n", greaterThanEqualTo(a,b));
}

int equalToEqualTo(int a, int b)
{
    res = a == b;
    return res;
}
int notEqualTo(int a, int b)
{
    res = a != b;
    return res;
}

int lessThan(int a, int b)
{
    res = a < b;
    return res;
}

int lessThanEqualTo(int a, int b)
{
    res = a <= b;
    return res;
}

int greaterThan(int a, int b)
{
    res = a > b;
    return res;
}

int greaterThanEqualTo(int a, int b)
{
    res = a >= b;
    return res;
}