#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>
#include <cfloat>
#include <assert.h>
using namespace std;

vector<string> split2(const string &line, char delimiter) {
    vector<string> tokens;
    size_t start = 0;
    size_t end = line.find(delimiter);

    while (end != string::npos) {
        tokens.push_back(line.substr(start, end - start));
        start = end + 1;
        end = line.find(delimiter, start);
    }

    tokens.push_back(line.substr(start)); // Add the last token
    return tokens;
}

string transformLine(string line){
    vector<string> tokens = split2(line, ';');

    //Extract datetime and remove quotes 
    vector<string> datetime_str = split2(tokens[1].substr(1, tokens[1].length() - 2), 'T');

    vector<string> date = split2(datetime_str[0], '-');
    vector<string> time = split2(datetime_str[1], ':');

    // Remove leading zeros from date and time components
    if (date[1][0] == '0') date[1].erase(0, 1);
    if (date[2][0] == '0') date[2].erase(0, 1);
    if (time[0][0] == '0') time[0].erase(0, 1);
    if (time[1][0] == '0') time[1].erase(0, 1);

    string outDateTime = date[2] + ',' + date[1] + ',' + time[0] + ',' + time[1];
    
    string sugar = tokens[7].substr(1, tokens[7].length() - 2);

    // Replace comma with dot in sugar value
    for (char &ch : sugar) {
        if (ch == ',') {
            ch = '.';
        }
    }

    if (sugar == "Vysoké") {
        sugar = "Vysoke";
    } else if (sugar == "Nízke") {
        sugar = "Nizke";
    }

    return outDateTime + ',' + sugar;

}

void toCSV(vector<string> &lines){
    ofstream fileOUT("output.csv");
    assert(fileOUT.is_open());
    string header = "Day,Month,Hour,Min,Sug";
    fileOUT << header << endl;
    for (const string &line : lines){
        fileOUT << line << endl;
    }

    fileOUT.close();
}

void editFile(string filename){
    ifstream fileIN(filename);
    assert(fileIN.is_open());

    vector<string> transformedLines;
    string line;

    
    
    // Skip the first 12 lines
    for (int i = 0; i < 12 && getline(fileIN, line); ++i) {
        // Do nothing, just skip these lines
    }

    while (getline(fileIN, line)){
        transformedLines.push_back(transformLine(line));
    }

    fileIN.close();
    toCSV(transformedLines);
}

void convertFile(){
    cout << "enter the file name: ";
    string filename;
    cin >> filename;

    editFile(filename);
}

