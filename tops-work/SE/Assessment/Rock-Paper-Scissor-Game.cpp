# include <iostream>
#include<stdlib.h>
#include<ctime>
using namespace std;


int main(){
    string name;
    int rounds,counter = 1,p1_score = 0,p2_score = 0,ch,cc;
    cout<<"NAME\n"<<"Enter your name :";
    cin>>name;
    cout<<"ROUNDS\n"<<name<<" How many rounds you want to play? : ";
    cin>>rounds;
    if(rounds > 0)
    {
            do
            {
                cout<<"GAME";
                cout<<"\nRound no: "<<counter<<"/"<<rounds<<endl;
                cout<<name<<" Score = "<<p1_score<<endl;
                cout<<"Computer Score = "<<p2_score<<endl;
                cout<<"\n1. ROCK\n2. PAPER\n3. SCISSOR"<<endl;
                cout<<"Select your choice: ";
                cin>>ch;
                srand(time(0));
                cc = (rand()%3)+1; 

                if(ch == cc){
                    cout<<"Tie";
                }
                counter++;
                cout<<counter; 
            } while (counter <= rounds);
           
    }
    else
    {
        cout<<"You want to play at least 1 round";
    }
}
