/*
  1   2   3   4   5   6   7   8   9  10
  36  37  38  39  40  41  42  43  44  11
  35  64  65  66  67  68  69  70  45  12
  34  63  84  85  86  87  88  71  46  13
  33  62  83  96  97  98  89  72  47  14
  32  61  82  95 100  99  90  73  48  15
  31  60  81  94  93  92  91  74  49  16
  30  59  80  79  78  77  76  75  50  17
  29  58  57  56  55  54  53  52  51  18
  28  27  26  25  24  23  22  21  20  19
*/

#include <stdio.h>

int main() {
    int matrix[10][10];
    int top = 0, bottom = 10 - 1, left = 0, right = 10 - 1;
    int value = 1;

    while (value <= 10 * 10) {
        // Fill top row
        for (int i = left; i <= right && value <= 10 * 10; i++) {
            matrix[top][i] = value++;
        }
        top++;

        // Fill right column
        for (int i = top; i <= bottom && value <= 10 * 10; i++) {
            matrix[i][right] = value++;
        }
        right--;

        // Fill bottom row
        for (int i = right; i >= left && value <= 10 * 10; i--) {
            matrix[bottom][i] = value++;
        }
        bottom--;

        // Fill left column
        for (int i = bottom; i >= top && value <= 10 * 10; i--) {
            matrix[i][left] = value++;
        }
        left++;
    }

    // Print the matrix
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%4d", matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}
