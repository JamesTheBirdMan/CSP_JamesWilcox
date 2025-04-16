// James Wilcox, My Family Loop C
#include <stdio.h>
#include <string.h>

char *family[] = {"Billy", "Bob", "Joe", "John", "Jacob", "Jinglheimer", "Smith", "Jesus"};
int num = 0;

int main(void){
while (num <8){
    printf("Hello, %s Wilcox!\n", family[num]);
    num +=1;
}
    return 0;
}