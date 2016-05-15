#include <iostream>

using namespace std;

template <char>
struct selectType { typedef char type; };

template <> // специализация для параметра 's' -- type == short
struct selectType<'s'> { typedef short type; };

template <> // специализация для параметра 'i' -- type == integer
struct selectType<'i'> { typedef int type; };
template <int L, int H, int N, char t = (H - N < 256) ? 'c' : (H - N < 65536) ? 's' : 'i' >
class IntVector {
private:
  typedef typename selectType<t>::type T;
  T* array;
public:
  IntVector() {
    cout << "Внутри конструктора IntVector" << endl;
    cout << "Размер элемента массива: " << sizeof(T) << endl;
    array = new T[N];
  }
  ~IntVector() { delete[] array; }
};

int main() {
  IntVector<0, 10, 5> charArray;
  IntVector<0, 1000, 5> shortVector;
  IntVector<0, 100000, 5> intVector;
  return 0;
}
