// James Wilcox, Financial Calculator C
#include <stdio.h>
#include <math.h>

char income = input("what is your monthly income\n");

char rent = input("What is your monthly expense for housing?\n");

char utilities = input("What are your monthly expenses for utilities?\n");

char groceries = input("What are your monthly expenses for groceries?\n");

char transportation = input("What are your monthly expenses for transportation?\n");

char savings = income/10;

char spending = income - rent - utilities - groceries - transportation - savings;

char rentpercent = rent/income*100;

char utilitiespercent = utilities/income*100;

char groceriespercent = groceries/income*100;

char transportationpercent = transportation/income*100;

char savingspercent = savings/income*100;

char spendingpercent = spending/income*100;

int main(void){

printf("Hello! This is a program for calculating your budget and finances!");

printf(income);

printf(rent);

printf(utilities);

printf(groceries);

printf(transportation);

printf("Every month you save ", savings);

printf("Every month you can spend", spending);

printf("You spend $", rent, "on rent and that is ", rentpercent , "percent of your income");

printf("You spend $", utilities, "on utilties and that is ", utilitiespercent, "percent of your income");

printf("You spend $", groceries, "on groceries and that is ", groceriespercent, "percent of your income");

printf("You spend $", transportation, "on transportation and that is ", transportationpercent, "of your income");

printf("You spend $", savings, "on savings and that is ", savingspercent, "percent of your income");

printf("You spend $", spending, "on spending and that is ", spendingpercent, "percent of your income");
    return 0;
}