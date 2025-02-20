// James Wilcox, Update Hello World C
#include <stdio.h>

int name1 = hello("1");
int name2 = hello("2");
int name3 = hello("3");
int name4 = hello("4");
int name5 = hello("5");

char hello(int number){
    printf("Tell me person %d's name:\n", number);
    return 0;
}
