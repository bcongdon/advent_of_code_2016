#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

vector<string> read_file(string fname) {
    ifstream file(fname);
    string line;
    vector<string> lines;
    if(file.is_open()) {
        while(getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
    }
    return lines;
}

int max_idx(vector<int> const &v) {
    int idx = 0;
    for(int i = 1; i < v.size(); i++){
        if(v[idx] < v[i]) idx = i;
    }
    return idx;
}

int min_idx(vector<int> const &v) {
    int idx = -1;
    for(int i = 1; i < v.size(); i++){
        if((v[idx] > v[i] || idx < 0) && v[i] != 0) idx = i;
    }
    return idx;
}

string decrypt(vector<string> &lines, int part){
    string out = "";
    for(int i = 0; i < lines[0].length(); i++) {
        vector<int> counts(256, 0);
        for(int j = 0; j < lines.size(); j++) {
            counts[lines[j][i]] ++;
        }
        out += char((part == 1) ? max_idx(counts) : min_idx(counts));
    }
    return out;
}

int main() {
    vector<string> input_test = read_file("6-test.txt");
    vector<string> input = read_file("6.txt");

    assert(!decrypt(input_test, 1).compare("easter"));
    assert(!decrypt(input_test, 2).compare("advent"));

    printf("Part 1: %s\n", decrypt(input, 1).c_str());
    printf("Part 2: %s\n", decrypt(input, 2).c_str());
}
