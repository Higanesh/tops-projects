/*
Que1. Assume a class cricketer is declared. Declare a derived class batsman from cricketer. Data member of batsman. Total runs, Average runs and best performance. Member functions input data, calculate average runs, Display data. (Single Inheritance)
*/

#include<iostream>
using namespace std;

class Cricketer{

    protected:
    Cricketer(){
        cout<<"I am from class Cricketer."<<endl;
    }
};

class Batsman : public Cricketer{

    int total_runs;
    int avg_runs;
    int best_per;

public:
    void input_data(){
        cout<<"Enter total runs of batsman: "<<endl;
        cin>>total_runs;
        cout<<"Enter best performance of batsman: "<<endl;
        cin>>best_per;
}

    int calculate_avg_runs(){
        int no_of_matches;
        cout<<"Enter number of matches played by batsman: ";
        cin>>no_of_matches;
        avg_runs = total_runs / no_of_matches;
        return avg_runs;
}

    void display_data(){
        cout<<"Total runs of batsman: "<<total_runs<<endl;
        cout<<"Average runs of batsman: "<<avg_runs<<endl;
        cout<<"Best performance of batsman: "<<best_per;
}
};

int main(){

    Batsman b;
    b.input_data();
    b.calculate_avg_runs();
    b.display_data();
    return 0;
}

