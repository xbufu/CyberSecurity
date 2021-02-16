#include <stdio.h>
#include <string.h>


void printChar(const char *buf) {
    printf("Character: %c\n", buf[0]);
}

void printStr(const char *buf) {
    printf("String: %s\n", buf);
}

int main(int argc, char **argv) {
    extern int system(char *);
    void (*fctPtr)(char*) = (void(*)(char*))&system;
    char buffer[256];

    if(argc != 3) {
        fprintf(stderr, "Error, wrong number of arguments. \n");
        return 0;
    }

    if(strlen(argv[2]) > 2)
            fctPtr = (void(*)(char*))&printStr;
    else
            fctPtr = (void(*)(char*))&printChar;
    
    strcpy(buffer, argv[1]);
    fctPtr(argv[2]);
    return 0;
}
