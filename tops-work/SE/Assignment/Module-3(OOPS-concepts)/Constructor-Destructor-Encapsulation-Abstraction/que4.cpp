/*
Que4. Write a C++ program to implement a class called Bank Account that has private member variables for account number and balance. Include member functions to deposit and withdraw money from the account.
*/

#include <iostream>

using namespace std;

class Bank_Account{

private:    
        string name;
        long acc_number;
        string account_type;
        int balance;
public:
        Bank_Account(string name,long acc_number,string account_type,int balance){
            this->name = name;
            this->acc_number = acc_number;
            this->account_type = account_type;
            this->balance = balance;
        }

        int deposite(){
            int deposit_amt;
            cout<<"Enter deposite amount "<<endl;
            cin>>deposit_amt;
            balance = balance + deposit_amt;
            return balance;
        }

        int withdraw(){
            int withdraw_amt;
            cout<<"Enter withdraw amount "<<endl;
            cin>>withdraw_amt;
            if(balance > withdraw_amt){
                balance = balance - withdraw_amt;
            }
            else{
                cout<<"Insufficient balance"<<endl;
            }
            return balance;
        }

        void display(){
            cout<<"Name: "<<name<<endl<<"Balance: "<<balance;
        }
};

int main(){
    
    string nm;
    long acc_num;
    string acc_type;
    int bal;
    cout<<"Enter name, account number, account type and account balance"<<endl;
    cin>>nm>>acc_num>>acc_type>>bal;
    if(acc_num > 0 && bal > 0){
        Bank_Account b(nm,acc_num,acc_type,bal);
        cout<<"Balance after deposite: "<<b.deposite()<<endl;
        cout<<"Balance after withdraw: "<<b.withdraw()<<endl;
        b.display();
    }else{
        cout<<"Invalid account number or account balance"<<endl;
    }
    return 0;
}