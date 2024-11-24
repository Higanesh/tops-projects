/*
task - 1 : guessing game
1] puts "Welcome to the guessing game!"
2] get input from the user: number between 0 to 100 [GUESSING_NUMBER]
3] generate a random number between 0 to 100 [WINNING_NUMBER]

GUESSING_NUMBER == WINNING_NUMBER:
puts "Congrats, You win!. (you win after gussing (count) times)"

GUESSING_NUMBER < WINNING_NUMBER :
puts "Your guess is too low. Try again."

GUESSING_NUMBER > WINNING_NUMBER :
puts "Your guess is too high. Try again."

4] set Guess counter

5] restart the game if user want to continue
*/

#include <stdio.h>

int main() {
    
    int winningNumber = 45,guessingNumber,counter = 1,limit = 3;
    char choice;
    do{
        printf("Welcome to the Guessing Game!\n");
        printf("If you want to win this game you have to guess right number within 3 attempts\n");
        while(counter <= limit)
        {
            printf("Enter your guessing number (between 0 to 100)\n");
            scanf("%d",&guessingNumber);
            if(guessingNumber < 0 || guessingNumber > 100)
            {
                printf("your have enter number out of range\n");
            }
            else if(guessingNumber < winningNumber)
            {
                printf("Your guess is too low\n");
            }
            else if(guessingNumber > winningNumber)
            {
                printf("Your guess is too high\n");
            }
            else
            {
                printf("Congrats, You win!\n");
            }
            counter++;
            
        }
        printf("You have reached the maximum number of attempts\n");
        printf("You want to continue your game(Y/N)\n");
        scanf(" %c",&choice);
        counter = 1;
    }while(choice == 'Y');
    return 0;
}