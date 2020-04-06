#include <stdio.h>
#include <math.h>
int main(int argc, char *argv[])
{
    double C, I;
    int M;
    while(scanf("%lf", &C) != EOF){
        scanf("%lf", &I);
        scanf("%d", &M);
        double SIMPLES, COMPOSTO, X, DIFERENCA;
        SIMPLES = C * M * I;
        X = C * pow((1 + I), M);
        COMPOSTO = X - C;
        DIFERENCA = fabs(SIMPLES - COMPOSTO);
        printf("DIFERENCA DE VALOR = %.2lf\n", DIFERENCA);
		printf("JUROS SIMPLES = %.2lf\n", SIMPLES);
		printf("JUROS COMPOSTO = %.2lf\n", COMPOSTO);

    }
    return 0;
}
