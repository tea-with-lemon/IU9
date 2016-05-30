#ifndef PARSER_H_
#define PARSER_H_

#include <string>
namespace parser {

struct coord {
	int offs;
	int line;
	int col;
};

void parse(std::string text) throw (coord);

}

#endif /* PARSER_H_ */
