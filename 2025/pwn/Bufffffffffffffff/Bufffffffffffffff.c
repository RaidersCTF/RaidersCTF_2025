#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    char buf[12];
    int is_authorized = 0;

    printf("Enter password:");
    fflush(stdout);
    read(0, buf, 0x12);

    if (is_authorized) {
        puts("RaidersCTF{XXXXXXXXXX}");
    } else {
        puts("Incorrect password. Access denied!");
    }

    return 0;
}