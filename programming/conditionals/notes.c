// James Wilcox, Conditionals Notes C
#include <stdio.h>
#include <string.h>
char name[20];

// && = and
// || = or
// != = not

int main(void){
    printf("Please enter your name: ");
    scanf("%s", name);
if(strcmp(name, "James") || (name, "Cairo") == 0){
    printf("Hi you are very cool");
}else{
    printf("You are a horrible person with a horrible name. You should be ashamed.");
}
    return 0;
}