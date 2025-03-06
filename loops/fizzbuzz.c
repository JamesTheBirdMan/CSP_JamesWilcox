// James Wilcox, FizzBuzz C
#include <stdio.h>
#include <string.h>

int num = 1;

int main(void){
while (num <= 50) {  
    if (num % 3 == 0 && num % 5 == 0) {  
        printf("FizzBuzz\n");
    } else if (num % 3 == 0) {  
        printf("Fizz\n");
    } else if (num % 5 == 0) {  
        printf("Buzz\n") ;
    } else {  
        printf("%d\n", num);
    }  
    num+=1;  
}  

    return 0;
}