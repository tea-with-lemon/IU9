//
// Created by alena on 4/28/16.
//

#include <iostream>
#include "BreakLineA.h"

int BreakLineA::numPoints() {
    return line.size();
}

pair<int,int> BreakLineA::sizeMinRect() {
    if (numPoints()==0) return make_pair(0,0);
    int minX=line[0]->x,minY=line[0]->y,maxX=line[0]->x,maxY=line[0]->y;
    int height, width;
    for (auto point: line) {
        if (point->x<minX) minX=point->x;
        if (point->y<minY) minY=point->y;
        if (point->x>maxX) maxX=point->x;
        if (point->y>maxY) maxY=point->y;
    }
    height=maxY-minY;
    width=maxX-minX;
    return make_pair(width, height);
}

Point* BreakLineA::operator[](int i) {
    if (i>numPoints()) cout << "This point is not exist! Index: " << i <<endl;
    else return line[i];
    return NULL;
}

void BreakLineA::enterNew(Point *a, int index) { line.insert(line.begin()+index, a); }

BreakLineA::~BreakLineA() { for (auto point: line) delete point; }

BreakLineA::BreakLineA(const BreakLineA &obj) {
    this->line.clear();
    for (auto point: obj.line) {
        Point* newPoint=new Point(point->x, point->y);
        enterNew(newPoint, numPoints());
    }
}

BreakLineA & BreakLineA::operator= (const BreakLineA &value) {
    this->line.clear();
    for (auto point: value.line) {
        Point* newPoint=new Point(point->x, point->y);
        enterNew(newPoint, numPoints());
    }
}
