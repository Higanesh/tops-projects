#include<stdio.h>

int postIncrement(int a);
int postDecrement(int a);
int preIncrement(int b);
int preDecrement(int b);

int a,b,res;
void main()
{
    printf("enter 'a' for increment and decrement operation :\n");
    scanf("%d%d",&a,&b);
    printf("operand plus plus is: %d\n", postIncrement(a));
    printf("operand minus minus is: %d\n", postDecrement(a));
    printf("plus plus operand is: %d\n", preIncrement(b));
    printf("minus minus operand is: %d\n", preDecrement(b));
}

int postIncrement(int a)
{
    a++;
    //res = a;
    return a;
}

int postDecrement(int a)
{
    a--;
    //res = a;
    return a;
}

int preIncrement(int b)
{
    return ++b;
}

int preDecrement(int b)
{
    return --b;
}