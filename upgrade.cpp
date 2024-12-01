#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cfloat>
#include <iomanip>
using namespace std;

int ID = 0;

struct sElement{
    int day;
    int month;
    int hour;
    int minute;
    float value;
};

struct sData{
    float m;
    float l;
    float e;
    float n;
};

struct sOutput{
    int id;
    int day;
    sData Ins;
    sData Sug;
};

vector<string> split(const string &line, char delimiter) {
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

sOutput proccesDay(vector<sElement> &days)
{
    sOutput result;
    sData Sug = {FLT_MAX, FLT_MAX, FLT_MAX, FLT_MAX}; // Initialize to maximum for finding minimum
    sData Ins = {0, 0, 0, 0}; // Initialize to 0 for calculated values

    // Iterate over elements for the day
    for (const auto &elem : days) {
        if (elem.hour >= 6 && elem.hour <= 9) { // Morning
            Sug.m = min(Sug.m, elem.value);
        } else if (elem.hour >= 11 && elem.hour <= 14) { // Lunch
            Sug.l = min(Sug.l, elem.value);
        } else if (elem.hour >= 16 && elem.hour <= 19) { // Evening
            Sug.e = min(Sug.e, elem.value);
        } else if (elem.hour >= 21 && elem.hour <= 23){ // Night
            Sug.n = min(Sug.n, elem.value);
        }
    }
    if (Sug.m == FLT_MAX) Sug.m = 0;
    if (Sug.l == FLT_MAX) Sug.l = 0;
    if (Sug.e == FLT_MAX) Sug.e = 0;
    if (Sug.n == FLT_MAX) Sug.n = 0;

    // Assign Insulin values based on Sug and provided thresholds
    // Morning
    Ins.m = (Sug.m < 7) ? 7 : (Sug.m > 15) ? 11 : 9;
    // Lunch
    Ins.l = (Sug.l < 7) ? 16 : (Sug.l > 15) ? 17 : 16;
    // Evening
    Ins.e = (Sug.e < 7) ? 16 : (Sug.e > 15) ? 18 : 17;
    // Night
    Ins.n = 19;

    // Populate result
    result.id = ID;
    ID++;
    result.day = days[0].day;
    result.Sug = Sug;
    result.Ins = Ins;

    return result;
}

void toCSV(vector<sOutput> &output){
    ofstream file("test1.csv");
    string result = "ID,Day,SugM,SugL,SugE,SugN,InsM,InsL,InsE,InsN\n"; // Initial header

    ostringstream oss; // Use ostringstream for formatting numbers
    // Accumulate the CSV data in a string
    for (auto &elem : output) {
        oss.str("");  // Clear previous contents

        // Format glucose values to one decimal place
        oss << fixed << setprecision(1) 
            << elem.id << "," << elem.day << ","
            << elem.Sug.m << "," << elem.Sug.l << ","
            << elem.Sug.e << "," << elem.Sug.n << ","
            // Ensure insulin values are whole numbers
            << static_cast<int>(elem.Ins.m) << "," 
            << static_cast<int>(elem.Ins.l) << ","
            << static_cast<int>(elem.Ins.e) << ","
            << static_cast<int>(elem.Ins.n) << "\n";

        result += oss.str();  // Append the formatted result to the string
    }

    // Write the accumulated data to the file at once
    file << result;
    file.close();
}

void manager(ifstream &data)
{
    string line;
    vector<sOutput> output;
    
    int date = -1;
    vector<sElement> day;
    day.reserve(312);  
    int i = 0;
    while (getline(data, line))
    {

        //i++;
        //cout<<i<<endl;
        vector<string> tokens = split(line, ',');
        
        // Parse the line tokens into the sElement structure
        sElement elem;
        elem.day = stoi(tokens[0]);
        elem.month = stoi(tokens[1]);
        elem.hour = stoi(tokens[2]);
        elem.minute = stoi(tokens[3]);

        // Handle special cases for glucose values (e.g., "Vysoké" or "Nízké")
        if (tokens[4] == "Vysoke")
            elem.value = 22.2;
        else if (tokens[4] == "Nizke")
            elem.value = 2.2;
        else
            elem.value = stof(tokens[4]); // Convert to float for numerical values

        if(date == -1)
        {
            date = elem.day;
        }
        
        if(date != elem.day)
        {
            //process day
            output.push_back(proccesDay(day));
            date = elem.day;
            day.clear();
        }
        

        day.push_back(elem);
    }
    toCSV(output);
    cout << "Done" << endl;
    
}

void loadFile()
{
    cout << "Name of file: ";
    string fileName;
    cin >> fileName;
    ifstream data(fileName);
    if (!data.is_open())
    {
        cout << "File not found" << endl;
        return;
    }
    getline(data, fileName);
    manager(data);
}

int main()
{
    loadFile();
}