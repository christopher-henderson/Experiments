#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

int main() {
    int ceiling = 1000000;
    int* primes = (int*) malloc(ceiling*sizeof(int));
    primes[0] = 2;
    int test = 3;
    int needed = ceiling - 1;
    double sqroot;
    int divisor;
    bool isPrime;
    while (needed > 0) {
        isPrime = true;
        sqroot = sqrt(test);
        int index = 0;
        int max = ceiling-needed;
        while (index < max && isPrime) {
            divisor = primes[index];
            if (divisor > sqroot)
                break;
            else if (test % divisor == 0)
                isPrime = false;
            else
                index ++;
        }
        if (isPrime) {
            primes[max] = test;
            needed --;
        }
        test = test + 2;
    }
    printf("%u", primes[ceiling - 1]);
}

