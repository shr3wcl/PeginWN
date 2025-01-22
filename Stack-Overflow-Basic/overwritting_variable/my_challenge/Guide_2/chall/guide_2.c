#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int init(int argc, char **argv, char **envp){
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    setbuf(stdin, NULL);
}

int main(int argc, char **argv, char **envp)
{
    init(argc, argv, envp);
    char buf[0x20];
    int a = 0, b = 0, c = 0;
    printf("Type something again > ");
    read(0, buf, 0x40);
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("c = %d\n", c);
    if (c == 1633771873) {
        printf("c is correct\n");
        if (b == 1633771890) {
            printf("b is correct\n");
            if (a == 0x13371337) {
                printf("a is correct\n");
                system("cat flag.txt");
            }
        }
    }
    return 0;
}
