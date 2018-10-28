import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
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
    public String substring(int follow) {
        return text.substring(index, follow);
    }
    public int getIndex() {return index;}

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
}
class SyntaxError extends Exception {
    public SyntaxError() {
        super(String.format("%s", "error"));
    }
}
enum Tag {
    VAR,
    NUMBER,
    PLUS,
    MINUS,
    MUL,
    DIV,
    LPAREN,
    RPAREN,
    END_OF_TEXT;

    public String toString() {
        switch (this) {
            case VAR: return "var";
            case NUMBER: return "number";
            case PLUS: return "+";
            case MINUS: return "-";
            case MUL: return "*";
            case DIV: return "/";
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
    private int value;
    private String varID;

    public Token(String text) throws SyntaxError {
        this(new Position(text));
    }

    public int getValue() {
        return value;
    }
    public String getVarID() {
        return varID;
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
            case '+':
                tag=Tag.PLUS;
                break;
            case '-':
                tag=Tag.MINUS;
                break;
            case '*':
                tag=Tag.MUL;
                break;
            case '/':
                tag=Tag.DIV;
                break;
            default:
                if (start.satisfies(Character::isLetter)) {
                    follow = follow.skipWhile(Character::isLetterOrDigit);
                    varID=start.substring(follow.getIndex());
                    tag = Tag.VAR;
                } else if (start.satisfies(Character::isDigit)) {
                    follow = follow.skipWhile(Character::isDigit);
                    if (follow.satisfies(Character::isLetter)) {
                        throw new SyntaxError();
                    }
                    value=Integer.parseInt(start.substring(follow.getIndex()));
                    tag = Tag.NUMBER;
                } else throw new SyntaxError();
        }
    }
    public void throwError() throws SyntaxError {
        throw new SyntaxError();
    }

    public boolean matches(Tag ...tags) {return Arrays.stream(tags).anyMatch(t -> tag == t);}

    public Token next() throws SyntaxError {return new Token(follow);}
}
public class Calc {
    private static Map<String, Integer> dict=new HashMap<>();
    private static Token sym;
    private static Scanner in;
    private static void expect(Tag tag) throws SyntaxError {
        if (!sym.matches(tag)) {
            sym.throwError();
        }
        sym = sym.next();
    }
    public static void main(String[] args) {
        in = new Scanner(System.in);
        String text = in.nextLine();
        try {
            sym = new Token(text);
            System.out.println(parse());
        }
        catch (SyntaxError e) {
            System.out.println(e.getMessage());
        }
    }
    // <E>  ::= <T> <E1>
    // <E1> ::= + <T> <E1> | - <T> <E1> | ε
    // <T>  ::= <F> <T1>
    // <T1> ::= * <F> <T1> | / <F> <T1> | ε
    // <F>  ::= <number> | <var> | ( <E> ) | - <F>
    private static int parse() throws SyntaxError {
        int value = parseE();
        expect(Tag.END_OF_TEXT);
        return value;
    }
    private static int parseE() throws SyntaxError {
        int value=parseT();
        return parseE1(value);
    }
    private static int parseT() throws SyntaxError {
        int value=parseF();
        return parseT1(value);
    }
    private static int parseE1(int left) throws SyntaxError {
        if (sym.matches(Tag.PLUS)) {
            sym = sym.next();
            int right = parseT();
            return parseE1(left+right);
        }
        else if (sym.matches(Tag.MINUS)) {
            sym = sym.next();
            int right = parseT();
            return parseE1(left-right);
        } else return left;
    }
    private static int parseF() throws SyntaxError {
        if (sym.matches(Tag.NUMBER)) {
            int value = sym.getValue();
            sym = sym.next();
            return value;
        } else if (sym.matches(Tag.VAR)) {
            if (!dict.containsKey(sym.getVarID())) {
                int x=in.nextInt();
                dict.put(sym.getVarID(),x);
            }
            int value = dict.get(sym.getVarID());
            sym = sym.next();
            return value;
        } else if (sym.matches(Tag.LPAREN)) {
            sym = sym.next();
            int value = parseE();
            expect(Tag.RPAREN);
            return value;
        } else {
            expect(Tag.MINUS);
            return -parseF();
        }
    }
    private static int parseT1(int left) throws SyntaxError {
        if (sym.matches(Tag.MUL)) {
            sym = sym.next();
            int right = parseF();
            return parseT1(left*right);
        } else if (sym.matches(Tag.DIV)) {
            sym = sym.next();
            int right = parseF();
            return parseT1(left/right);
        } else return left;
    }
}

