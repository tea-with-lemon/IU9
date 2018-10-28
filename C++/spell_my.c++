#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

set<string> CreateBigrammSet(string str);

double DegreeOfSimilarity(set<string> a, set<string> b);

int main() {
    ifstream file("count_big.txt");
    map<string, pair<set<string>, int>> dict;
    string line;
    while (file) {
        int p;
        file >> line >> p;
        dict.emplace(line, make_pair(CreateBigrammSet(line), p));
    }
    do {
        string ans;
        cin >> line;
        ans = line;
        double sim = -1;
        int p =0;
        set<string> bigramms=CreateBigrammSet(line);
        for (auto i : dict) {
            double c = DegreeOfSimilarity(bigramms, i.second.first);
            if (c > sim || (c == sim && i.second.second > p) || (c == sim && i.second.second == p && i.first < ans)) {
                sim = c;
                ans = i.first;
                p = i.second.second;
      }
    }
    if (cin) cout << ans << endl;
  }
  while (cin);
  file.close();
  return 0;
}
set<string> CreateBigrammSet(string str) {
    set<string> bis;
    if (str.length() <= 2) {
		bis.emplace(str);
		return bis;
	}
    for (auto i = 0; i<str.size()-1; i++) {
        bis.emplace(string{str[i], str[i + 1]});
    }
    return bis;
}
double DegreeOfSimilarity(set<string> a, set<string> b) {
    set<string> c;
    set_intersection(a.begin(),a.end(),b.begin(), b.end(),inserter(c, c.begin()));
    return (double) c.size() / (a.size() + b.size() - c.size());
}
