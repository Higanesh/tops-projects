#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

// Function to display the choice of either player or computer as Rock, Paper, or Scissors
void displayChoice(int choice) {
    if (choice == 1) {
        cout << "Rock" << endl;
    } else if (choice == 2) {
        cout << "Paper" << endl;
    } else if (choice == 3) {
        cout << "Scissors" << endl;
    }
}

int main() {
    string name;
    int no_of_rounds, current_round = 1, person_score = 0, computer_score = 0, person_choice, computer_choice;

    // Display a separator and prompt for the user's name
    cout << endl << "--*--*--*--*--*--*--*--*--*--*" << endl;
    cout << "             NAME" << endl;
    cout << "--*--*--*--*--*--*--*--*--*--*" << endl;
    cout << endl << "Enter your name: ";
    cin >> name;  // Get the player's name

    // Display a separator and prompt for the number of rounds
    cout << endl << "--*--*--*--*--*--*--*--*--*--*" << endl;
    cout << "             ROUNDS" << endl;
    cout << "--*--*--*--*--*--*--*--*--*--*" << endl;
    cout << endl << name << " How many rounds you want to play? : ";
    cin >> no_of_rounds;  // Get the number of rounds the player wants to play

    // Check if the player has entered a valid number of rounds
    if (no_of_rounds > 0) {
        srand(time(0));  // Seed the random number generator for computer's choices

        // Loop for the number of rounds the player wants to play
        do {
            // Display round information and scores
            cout << endl << "--*--*--*--*--*--*--*--*--*--*" << endl;
            cout << "             GAME" << endl;
            cout << "--*--*--*--*--*--*--*--*--*--*" << endl;
            cout << "\nRound no: " << current_round << "/" << no_of_rounds << endl;
            cout << endl << name << "'s Score = " << person_score << endl;
            cout << "Computer Score = " << computer_score << endl;
            cout << "\n1. ROCK\n2. PAPER\n3. SCISSOR" << endl;
            cout << endl << "Select your choice: ";
            cin >> person_choice;  // Get the player's choice

            // Validate the player's choice to make sure it's between 1 and 3
            while (true) {
                if (person_choice > 3 || person_choice < 1) {
                    cout << "Please select choice between 1 to 3: ";
                    cin >> person_choice;
                } else {
                    break;  // Valid input, break the loop
                }
            }

            // Display the player's choice as Rock, Paper, or Scissors
            cout << endl << name << "'s Choice: ";
            displayChoice(person_choice);

            // Randomly generate the computer's choice
            computer_choice = (rand() % 3) + 1;  // Randomly choose between 1 and 3
            cout << "Computer Choice: ";
            displayChoice(computer_choice);  // Display the computer's choice

            // Determine the winner of the round based on the player's and computer's choices
            if ((person_choice == 1 && computer_choice == 3) || 
                (person_choice == 2 && computer_choice == 1) || 
                (person_choice == 3 && computer_choice == 2)) {
                person_score += 1;  // Player wins the round
            } else if ((person_choice == 1 && computer_choice == 2) || 
                       (person_choice == 2 && computer_choice == 3) || 
                       (person_choice == 3 && computer_choice == 1)) {
                computer_score += 1;  // Computer wins the round
            } else {
                cout << endl << "You both selected the same choice" << endl;  // It's a tie
            }

            current_round++;  // Increment the round counter
        } while (current_round <= no_of_rounds);  // Continue until the specified number of rounds is reached

        // Display the final scores
        cout << endl << name << "'s Final Score: " << person_score << endl;
        cout << "Computer Final Score: " << computer_score << endl;

        // Determine and display the overall winner
        if (person_score > computer_score) {
            cout << endl << "Winner is " << name << endl;  // Player wins
        } else if (person_score < computer_score) {
            cout << endl << "Winner is Computer" << endl;  // Computer wins
        } else {
            cout << endl << "Match Draw" << endl;  // It's a draw
        }
    } else {
        cout << "You have entered 0 rounds" << endl;  // Invalid number of rounds
    }

    return 0;  // End of program
}


/*
OUTPUT:

D:\WEB DEVELOPMENT WITH PYTHON\tops\tops-projects\tops-work\SE\Assessment>a

--*--*--*--*--*--*--*--*--*--*
             NAME
--*--*--*--*--*--*--*--*--*--*

Enter your name: Ganesh

--*--*--*--*--*--*--*--*--*--*
             ROUNDS
--*--*--*--*--*--*--*--*--*--*

Ganesh How many rounds you want to play? : 3

--*--*--*--*--*--*--*--*--*--*
             GAME
--*--*--*--*--*--*--*--*--*--*

Round no: 1/3

Ganesh's Score = 0
Computer Score = 0

1. ROCK
2. PAPER
3. SCISSOR

Select your choice: 3

Ganesh's Choice: Scissors
Computer Choice: Rock

--*--*--*--*--*--*--*--*--*--*
             GAME
--*--*--*--*--*--*--*--*--*--*

Round no: 2/3

Ganesh's Score = 0
Computer Score = 1

1. ROCK
2. PAPER
3. SCISSOR

Select your choice: 2

Ganesh's Choice: Paper
Computer Choice: Scissors

--*--*--*--*--*--*--*--*--*--*
             GAME
--*--*--*--*--*--*--*--*--*--*

Round no: 3/3

Ganesh's Score = 0
Computer Score = 2

1. ROCK
2. PAPER
3. SCISSOR

Select your choice: 1

Ganesh's Choice: Rock
Computer Choice: Rock

You both selected the same choice

Ganesh's Final Score: 0
Computer Final Score: 2

Winner is Computer


D:\WEB DEVELOPMENT WITH PYTHON\tops\tops-projects\tops-work\SE\Assessment>a

--*--*--*--*--*--*--*--*--*--*
             NAME
--*--*--*--*--*--*--*--*--*--*

Enter your name: Ganesh

--*--*--*--*--*--*--*--*--*--*
             ROUNDS
--*--*--*--*--*--*--*--*--*--*

Ganesh How many rounds you want to play? : 2

--*--*--*--*--*--*--*--*--*--*
             GAME
--*--*--*--*--*--*--*--*--*--*

Round no: 1/2

Ganesh's Score = 0
Computer Score = 0

1. ROCK
2. PAPER
3. SCISSOR

Select your choice: 3

Ganesh's Choice: Scissors
Computer Choice: Scissors

You both selected the same choice

--*--*--*--*--*--*--*--*--*--*
             GAME
--*--*--*--*--*--*--*--*--*--*

Round no: 2/2

Ganesh's Score = 0
Computer Score = 0

1. ROCK
2. PAPER
3. SCISSOR

Select your choice: 1

Ganesh's Choice: Rock
Computer Choice: Scissors

Ganesh's Final Score: 1
Computer Final Score: 0

Winner is Ganesh
*/