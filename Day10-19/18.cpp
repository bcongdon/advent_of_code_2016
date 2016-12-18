#import <string>
#import <iostream>
#include <cassert>
using namespace std;

int num_safe_tiles(string inp, int rows) {
    int num_safe = 0;
    bool *curr = new bool[inp.length()];
    for(int i = 0; i < inp.length(); i++){
        curr[i] = inp[i] == '^';
        if(inp[i] != '^') {
            num_safe ++;
        }
    }
    for(int r = 0; r < rows - 1; r++) {
        bool *n_row = new bool[inp.length()];
        for(int i = 0; i < inp.length(); i++){
            if((i > 0 && curr[i-1]) ^ (i+1 < inp.length() && curr[i+1])) {
                n_row[i] = true;
            }
            else {
                n_row[i] = false;
                num_safe ++;
            }
        }
        delete[] curr;
        curr = n_row;
    }
    delete[] curr;
    return num_safe;
}

int main() {
    assert(num_safe_tiles("..^^.", 3) == 6);
    assert(num_safe_tiles(".^^.^.^^^^", 10) == 38);
    string input = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.";
    cout << "Part 1: " << num_safe_tiles(input, 40) << endl;
    cout << "Part 2: " << num_safe_tiles(input, 400000) << endl;

}