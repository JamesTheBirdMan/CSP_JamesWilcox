// James Wilcox, Functions Notes C
#include <stdio.h>
#include <string.h>
char asnwer[20];
char first[20];
char second[20];
char third[20];
char fourth[20];
char fifth[20];

char* hellow(int count){
printf("Tell me person #%d's name:\n", count);
scanf("%s", asnwer);
return asnwer;
}

int main(void){
strcpy(first, hellow(1));  
printf("It's nice to meet you, %s!\n", first);
strcpy(second, hellow(2)); 
printf("It's nice to meet you, %s and  %s!\n", second, first); 
strcpy(third, hellow(3));  
printf("It's nice to meet you, %s, %s, and %s!\n", third, second, first);
strcpy(fourth, hellow(4));  
printf("It's nice to meet you, %s, %s, %s, and %s!\n", fourth, third, second, first);
strcpy(fifth, hellow(5));  
printf("It's nice to meet you, %s, %s, %s, %s, and %s!\n", fifth, fourth, third, second, first);
    return 0;
}