// James Wilcox, Financial Calculator Update C
#include <stdio.h>  
#include <math.h>  
  
float get_expense(const char *name) {    
    float value;    
    printf("What is your monthly cost of %s?\n", name);    
    scanf("%f", &value);    
    return value;    
}    
    
float calculate_percentage(float part, float total) {    
    return (part / total) * 100;    
}    
    
int main(void) {    
    float income = 0.0;  
    float rent, utilities, groceries, transportation, savings, spending;  
  
    printf("What is your monthly income?\n");  
    scanf("%f", &income);  
  
    rent = get_expense("rent");    
    utilities = get_expense("utilities");    
    groceries = get_expense("groceries");    
    transportation = get_expense("transportation");    
  
    savings = income / 10; // 10% savings  
    spending = income - (rent + utilities + groceries + transportation + savings);  
  
    float percentrent = calculate_percentage(rent, income);  
    float percentutilities = calculate_percentage(utilities, income);  
    float percentgroceries = calculate_percentage(groceries, income);  
    float percenttransportation = calculate_percentage(transportation, income);  
    float percentspending = calculate_percentage(spending, income);  
  
    printf("The amount spent on rent is %.2f and that is %.2f percent of your income\n", rent, percentrent);  
    printf("The amount spent on utilities is %.2f and that is %.2f percent of your income\n", utilities, percentutilities);  
    printf("The amount spent on groceries is %.2f and that is %.2f percent of your income\n", groceries, percentgroceries);  
    printf("The amount spent on transportation is %.2f and that is %.2f percent of your income\n", transportation, percenttransportation);  
    printf("The money you have left for spending is %.2f, which is %.2f percent of your income\n", spending, percentspending);  
    printf("The amount of money you have saved for future use is %.2f, which is 10 percent of your income\n", savings);  
  
    return 0;    
}  
