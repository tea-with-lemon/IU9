#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

template <typename T>
class Point {
public:
    Point(T x, T y);
    double dist(Point point);
    friend ostream& operator<< (ostream& os, Point<T> p) {
        os << "(" << p.x << ", "<< p.y << ")";
        return os;
    }
private:
    T x, y;
};

template <typename T>
double Point<T> :: dist(Point<T> point) {
    return sqrt(((this->x-point.x)*(this->x-point.x))+(this->x-point.x)*(this->x-point.x));
}

template <typename T>
Point<T>::Point(T x, T y) {
    this->x=x;
    this->y=y;
}

template<typename T>
class Polyline {
private:
    vector<Point<T>> line;
    double dist;
public:
	Polyline <T>& operator<< (Point<T>& otherPoint);
	Polyline <T>& operator>> (Point<T>& otherPoint);
    Point<T>& operator[] (int i);
    int count();
    double size();
	bool operator== (const Polyline<T>& otherLine);
	bool operator!= (const Polyline<T>& otherLine);
    bool operator< (const Polyline<T>& otherLine);
    bool operator> (const Polyline<T>& otherLine);
    bool operator<= (const Polyline<T>& otherLine);
    bool operator>= (const Polyline<T>& otherLine);
    friend ostream& operator<< (ostream& os, Polyline<T>& p) {
        os << "length :" << p.dist << "   " << "line : " ;
        for (int i = 0; i < p.size(); ++i) os << p[i] << " ";
        return os;
    }
};

template<typename T>
double Polyline<T>::size() {
    return line.size();
}

template<typename T>
Polyline <T>& Polyline <T>::operator<< (Point<T>& otherPoint) {
    line.insert(line.begin(), otherPoint);
    if (!line.empty()) dist+=otherPoint.dist(line[1]);
    else dist =0;
    return *this;
}

template<typename T>
Polyline <T>& Polyline <T>::operator>> (Point<T>& otherPoint) {
    line.push_back(otherPoint);
    if (!line.empty()) dist+=otherPoint.dist(line[line.size()-1]);
    else dist =0;
    return *this;
}

template<typename T>
Point<T>& Polyline<T>::operator[] (int i) {
    return line[i];
}

template<typename T>
int Polyline<T>::count() {
    return line.size();
}

template<typename T>
bool Polyline <T>::operator== (const Polyline <T>& otherLine) {
    return (this->dist == otherLine.dist);
}

template<typename T>
bool Polyline <T>::operator!= (const Polyline <T>& otherLine) {
    return (this->dist != otherLine.dist);
}

template<typename T>
bool Polyline <T>::operator< (const Polyline<T>& otherLine) {
    return (this->dist < otherLine.dist);
}

template<typename T>
bool Polyline <T>::operator<= (const Polyline<T>& otherLine) {
    return (this->dist <= otherLine.dist);
}

template<typename T>
bool Polyline <T>::operator> (const Polyline<T>& otherLine) {
    return (this->dist > otherLine.dist);
}

template<typename T>
bool Polyline <T>::operator>= (const Polyline<T>& otherLine) {
    return (this->dist >= otherLine.dist);
}
