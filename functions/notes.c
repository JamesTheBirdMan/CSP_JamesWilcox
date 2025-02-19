// James Wilcox, Functions Notes C
#include <stdio.h>

void add(int num1, int num2){
    printf("%d\n", num1+num2);
}

char input(char type[20]){
    char answer[50];
    printf("Give me a %s:\n", type);
    scanf("%s", answer);
    return answer;
}

int main(void){
   //printf("Hello World\n");
   //add(12, 9);
   input("name");
   input("verb");
   input("place");
   printf("%s was %s until they somehow reached %s", word("name"), word("verb"), word("place"));
    return 0;
}