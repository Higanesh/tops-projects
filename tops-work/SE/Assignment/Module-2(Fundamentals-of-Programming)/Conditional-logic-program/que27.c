/*
Que27. WAP to show
i.
Monday to Sunday using switch case
ii.
Vowel or Consonant using switch case
*/

#include <stdio.h>
#include <string.h>

int main()
{
    int ch,flag;
    char c;
    printf("Enter 0 for check days in a week or Enter 1 for check alphabet is VOWEL or CONSONANT\n");
    scanf("%d",&flag);
    if(flag == 0){
        printf("Enter your days choice between 1 to 7\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:printf("MONDAY");
            break;
            case 2:printf("TUESDAY");
            break;
            case 3:printf("WEDNESDAY");
            break;
            case 4:printf("THURSDAY");
            break;
            case 5:printf("FRIDAY");
            break;
            case 6:printf("SATURDAY");
            break;
            case 7:printf("SUNDAY");
            break;
            default:printf("INVALID CHOICE\nEnter choice between 1 to 7");
            break;
        }
    }else if(flag == 1){
        printf("Enter any letter\n");
        scanf(" %c",&c);
        switch(c)
        {
            case 'a':case 'e':case 'i':case 'o':case 'u':case 'A':case 'E':case 'I':case 'O':case 'U': printf("VOWEL");
                break;
            case 'b':case 'c':case 'd':case 'f':case 'g':case 'h':case 'j':case 'k':case 'l':case 'm':case 'n':case 'p':case 'q':case 'r':case 's':case 't':case 'v':case 'w':case 'x':case 'y':case 'z':case 'B':case 'C':case 'D':case 'F':case 'G':case 'H':case 'J':case 'K':case 'L':case 'M':case 'N':case 'P':case 'Q':case 'R':case 'S':case 'T':case 'V':case 'W':case 'X':case 'Y':case 'Z': printf("CONSONANT");
                break;
            default: printf("INVALID LETTER");
                break;
        }
    }
    else
    {
        printf("INVALID CHOICE\nEnter 0 for check days in a week or Enter 1 for check alphabet is VOWEL or CONSONANT");
    }
    return 0;
}