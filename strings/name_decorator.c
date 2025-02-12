// James Wilcox, Template
#include <stdio.h>
#include <string.h>

char name[20];
char name_deco1[12] = "~:O-|-{ ";
char name_deco2[12] = " }-|-O:~";

int main(void){
    printf("Please enter your name: ");
    scanf("%s", name);
    strcat(name_deco1, name);
    strcat(name_deco1, name_deco2);
    printf("Your name is %s\n", name_deco1);
    return 0;
}