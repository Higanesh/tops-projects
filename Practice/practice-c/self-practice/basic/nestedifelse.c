#include<stdio.h>

int main()
{
    
    char groupstageres,super8res,semires,finalres;
    printf("Enter group stage result(W/L) : \n");
    scanf(" %c",&groupstageres);
    if(groupstageres == 'w' || groupstageres == 'W')
    {
        printf("congratulations!, you are in the super 8");
        printf("\nEnter super 8 result(W/L) : \n");
        scanf(" %c",&super8res);
        if (super8res == 'w' || super8res == 'W')
        {
            printf("congratulations!, you are in the semi-final");
            printf("\nEnter semi-final result(W/L) : \n");
            scanf(" %c",&semires);
            if (semires == 'w' || semires == 'W')
            {
                printf("congratulations!, you are in the final");
                printf("\nEnter final result(W/L) : \n");
                scanf(" %c",&finalres);
                if (finalres == 'w' || finalres == 'W')
                {
                    printf("congratulations!, India lift the world cup");
                }
                else
                {
                    printf("Better luck next time");
                }
            }
            else
            {
                printf("you are out of this tournament");
            }
        }
        else
        {
            printf("you are out of this tournament");
        }
        
    }
    else
    {
        printf("you are out of this tournament");
    }
    return 0;
}