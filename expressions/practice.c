// James Wilcox, Expressions Practice
#include <stdio.h>
#include <math.h>

int par1 = (7-24/8*4+6);
int par2 = (18/3-7+2*5);
int par3 = (6*4/12+72/8-9);
int par4_1 = (17-6/2);
int par4_2 = (4*3);
int par5_1 = (1*4-2/2);
int par5_2 = (6+2-3);
int par6_1 = (3-4*7);
int par6_2 = (-2*24/6);
int par7_1 = pow(5, 2);
int par7_2 = pow(2, 2)

int main(void){
    printf("%d\n", par1);
    printf("%d\n", par2);
    printf("%d\n", par3);
    printf("%d\n", par4_1 + par4_2);
    printf("%d\n", -2*(par5_1) + par5_2);
    printf("%d\n", -1*par6_1/5 - par6_2);
    printf("%d\n", par7_1);
    return 0;
}
