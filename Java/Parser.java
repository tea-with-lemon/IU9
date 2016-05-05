import java.util.Arrays;
import java.util.Scanner;
import java.util.function.IntPredicate;

class Position {
    private String text;
    private int index, line, col;

    public Position(String text) {
        this(text, 0, 1, 1);
    }

    private Position(String text, int index, int line, int col) {
        this.text = text;
        this.index = index;
        this.line = line;
        this.col = col;
    }

    public int getChar() {
        return index < text.length() ? text.codePointAt(index) : -1;
    }

    public boolean satisfies(IntPredicate p) {
        return p.test(getChar());
    }

    public Position skip() {
        int c = getChar();
        switch (c) {
            case -1:
                return this;
            case '\n':
                return new Position(text, index+1, line+1, 1);
            default:
                return new Position(text, index + (c > 0xFFFF ? 2 : 1), line, col+1);
        }
    }

    public Position skipWhile(IntPredicate p) {
        Position pos = this;
        while (pos.satisfies(p)) pos = pos.skip();
        return pos;
    }

    public String toString() {
        return String.format("(%d, %d)", line, col);
    }
}

class SyntaxError extends Exception {
    public SyntaxError(Position pos, String msg) {
        super(String.format("Syntax error at %s: %s", pos.toString(), msg));
    }
}

enum Tag {
    IDENT,
    NUMBER,
    STRING,
    LPAREN,
    RPAREN,
    END_OF_TEXT;

    public String toString() {
        switch (this) {
            case IDENT: return "identifier";
            case NUMBER: return "number";
            case STRING: return "string";
            case LPAREN: return "'('";
            case RPAREN: return "')'";
            case END_OF_TEXT: return "end of text";
        }
        throw new RuntimeException("unreachable code");
    }
}

class Token {
    private Tag tag;
    private Position start, follow;

    public Token(String text) throws SyntaxError {
        this(new Position(text));
    }

    private Token(Position cur) throws SyntaxError {
        start = cur.skipWhile(Character::isWhitespace);
        follow = start.skip();
        switch (start.getChar()) {
            case -1:
                tag = Tag.END_OF_TEXT;
                break;
            case '(':
                tag = Tag.LPAREN;
                break;
            case ')':
                tag = Tag.RPAREN;
                break;
            case '"':
                follow = follow.skipWhile(c -> c != '"' && c != '\n' && c != -1);
                if (follow.getChar() != '"') {
                    throw new SyntaxError(follow, "newline in string literal");
                }
                follow = follow.skip();
                tag = Tag.STRING;
                break;
            default:
                if (start.satisfies(Character::isLetter)) {
                    follow = follow.skipWhile(Character::isLetterOrDigit);
                    tag = Tag.IDENT;
                } else if (start.satisfies(Character::isDigit)) {
                    follow = follow.skipWhile(Character::isDigit);
                    if (follow.satisfies(Character::isLetter)) {
                        throw new SyntaxError(follow, "delimiter expected");
                    }
                    tag = Tag.NUMBER;
                } else {
                    throwError("invalid character");
                }
        }
    }

    public void throwError(String msg) throws SyntaxError {
        throw new SyntaxError(start, msg);
    }

    public boolean matches(Tag ...tags) {
        return Arrays.stream(tags).anyMatch(t -> tag == t);
    }

    public Token next() throws SyntaxError {
        return new Token(follow);
    }
}

public class Parser {
    private static Token sym;

    private static void expect(Tag tag) throws SyntaxError {
        if (!sym.matches(tag)) {
            sym.throwError(tag.toString() + " expected");
        }
        sym = sym.next();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        in.useDelimiter("\\Z");
        String text = in.next();

        try {
            sym = new Token(text);
            parse();
            System.out.println("success");
        }
        catch (SyntaxError e) {
            System.out.println(e.getMessage());
        }
    }

    // <A> ::= IDENT ( <B> ) | NUMBER | STRING
    // <B> ::= <A> <B> | ε
    private static void parse() throws SyntaxError {
        parseA();
        expect(Tag.END_OF_TEXT);
    }

    private static void parseA() throws SyntaxError {
        if (sym.matches(Tag.IDENT)) {
            System.out.println("<A> ::= IDENT ( <B> )");
            sym = sym.next();
            expect(Tag.LPAREN);
            parseB();
            expect(Tag.RPAREN);
        } else if (sym.matches(Tag.NUMBER)) {
            System.out.println("<A> ::= NUMBER");
            sym = sym.next();
        } else if (sym.matches(Tag.STRING)) {
            System.out.println("<A> ::= STRING");
            sym = sym.next();
        } else {
            sym.throwError("identifier, number or string expected");
        }
    }

    private static void parseB() throws SyntaxError {
        if (sym.matches(Tag.IDENT, Tag.NUMBER, Tag.STRING)) {
            System.out.println("<B> ::= <A> <B>");
            parseA();
            parseB();
        } else {
            System.out.println("<B> ::= ε");
        }
    }
}