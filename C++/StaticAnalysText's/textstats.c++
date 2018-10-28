#include <string>
#include <vector>
#include <unordered_set>
#include <set>
#include <map>

using namespace std;

void get_tokens(const string &s,const unordered_set<char> &delimiters,vector<string> &tokens) {
    string xs="";
    for (int i = 0; i < s.size(); i++) {
        if (delimiters.find(s[i]) == delimiters.end()) xs+=tolower(s[i]);
        else {
            if (!xs.empty()) tokens.emplace_back(xs);
            xs = "";
        }
    }
    if (!xs.empty()) tokens.emplace_back(xs);
}
void get_type_freq(const vector<string> &tokens, map<string, int> &freqdi) {
    for (auto t:tokens) freqdi[t]++;
}
void get_x_length_words(const vector<string> &wtypes,int x,vector<string> &words) {
    for (auto w:wtypes) {
        if (w.size() >= x) words.emplace_back(w);
    }
}
void get_types(const vector<string> &tokens,vector<string> &wtypes) {
    set<string> dict(tokens.begin(), tokens.end());
	for (auto d : dict) wtypes.emplace_back(d);
}
void get_x_freq_words(const map<string, int> &freqdi,int x,vector<string> &words) {
    for (auto f : freqdi){
        if (f.second >= x) words.emplace_back(f.first);
    }
}
void get_words_by_length_dict(const vector<string> &wtypes,map<int, vector<string> > &lengthdi) {
    for (auto w:wtypes) lengthdi[w.size()].emplace_back(w);
}
