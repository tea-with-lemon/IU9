#include <cstdio>
#include <iostream>
#include "BreakLineB.h"

BreakLineB::BreakLineB() {
    num=0;
    line=NULL;
}

BreakLineB::~BreakLineB() {
    for (int i=0; i<num; i++) {
        delete line[i];
    }
    delete[] line;
}

int BreakLineB::numPoints() {
    return num;
}

Point* BreakLineB::operator[](int i) {
    if (i>num) cout << "This point is not exist! Index: " << i <<endl;
    else return line[i];
    return NULL;
}

pair<int,int> BreakLineB::sizeMinRect() {
    if (num==0) return make_pair(0,0);
    int minX=line[0]->x,minY=line[0]->y,maxX=line[0]->x,maxY=line[0]->y;
    int height, width;
    for (int i=0; i<num; i++) {
        if (line[i]->x<minX) minX=line[i]->x;
        if (line[i]->y<minY) minY=line[i]->y;
        if (line[i]->x>maxX) maxX=line[i]->x;
        if (line[i]->y>maxY) maxY=line[i]->y;
    }
    height=maxY-minY;
    width=maxX-minX;
    return make_pair(width, height);
}

void BreakLineB::enterNew(Point *a, int index) {
    Point** newLine=new Point*[num+1];
    for (int i=0; i<index; i++) {
        newLine[i]=line[i];
    }
    newLine[index]=a;
    for (int j=index+1; j<num+1; j++) {
        newLine[j]=line[j-1];
    }
    delete[] line;
    line=newLine;
    num++;
}

BreakLineB::BreakLineB(const BreakLineB &obj) {
    num=obj.num;
    line=new Point*[num];
    for (int i=0; i<num; i++) {
        Point* newPoint=new Point(obj.line[i]->x, obj.line[i]->y);
        line[i]=newPoint;
    }
}

void BreakLineB::swap(BreakLineB &value) {
    Point** buff=new Point*[value.line->numPoints()];
    value.line=this->line;
    this->line=buff;
}

BreakLineB & BreakLineB::operator= (const BreakLineB &value) {
    if (this != &value) {
        BreakLineB tmp(value);
        this->swap(tmp);
    }
    return *this;
}
