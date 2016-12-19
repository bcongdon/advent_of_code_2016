#include <math.h>
#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? a : b)


int elf_exchange(int n) {
    int b = 0;
    int t = n;
    while(t != 0) {
        b ++;
        t >>= 1;
    }
    n = n ^ (0x1 << (b-1));
    n = (n << 1) | 0x1;
    return n;
}

int elf_exchange_2(long n) {
    long l = (log2l(n) / log2l(3));
    long i = pow(3, l);
    return n == i ? n : MAX(n - i, 2*n - 3*i);
}

int main() {
    printf("Part 1: %d\n", elf_exchange(3005290));
    printf("Part 2: %d\n", elf_exchange_2(3005290));
}