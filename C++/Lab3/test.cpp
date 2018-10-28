#include <iostream>

using namespace std;

template <char>
struct selectType { typedef char type; };
template <>
struct selectType<'s'> { typedef short type; };
template <>
struct selectType<'i'> { typedef int type; };

template <int L, int H, int N, char t = (H - N < 256) ? 'c' : (H - N < 65536) ? 's' : 'i' >
class IntVector {
private:
  typedef typename selectType<t>::type T;
  T* array;
  int low;
  int high;
public:
  IntVector(int* coords) {
    low=L;
    high=H;
    array=new T[N];
    for (int i=0; i<N; i++) {
      if (coords[i] < low || coords[i] > high) array[i]=0;
      else array[i]=coords[i]-L;
    }
  }
  ~IntVector() { delete[] array; }
  T operator [] (int index) const {
    if (index >= N) return (T)NULL;
    else return array[index]+low;
  }
  int getLow() { return low; }
  int getHigh() { return high; }
  //IntVector operator +
};

int main() {
  int array[2];
  array[0]=1105;
  array[1]=1002;
  IntVector<1000, 1010, 2> vec(array);
  cout << vec[0] << ' ' << vec[1] << endl;
  return 0;
}
