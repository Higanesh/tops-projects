/*
Que15. Write a program in C to find the largest and smallest words in a string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    int word_counter = 1,char_counter = 0;
    printf("Enter any string\n");
    fgets(str,sizeof(str),stdin);
    str[strcspn(str, "\n")] = '\0';
    //printf("%s\n",str);
    int j = 0;
    while(str[j] != '\0')
    {
        if(str[j] == ' ')
        {
            word_counter++;
        }
        j++;
    }
    printf("Total number of words in string: %d\n",word_counter);
    int word_lengths[word_counter];
    int i = 0, word_index = 0;
    while (str[i] != '\0') {
        if (str[i] != ' ') {
            char_counter++;
        } else {
            word_lengths[word_index] = char_counter;
            printf("Length of word %d: %d\n", word_index + 1, char_counter);
            word_index++;
            char_counter = 0;  // Reset character counter for next word
        }
        i++;
    }
    if (char_counter > 0) {
        word_lengths[word_index] = char_counter;
        printf("Length of word %d: %d\n", word_index + 1, char_counter);
    }
    
    printf("Word lengths stored in the array:\n");
    for (int k = 0; k <= word_index; k++) {
        printf("Word %d length: %d\n", k + 1, word_lengths[k]);
    }
    
    //check smallest and largest word in the given string
    int temp = 0;
    for(int j = 0; j < word_index; j++)
            {
                 if(word_lengths[j] > word_lengths[j+1])
                {
                    temp = word_lengths[j];
                    word_lengths[j] = word_lengths[j+1];
                    word_lengths[j+1] = temp;
                }
            }
    printf("Largest no. is %d\n",word_lengths[word_counter-1]);
    
    int temp1 = 0;
    for(int j = 0; j < word_index; j++)
            {
                 if(word_lengths[j] < word_lengths[j+1])
                {
                    temp1 = word_lengths[j];
                    word_lengths[j] = word_lengths[j+1];
                    word_lengths[j+1] = temp1;
                }
            }
    printf("Smallest no. is %d",word_lengths[word_counter-1]);
    return 0;
}