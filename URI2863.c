#include <stdio.h>
int main()
{
    int size, c;
    double array[100], minimum;
    while(scanf("%d",&size) != EOF)
    {
        for (c = 0; c < size; c++)
        scanf("%lf", &array[c]);
    minimum = array[0];
    for (c = 1; c < size; c++)
    {
        if (array[c] < minimum)
        {
           minimum = array[c];
        }
    }
    printf("%0.2lf\n", minimum);
    }
    return 0;
}
