// James Wilcox, Financial Calculator Update C
#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;

int main(void){
   printf("Hello, this is a program for calculating your monthly finances\n");
   float income, rent, utilities, groceries, transportation, savings, spending;
   float percentrent, percentutilities, percentgroceries, percenttransportation, percentspending;

   printf("What is your monthly income?\n");
   scanf("%f", &income);

   printf("What is your monthly rent?\n");
   scanf("%f", &rent);

   printf("What is your monthly cost of utilities?\n");
   scanf("%f", &utilities);

   printf("What is your monthly cost of groceries?\n");
   scanf("%f", &groceries);

   printf("What is your monthly cost of transportation?\n");
   scanf("%f", &transportation);

   savings = income/10;
   spending = income-rent-utilities-groceries-transportation-savings;

   percentrent = (rent/income) * 100;
   percentutilities = (utilities/income) * 100;
   percentgroceries = (groceries/income) * 100;
   percenttransportation = (transportation/income) * 100;
   percentspending = (spending/income) * 100;

   printf("The amount spent on rent is %.2f and that is %.2f percent of your income\n", rent, percentrent);
   printf("The amount spent on utilities is %.2f and that is %.2f percent of your income\n", utilities, percentutilities);
   printf("The amount spent on groceries is %.2f and that is %.2f percent of your income\n", groceries, percentgroceries);
   printf("The amount spent on transportation is %.2f and that is %.2f percent of your income\n", transportation, percenttransportation);

   printf("The money you have left for spending is %.2f, which is %.2f percent of your income\n", spending, percentspending);

   printf("The amount of money you have saved for future use is %.2f, which is 10 percent of your income\n", savings);
   return 0;
}