//17 вариант
#include <iostream>
#include "Polyline.h"

using namespace std;

int main() {
    Polyline <float> line1;
    Point <float> x1(1,3);
    Point <float> x2(2,2);
    line1 << x1 ;
    line1 << x2;
	cout << line1 << endl;
    Polyline <float> line2;
    Point<float> y1 (2.1, 3.45);
    line2 <<y1;
    cout << "Number of points of line1: " <<line1.count() <<endl;
    cout <<(line1<line2)<<endl;
    cout <<"Line1[1]: "<< line1[1] <<endl;

}
