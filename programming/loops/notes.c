// James Wilcox, Loops Notes C
#include <stdio.h>
#include <string.h>

int main(void){
// What is a loop?
    // A section of code that repeats

// What are the two types of loops?
    // For loops
    int x;
    for(x = 0; x < 10; x++){
        printf("Hello\n");
    }

    // While loops
    int i=1;
    while(i < 10){
        printf("%d\n", i);
        i++;
    }

// What is iteration
    // The act of repitition

// What are lists? 
    // A bunch of values in the same variable
    // Reference to iteration as a specific time through the loop

// How do you make lists in C (arrays)?
    int grades[] = {97, 88, 79, 100, 94, 64, 54};
    printf("%d\n", grades[4]);
    // In the brackets we set how long the list will be, unless list is set
    // Data type is whatever is in the list
    // List items in {} with , between each item
    // Index number in brackets
    grades[2] = 87;

    // How to get the size of an arrray (list)
    // This is amount of bytes-----------------------------------vvvvvvvvvvvvv
    printf("The number of bytes that Grades takes up is %lu\n", sizeof(grades));
    int length = sizeof(grades) / sizeof(grades[0]);
    if(length < 1 || length > 1){
        printf("This item takes up %d bytes\n", length);
    }else{
        printf("This item takes up 1 byte\n");
    }

// How do you make for loops in C?
// In () 1 starting point 2 go until point 3 count by
    int t;
    for(t = 0; t < 10; t += 2){
        printf("%d\n", t);
    }
    int l;
    for(l = 0; l < length; l++){
        printf("%d\n", grades[l]);
    }

// How do you make while loops in C?
    // Variable sets up start point
    // While line sets up stop point
    int itratr = 0;
    while(itratr <= 100){
        printf("%d\n", itratr);
        // Sets what it counts by
        itratr += 10;
    }

    char movies[][20] = {"Cinderella", "Smurfs", "Transformers" ,"Cars", "Up", "1984"};
    int mlength = sizeof(movies) / sizeof(movies[0]);
    int m = 0;
    while(m < mlength){
        printf("%s\n", movies[m]);
        m++;
    }

    return 0;
}