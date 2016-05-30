#include "parser.h"

#include <iostream>

namespace parser {

enum tag_t {
	IDENT, NUMBER, END, COMA, EQUALS, LBRACE, RBRACE, ENUM, SEMICOLON
};

struct context {
	std::string text;
	coord cur;
	coord next;
	coord start;
	tag_t tag;
};

int next_char(context& ctx) {
	ctx.cur = ctx.next;
	if (ctx.next.offs == ctx.text.length())
		return -1;
	char c = ctx.text[ctx.next.offs++];
	if (c == '\n') {
		ctx.next.line++;
		ctx.next.col = 1;
	} else {
		ctx.next.col++;
	}
	return c;
}

void next_token(context& ctx) throw (coord) {
	int c;
	while (isspace(c = next_char(ctx)))
		;

	ctx.start = ctx.cur;
	switch (c) {
	case -1:
		ctx.tag = END;
		break;
	case '{':
		ctx.tag = LBRACE;
		break;
	case '}':
		ctx.tag = RBRACE;
		break;
	case '=':
		ctx.tag = EQUALS;
		break;
	case ',':
		ctx.tag = COMA;
		break;
	case ';':
		ctx.tag = SEMICOLON;
		break;
	default:
		if (isalpha(c)) {
			std::string tmp = "";
			tmp += c;
			while (isalnum(c = next_char(ctx)))
				tmp += c;
			if (tmp == "enum")
				ctx.tag = ENUM;
			else
				ctx.tag = IDENT;
			if (!isspace(c)) {
				ctx.next.offs--;
				ctx.next.col--;
			}
		} else if (isdigit(c)) {
			while (isdigit(c = next_char(ctx)))
				;
			ctx.tag = NUMBER;
			if (!isspace(c)) {
				ctx.next.offs--;
				ctx.next.col--;
			}
		} else {
			throw ctx.cur;
		}
	}
}

void parse_decl(context& ctx) throw (coord);
void parse_enum(context& ctx) throw (coord);
void parse_list(context& ctx) throw (coord);
void parse_item(context& ctx) throw (coord);
void parse_vars(context& ctx) throw (coord);

void parse(std::string text) throw (coord) {
	context ctx { text };
	ctx.next = coord { 0, 1, 1 };
	next_token(ctx);
	parse_decl(ctx);
	if (ctx.tag != END)
		throw ctx.start;
}

void parse_decl(context& ctx) throw (coord) {
	parse_enum(ctx);
	if (ctx.tag == IDENT)
		parse_vars(ctx);
	if (ctx.tag != SEMICOLON)
		throw ctx.start;
	next_token(ctx);

}

void parse_enum(context& ctx) throw (coord) {
	if (ctx.tag != ENUM)
		throw ctx.start;
	next_token(ctx);
	if (ctx.tag != IDENT)
		throw ctx.start;
	next_token(ctx);
	if (ctx.tag != LBRACE)
		throw ctx.start;
	next_token(ctx);
	parse_list(ctx);
	if (ctx.tag != RBRACE)
		throw ctx.start;
	next_token(ctx);
}

void parse_list(context& ctx) throw (coord) {
	parse_item(ctx);
	while (ctx.tag == COMA) {
		next_token(ctx);
		parse_item(ctx);
	}
}

void parse_item(context& ctx) throw (coord) {
	if (ctx.tag != IDENT)
		throw ctx.start;
	next_token(ctx);
	if (ctx.tag != EQUALS)
		return;
	next_token(ctx);
	if (ctx.tag != NUMBER)
		throw ctx.start;
	next_token(ctx);
}

void parse_vars(context& ctx) throw (coord) {
	next_token(ctx);
	while (ctx.tag == COMA) {
		next_token(ctx);
		if (ctx.tag != IDENT)
			throw ctx.start;
		next_token(ctx);
	}
}
