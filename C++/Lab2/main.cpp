#include <iostream>
#include "BreakLineA.h"
#include "BreakLineB.h"

using namespace std;

void printLine(BreakLineA line) {
    for (int i=0; i < line.numPoints(); i++) {
        cout << "Point x: " << line[i]->x << " " << "Point y: " << line[i]->y <<endl;
    }
}

void printLine(BreakLineB line) {
    for (int i=0; i < line.numPoints(); i++) {
        cout << "Point x: " << line[i]->x << " " << "Point y: " << line[i]->y <<endl;
    }
}

void addPoints(BreakLineA line) {
    line.enterNew(new Point(10,10), 0);
    printLine(line);
    cout << "width: " << line.sizeMinRect().first << " height: " << line.sizeMinRect().second << endl;
}

void addPoints(BreakLineB* line) {
    line->enterNew(new Point(9,9), 0);
    printLine(*line);
    cout << "width: " << line->sizeMinRect().first << " height: " << line->sizeMinRect().second << endl;
}


int main() {
    BreakLineA testA;
    BreakLineB testB;

    testA.enterNew(new Point(0,2), 0);
    testA.enterNew(new Point(-7,5), 1);
    testA.enterNew(new Point(3,-2), 2);
    testA.enterNew(new Point(8,0), 3);

    testB.enterNew(new Point(1,3), 0);
    testB.enterNew(new Point(-8,6), 1);
    testB.enterNew(new Point(5,0), 2);
    testB.enterNew(new Point(10,1), 3);

    cout << "Line A:" << endl;
    printLine(testA);
    cout << "MinRect:" << endl;
    cout << "width: " << testA.sizeMinRect().first << " height: " << testA.sizeMinRect().second << endl;
    addPoints(testA);
    printLine(testA);

    cout << "Line B:" << endl;
    printLine(testB);
    cout << "MinRect:" << endl;
    cout << "width: " << testB.sizeMinRect().first << " height: " << testB.sizeMinRect().second << endl;
    addPoints(&testB);
    printLine(testB);

    BreakLineA testA1;
    BreakLineB testB1;

    testA1=testA;
    testB1=testB;
    cout << "Copy testA: " << endl;
    printLine(testA1);
    cout << "Copy testB: " << endl;
    printLine(testB1);

    return 0;
}
