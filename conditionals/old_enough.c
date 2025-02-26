// James Wilcox, Old Enough C
#include <stdio.h>
#include <string.h>

int main(void){
    int age;
    char canvote[8];
    char candrive[8];
    char canlearn[8];
    char canschool[8];
printf("How old are you? ");
    scanf("%d", &age);
if (age >= 18){
   strcpy(canvote, "can");
}
else{
    strcpy(canvote, "can't");
} 
if (age >= 16){
   strcpy(candrive, "can");
}
else{
    strcpy(candrive, "can't");
} 
if (age >= 15){
   strcpy(canlearn, "can");
}
else{
    strcpy(canlearn, "can't");
} 
if (age >= 5){
   strcpy(canschool, "can");
}
else{
    strcpy(canschool, "can't");
} 
printf("You %s vote, %s drive, %s have a learner's permit, and %s go to school", canvote, candrive, canlearn, canschool);
    return 0;
}