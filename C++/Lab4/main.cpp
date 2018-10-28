//17 вариант
#include <iostream>
#include <cstdlib>
#include "Polyline.h"

using namespace std;

int main() {
    vector<int> coords;
    for (int i=0; i< 5; i++) {
        coords.push_back(rand()%7);
    }
    Point x1(coords);
    coords[0] = 42;
    coords[1] = 999;
    Point x2(coords);

    vector<int> coords2;
    for (int i=0; i< 5; i++) {
        coords2.push_back(rand()%100);
    }
    Polyline <Point> line1;
    Polyline<Point> line2;
    Point y1(coords2);
    coords2[1]=0;
    coords2[3]=76;
    Point y2(coords2);
    line1 << x1;
    line1 << x2;
    line2 << y1;
    line2 << y2;
	cout << line1 << endl;
    cout << line2 << endl;
    cout << "number of points of line1: " <<line1.count() <<endl;
    cout << "number of points of line2: " <<line2.count() <<endl;
    cout << "Check dist method in Point between x1 & y1: " << x1.dist(y1) <<endl;
    cout << "line1>line2? Ans: " <<(line1>line2) << endl;
    cout << "line1==line2? Ans: " <<(line1==line2) << endl;
    cout << "line1!=line2? Ans: " <<(line1!=line2) << endl;
}
