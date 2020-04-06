#include <stdio.h>
int main()
{
    int T, X, i;
    scanf("%d", &T);
    for(i = 0; i < T; i++)
    {
        scanf("%d", &X);
        if (X % 4 == 0)
            printf("1\n");
        else if (X % 4 == 1)
            printf("7\n");
        else if (X % 4 == 2)
            printf("9\n");
        else if (X % 4 == 3)
            printf("3\n");
    }
    return 0;
}
