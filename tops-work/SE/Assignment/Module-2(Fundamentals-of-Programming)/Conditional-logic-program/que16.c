/*
Que16. Write a C program to read temperature in centigrade and display a suitable message according to the temperature state below:
Temp < 0 then Freezing weather Temp 0-10 then Very Cold weather Temp 10-20 then Cold weather Temp 20-30 then Normal in Temp Temp 30-40 then Its Hot
Temp >=40 then Its Very Hot.
*/

#include <stdio.h>

int main()
{
    int temperature;
    printf("Enter temperature in centigrade\n");
    scanf("%d",&temperature);
    if(temperature < 0){
        printf("Freezing weather");
    }else if(temperature >= 0 && temperature <= 10){
        printf("Very Cold weather");
    }else if(temperature >= 10 && temperature <= 20){
        printf("Cold weather");
    }else if(temperature >= 20 && temperature <= 30){
        printf("Normal in Temp");
    }else if(temperature >= 30 && temperature <= 40){
        printf("Its Hot Temp");
    }else if(temperature >= 40){
        printf("Its Very Hot");
    }
    
    return 0;
}