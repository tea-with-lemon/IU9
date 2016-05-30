#include <iostream>
#include <iterator>
#include <string>

#include "parser.h"

using namespace std;

int main() {
	string text((istreambuf_iterator<char>(cin)),
			(istreambuf_iterator<char>()));
	try {
		parser::parse(text);
	} catch (parser::coord &pos) {
		cout << "syntax error at " << pos.line << ", " << pos.col << endl;
		return 1;
	}

	cout << "success" << endl;
	return 0;
}
Status API Training Shop Blog About
