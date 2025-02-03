// James Wilcox, Expressions Notes C
#include <stdio.h>
//integers have int when set variable and %d when print
//floats have float when set the variable and %f when print
//strings (words) char when we set the variable and %s when print
int mynum;
float percent;

int main(void){
    printf("Type a number: \n"); 
    scanf("%d", &mynum);
    printf("you said %d", mynum);
    printf("give me a percent as a decimal: \n");
    scanf("%f", &percent);
    printf("Your percent is %f\n", percent);
    return 0;
}