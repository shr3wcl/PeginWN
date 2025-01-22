#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int init(int argc, char **argv, char **envp){
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    setbuf(stdin, NULL);
}

void ret2win()
{
    system("/bin/cat flag.txt");
}

void vuln()
{
    char buf[0x10];
    printf("Type something\n");
    printf("> ");
    read(0, buf, 0x100);
}

int main(int argc, char **argv, char **envp)
{
    init(argc, argv, envp);
    vuln();
    return 0;
}