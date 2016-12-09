#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROW_L 50
#define COL_L 6
#define SIZE 50 * 6

void print_display(char *disp){
    char out;
    for(int i = 0; i < SIZE; i++){
        if(i % 50 == 0 && i) printf("\n");
        out = disp[i] ? '#' : ' ';
        printf("%c", out);
    }
    printf("\n\n");
}

int sum_pixels(char *disp){
    int x = 0;
    for(int i = 0; i < SIZE; i ++) {
        if(disp[i]) x ++;
    }
    return x;
}

int posmod(int i, int n) {
    return (i % n + n) % n;
}

void decrypt(char* fname) {
    FILE *fp = fopen(fname, "r");
    char instr [100];
    char display [SIZE] = {0};
    while(fgets(instr, 100, fp) != NULL) {
        // Rect command
        if(strstr(instr, "rect")){
            char *num_seg = strstr(instr, " ") + 1;
            int x = atoi(strtok(num_seg, "x"));
            int y = atoi(strtok(NULL, "x"));
            // Fill in an x by y rectangle of pixels
            for(int i = 0; i < x; i++) {
                for(int j = 0; j < y; j++){
                    display[i + ROW_L * j] = 1;
                }
            }
        }
        // Rotate command
        else {
            char rc = strstr(instr, "column") == NULL;
            strtok(instr, "="); // Clear out before x/y=
            int loc = atoi(strtok(NULL, " "));
            strtok(NULL, " "); // Clear out " by "
            int amt = atoi(strtok(NULL, " "));

            // Row rotation
            if(rc) {
                char temp[ROW_L];
                for(int i = 0; i < ROW_L; i ++)
                    temp[i] = display[loc * ROW_L + posmod(i - amt, ROW_L)];
                for(int i = 0; i < ROW_L; i++)
                    display[loc * ROW_L + i] = temp[i];
            }
            // Column Rotation
            else {
                char temp[COL_L];
                for(int i = 0; i < COL_L; i ++)
                    temp[i] = display[loc + ROW_L * posmod(i - amt, COL_L)];
                for(int i = 0; i < COL_L; i ++)
                    display[loc + ROW_L * i] = temp[i];
            }
        }
    }
    printf("Part 1: %d\n", sum_pixels(display));
    printf("Part 2:\n");
    print_display(display);
}

int main() {
    decrypt("8.txt");
}