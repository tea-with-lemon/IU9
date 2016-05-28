//17 вариант
#include <iostream>
#include "Polyline.h"

using namespace std;

int main() {
    std::vector<int> coords;
    for (int i=0; i< 5; i++) {
        coords.push_back(rand()%7);
    }
    Point x1(coords);
    Polyline <Point> line1;
    line1 << x1;
	cout << line1 << endl;
    //Polyline <int> line2;
    std::vector<int> mas1;
    mas1.push_back(2);
    mas1.push_back(3);
    Point y1 (mas1);
    //line2 <<y1;
    cout << "Number of points of line1: " <<line1.count() <<endl;
    //cout <<(line1<line2)<<endl;
    cout <<"Line1[1]: "<< line1[1] <<endl;

}
