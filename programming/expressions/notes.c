// James Wilcox, Expressions Notes C
#include <stdio.h>
#include <math.h> //This lets us do exponents
//integers have int when set variable and %d when print
//floats have float when set the variable and %f when print
//strings (words) char when we set the variable and %s when print
int mynum;
float percent;
int add = 4+6;
int sub = 4-6;
int mul = 4*6;
float div = 6/4;
int ex = pow(5, 2);

int main(void){
   // printf("Type a number: \n"); 
   // scanf("%d", &mynum);
   // printf("you said %d", mynum);
   // printf("give me a percent as a decimal: \n");
   // scanf("%f", &percent);
   // printf("Your percent is %f\n", percent);
   printf("%d\n", add);
   printf("%d\n", sub);
   mul = 7*4;
   printf("%d\n", mul);
   printf("%.2f\n", div);
   printf("%d\n", ex);
    return 0;
}