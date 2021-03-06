#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Point {
public:
    Point(vector<int> &coords);
    double dist(Point point);
    friend ostream& operator<< (ostream& os, Point p) {
        os << "(" << p.coords[0];
        for (int i=1; i<p.coords.size(); i++) {
            os << ", " << p.coords[i];
        }
        os << ")";
        return os;
    }
private:
    vector<int> coords;
};

Point::Point(vector<int>& coords) {
    this->coords = coords;
}

double Point::dist(Point point) {
    int v=0;
    for (int i=0; i<point.coords.size(); i++) {
        v+=(this->coords[i]-point.coords[i])*(this->coords[i]-point.coords[i]);
    }
    return sqrt(v);
}

template<typename Point>
class Polyline {
private:
    vector<Point> line;
    double dist;
public:
	Polyline <Point>& operator<< (Point& otherPoint);
	Polyline <Point>& operator>> (Point& otherPoint);
    Point& operator[] (int i);
    int count();
    double size();
	bool operator== (const Polyline<Point>& otherLine);
	bool operator!= (const Polyline<Point>& otherLine);
    bool operator< (const Polyline<Point>& otherLine);
    bool operator> (const Polyline<Point>& otherLine);
    bool operator<= (const Polyline<Point>& otherLine);
    bool operator>= (const Polyline<Point>& otherLine);
    friend ostream& operator<< (ostream& os, Polyline<Point>& p) {
        os << "length: " << p.dist << endl << "line: " ;
        os << p[0];
        for (int i = 1; i < p.size(); ++i) os << ", " << p[i];
        return os;
    }
};

template<typename Point>
double Polyline<Point>::size() {
    return line.size();
}

template<typename Point>
Polyline <Point>& Polyline <Point>::operator<< (Point& otherPoint) {
    line.insert(line.begin(), otherPoint);
    dist += otherPoint.dist(line[0]);
    return *this;
}

template<typename Point>
Polyline <Point>& Polyline <Point>::operator>> (Point& otherPoint) {
    line.push_back(otherPoint);
    dist+=otherPoint.dist(line[line.size()-1]);
    return *this;
}

template<typename Point>
Point& Polyline<Point>::operator[] (int i) {
    return line[i];
}

template<typename Point>
int Polyline<Point>::count() {
    return line.size();
}

template<typename Point>
bool Polyline <Point>::operator== (const Polyline <Point>& otherLine) {
    return (this->dist == otherLine.dist);
}

template<typename Point>
bool Polyline <Point>::operator!= (const Polyline <Point>& otherLine) {
    return (this->dist != otherLine.dist);
}

template<typename Point>
bool Polyline <Point>::operator< (const Polyline<Point>& otherLine) {
    return (this->dist < otherLine.dist);
}

template<typename Point>
bool Polyline <Point>::operator<= (const Polyline<Point>& otherLine) {
    return (this->dist <= otherLine.dist);
}

template<typename Point>
bool Polyline <Point>::operator> (const Polyline<Point>& otherLine) {
    return (this->dist > otherLine.dist);
}

template<typename Point>
bool Polyline <Point>::operator>= (const Polyline<Point>& otherLine) {
    return (this->dist >= otherLine.dist);
}
