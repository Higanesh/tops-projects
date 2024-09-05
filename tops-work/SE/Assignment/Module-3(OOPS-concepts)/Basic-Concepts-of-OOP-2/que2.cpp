/*
Que2. Define a class to represent a bank account. Include the following members:
    Data Member:
    -Name of the depositor
    -Account Number
    -Type of Account
    -Balance amount in the account
    Member Functions:
    -To assign values
    -To deposited an amount
    -To withdraw an amount after checking balance
    -To display name and balance
*/

#include <iostream>

using namespace std;

class bank_account{

    public:
        string name;
        long acc_number;
        string account_type;
        int balance;

        void set_value(string name,long acc_number,string account_type,int balance){
            name = name;
            acc_number = acc_number;
            account_type = account_type;
            balance = balance;
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
    bank_account b;
    cout<<"Enter name, account number, account type and account balance"<<endl;
    cin>>b.name>>b.acc_number>>b.account_type>>b.balance;
    if(b.acc_number > 0 && b.balance > 0){
        b.set_value(b.name,b.acc_number,b.account_type,b.balance);
        cout<<"Balance after deposite: "<<b.deposite()<<endl;
        cout<<"Balance after withdraw: "<<b.withdraw()<<endl;
        b.display();
    }else{
        cout<<"Invalid account number or account balance"<<endl;
    }
    return 0;
}