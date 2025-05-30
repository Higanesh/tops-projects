/*
● Create a Food billing system

    Make sure each business logic is denoted with appropriate comments and
    make your code interactive and represent clean and clear output on your
    console screen.
    Adhere to the coding principles
    Firstly, display the food items available
    Then after the user can choose any of the item displayed
    Also take the quantity of selected food item by the customer, then ask the user that
    he/she wanna select more?
    If yes then again display the food items available and take an order from the
    customer. Here, you have to consider the total bill as the price of food items
    previously selected plus the price of new items added should display as a whole bill.
    If no then display the final bill on the screen
*/

#include <stdio.h>
#include <string.h>

// Declare variables for the total amount and menu items
float amt; 
char item[5][10] = {"PIZZA ","BURGER","DOSA  ","IDLI  ","SAMOSA"};
int rate[] = {200, 150, 100, 50, 20}; // Corresponding prices for each item

// Function to calculate the amount based on quantity and rate
int amount(int qty, int rate) 
{
    return qty * rate; 
}

int main() {
    char buffer[100]; // Buffer to hold input as a string
    int qty, menu_choice; // Variables to store quantity and user's choice
    char want_more; // Variable to store user's decision to continue or not

    do {
        // Display the menu
        printf("------------MENU-------------\n");
        printf("ITEM NAME\tPRICE\n");
        printf("-----------------------------\n");
        
        // Loop through and display all menu items and their prices
        for(int i = 0; i < 5; i++)
        {
            printf("%d.%s\t%drs/pc\n", i+1, item[i], rate[i]);
        }
        printf("-----------------------------\n");
        
        // Prompt user to select a meal
        printf("Select your meal\n");
        //scanf("%d", &menu_choice);

        //Read input as a string
        if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
            // Check if input is an integer
            if (sscanf(buffer, "%d", &menu_choice) != 1) {
                printf("Invalid input! Please enter a valid choice.\n");
                //continue;
            }
            
        // Display the selected meal
            switch(menu_choice)
            {
                case 1: printf("You chose PIZZA\n");
                        break;
                case 2: printf("You chose BURGER\n");
                        break;
                case 3: printf("You chose DOSA\n");
                        break;
                case 4: printf("You chose IDLI\n");
                        break;
                case 5: printf("You chose SAMOSA\n");
                        break;
                default: printf("You have selected a wrong item\n");
                        break;
            }
        }   
        // If a valid choice is made, prompt user for quantity and calculate the amount
        if(menu_choice <= sizeof(item) / sizeof(item[0]) && menu_choice > 0)
        {
                printf("Enter Quantity\n");
                if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                // Check if input is an integer
                    if (sscanf(buffer, "%d", &qty) != 1) {
                        printf("Invalid input! Please enter a valid quantity.\n");
                        //continue;
                    }
                // scanf("%d", &qty);
                else if(qty <= 0)
                {
                    printf("You have enter wrong quantity,Please enter quantity more than 0\n");
                } 
                else{
                        // Add the calculated amount to the total
                        amt += amount(qty, rate[menu_choice-1]);
            
                }
            }
        }
        
        // Display the current total amount
        printf("Amount: %.2f\n", amt);
        
        // Ask if the user wants to add something else
        printf("Do you want to add something else (Y/N)?\n");
        scanf(" %c", &want_more);

        // Clear the input buffer to handle extra characters (if any)
        while(getchar() != '\n');
          
    } while(want_more == 'y' || want_more == 'Y'); // Continue if the user wants to add more items
    
    // Display the grand total
    float gd = amt + (amt * 5 / 100);
    printf("Amount: %.2f\n",amt);
    printf("CGST: 2.5\n");
    printf("SGST: 2.5\n");
    printf("Grand total : %.2f", gd);
    
    return 0;
}


/*
OUTPUT:

D:\WEB DEVELOPMENT WITH PYTHON\tops\tops-projects\tops-work\SE\Assessment>gcc Food_billing_system.c -o a.exe

D:\WEB DEVELOPMENT WITH PYTHON\tops\tops-projects\tops-work\SE\Assessment>a
------------MENU-------------
ITEM NAME       PRICE
-----------------------------
1.PIZZA         200rs/pc
2.BURGER        150rs/pc
3.DOSA          100rs/pc
4.IDLI          50rs/pc
5.SAMOSA        20rs/pc
-----------------------------
Select your meal
3
You chose DOSA
Enter Quantity
5
Amount: 500.00
Do you want to add something else (Y/N)?
y
------------MENU-------------
ITEM NAME       PRICE
-----------------------------
1.PIZZA         200rs/pc
2.BURGER        150rs/pc
3.DOSA          100rs/pc
4.IDLI          50rs/pc
5.SAMOSA        20rs/pc
-----------------------------
Select your meal
2
You chose BURGER
Enter Quantity
32
Amount: 5300.00
Do you want to add something else (Y/N)?
n
Amount: 5300.00
CGST: 2.5
SGST: 2.5
Grand total : 5565.00
D:\WEB DEVELOPMENT WITH PYTHON\tops\tops-projects\tops-work\SE\Assessment>

*/