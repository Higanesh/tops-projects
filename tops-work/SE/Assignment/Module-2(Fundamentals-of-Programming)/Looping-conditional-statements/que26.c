/*
Que26. 1/2 - 2/3 + 3/4 - 4/5 + 5/6 .......... n
*/

#include <stdio.h>

int main() {
    int n;
    double sum = 0.0;
    printf("Enter the number of terms (n): ");
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 1) {
            sum += (double)i / (i + 1); 
        } else {
            sum -= (double)i / (i + 1);  
        }
    }
    printf("The result of the series is: %lf\n", sum);
    return 0;
}
