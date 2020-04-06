#include <stdio.h>
int main()
{
    long double l;
    while(scanf("%Lf", &l) && l != 0)
    {
        printf("%0.6Lf\n", ((l - 3) / l));
    }
    return 0;
}
