#include <stdio.h>
//our data port and status reg should be global scope
unsigned char *data_p = (unsigned char *)0x10A4;
unsigned char *status_r = (unsigned char *)0x10A5;

void write_serial(unsigned char *data, int size) {
    int i;
    for (i = 0; i < size; i++) {
        while ((*status_r & 0x10) == 0x10) {
            // check if bit 4 in status is 1
        }
        // safe to write
        *data_p = data[i];
    }
}

