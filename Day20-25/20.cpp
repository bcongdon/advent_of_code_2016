#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

void valid_ips(vector<pair<long, long> > &blocklist){
    // Sort blocklist by starting element    
    sort(blocklist.begin(), blocklist.end());
    stack<pair<long, long> > merged = stack<pair<long, long> >();
    merged.push(blocklist[0]);
    pair<long, long> top;
    // Merge overlapping ranges
    for(long i = 0; i < blocklist.size(); i++) {
        top = merged.top();
        if(top.second < blocklist[i].first){
            merged.push(blocklist[i]);
        }
        else if(top.second < blocklist[i].second){
            top.second = blocklist[i].second;
            merged.pop();
            merged.push(top);
        }
    }
    top = merged.top();
    merged.pop();
    long num_valid = (0x1L << 32) - 1 - top.second;
    long first_valid = top.first - 1;
    long old_lo = top.first;
    // Iterate through stack and find number of valid ip addresses
    while(!merged.empty()) {
        pair<long, long> i = merged.top();
        merged.pop();
        num_valid += old_lo - i.second - 1;
        if(old_lo > i.second + 1) {
            first_valid = i.second + 1;
        }
        old_lo = i.first;
    }
    cout << "Part 1: " << first_valid << endl;
    cout << "Part 2: " << num_valid << endl;
}

int main() {
    ifstream blFile;
    blFile.open("20.txt");
    string line;
    long lo, hi;
    vector<pair<long, long> > blocklist = vector<pair<long, long> >();
    while(!blFile.eof()) {
        blFile >> line;
        sscanf(line.c_str(), "%ld-%ld", &lo, &hi);
        blocklist.push_back(make_pair(lo, hi));
    }
    valid_ips(blocklist);
}