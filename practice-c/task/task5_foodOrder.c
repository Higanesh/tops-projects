/*
food order
*/

#include <stdio.h>
#include <string.h>

int amt;
char item[5][10] = {"PIZZA ","BURGER","DOSA  ","IDLI  ","SAMOSA"};
int rate[] = {200,150,100,50,20};

int amount(int qty,int rate)
{
    return qty * rate;
}
int main() {
     
    int qty,ch;
    char choice;
    do{
        printf("------------MENU-------------\n");
        printf("ITEM NAME\t\tPRICE\n");
        printf("-----------------------------\n");
        for(int i = 0; i < 5; i++)
        {
            printf("%d.%s\t\t\t%drs/pc\n",i+1,item[i],rate[i]);
        }
        printf("-----------------------------\n");
        printf("select your meal\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: printf("you choose PIZZA\n");
                    break;
            case 2: printf("you choose BURGER\n");
                    break;
            case 3: printf("you choose DOSA\n");
                    break;
            case 4: printf("you choose IDLI\n");
                    break;
            case 5: printf("you choose SAMOSA\n");
                    break;
            default : printf("you have selected wrong item\n");
                    break;
        }
        if(ch <= sizeof(item) / sizeof(item[0]) && ch > 0)
        {
            printf("Enter Quantity\n");
            scanf("%d",&qty);   
        }
        
        amt += amount(qty,rate[ch-1]);
        printf("Amount: %d\n",amt);
        printf("you want to add something else (Y/N)\n");
        scanf(" %c",&choice);
    }while(choice == 'y' || choice == 'Y');
    printf("Grand total : %d",amt);
    return 0;
}