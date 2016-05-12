#ifndef LAB2_BREAKLINEB_H
#define LAB2_BREAKLINEB_H

#include <utility>
#include "Point.h"

using namespace std;

class BreakLineB {
private:
    Point** line;
    int num;
public:
    BreakLineB();
    int numPoints();
    pair<int,int> sizeMinRect();
    Point* operator[] (int i);
    void enterNew(Point* a, int index);
    ~BreakLineB();
    BreakLineB(const BreakLineB &obj);
    BreakLineB & operator= (const BreakLineB &value);
};


#endif //LAB2_BREAKLINEB_H
