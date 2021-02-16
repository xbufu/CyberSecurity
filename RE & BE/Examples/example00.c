#include <stdio.h>

void readInput(char *buf){
    int offset = 0;
    int ch = 0;
    
    while ((ch = getchar()) != EOF) {
        buf[offset++] = (char) ch;
    }
}

int main() {
    int pivot = 1234;
    char buffer[20];

    printf("buffer: %8p pivot: %8p\n", (void*)&buffer, (void*)&pivot);

    readInput(buffer);

    if (pivot == 0x10204030) printf("Congratulations! You win!\n");

    return 0;
}
