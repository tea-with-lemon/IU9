#ifndef LAB2_BREAKLINEA_H
#define LAB2_BREAKLINEA_H

#include <vector>
#include "Point.h"

using namespace std;

class BreakLineA {
private:
    vector <Point*> line;
public:
    int numPoints();
    pair<int,int> sizeMinRect();
    Point* operator[] (int i);
    void enterNew(Point* a, int index);
    ~BreakLineA();
    BreakLineA(const BreakLineA &obj);
    BreakLineA()  {};
    BreakLineA & operator= (const BreakLineA &value);
};

#endif //LAB2_BREAKLINEA_H
