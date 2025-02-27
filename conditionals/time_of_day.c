// James Wilcox, Time of Day C
#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds;

    seconds = time(NULL);
    printf("Seconds since January 1, 1970 = %d\n", seconds);

    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
   //printf("Current time and date is %s\n", asctime(timeinfo));

    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);
    if (hour >= 6 && hour <= 11){
   printf("Good Morning!");
    }
   else if (hour >= 12 && hour <= 16){
   printf("Good Afternoon!");
   }
   else if (hour >= 17 && hour <= 19){
   printf("Good Evening!");
   }
   else{
    printf("You should be in bed!");
   }
    return 0;
}