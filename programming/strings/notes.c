// James Wilcox, Strings Notes C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
    //printf("Please tell me your full name:\n");
    //scanf("%s", name);
    //fgets(name, 20, stdin);
    //printf("Hello and welcome to my program,%s", name);
    //char sentence[] = "The amogus is so sus";
    //printf("%d\n", strlen(sentence));
    char one[] = "Hello ";
    char two[] = "World!";
    two[5] = '?';
    printf("%s\n", one);
    strcat(one, two);
    printf("%s\n", one);
    return 0;
}