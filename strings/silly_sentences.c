// James Wilcox, Silly Sentences C
#include <stdio.h>

char name[20];
char color[20];
char texture[20];
char toy[20];
char flavor[20];
char transportation[20];

int main(void){
    printf("What is a name?\n");
    scanf("%s", name);

   printf("Give me a color: \n");
   scanf("%s", color);

   printf("Name a texture: \n");
   scanf("%s", texture);

   printf("What is your favorite toy?\n");
   scanf("%s", toy);
   
   printf("What is a flavor?\n");
   scanf("%s", flavor);

   printf("What is a means of transportation?\n");
   scanf("%s", transportation);
   printf("You and your friend, %s ", name, "go out to play in the beautiful %s", color, "grass, but on the way, you find stinky Joe playing by himself in the sewers, drinking %s",  flavor, "flavored %s", texture, "water from the ceiling. You and %s",  name, "shudder and continue to find the coveted %s",  toy, ". After a while, you get tired of walking and see an old man riding an old %s",  transportation, ". You and %s", name, " beat him up, take his %s", transportation, "", and go home.");
    return 0;
}