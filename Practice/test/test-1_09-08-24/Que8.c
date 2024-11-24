/*
8] Write a for loop that prints all even numbers from 2 to 10.
*/

#include <stdio.h>

int main()
{
    int no;
    for(int no = 2; no <= 10; no++)
    {
        if(no % 2 == 0)
        {
            printf("%d\n",no);
        }
    }
    return 0;
}