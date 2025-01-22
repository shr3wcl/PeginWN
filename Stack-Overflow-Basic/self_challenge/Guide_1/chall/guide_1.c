#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void init(int argc, char **argv, char **envp) {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(0x1E);
}

int main(int argc, char **argv, char **envp) {
    init(argc, argv, envp);
    char bof[16];
    int a = 0, b = 0, c = 0, d = 0;
    printf("Type something > ");
    read(0, bof, 0x32);

    printf("Value of a: %d\n", a);
    printf("Value of b: %d\n", b);
    printf("Value of c: %d\n", c);
    printf("Value of d: %d\n", d);

    if (a && b && c && d) {   
        system("cat flag.txt");
    }
    return 0;
}