#include <stdio.h>

int main(void)
{
    int a, b, c, d;
    
    scanf("%i %i", &a, &b);
    scanf("%i %i", &c, &d);

    printf("%i", ((c - a) * 2) + ((d - b) * 2));

}