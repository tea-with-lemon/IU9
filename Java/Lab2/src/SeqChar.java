public class SeqChar implements Comparable<SeqChar > {
    private char[] chars;
    private int counter;
    public SeqChar (char[] chars) {
        this.chars = new char[chars.length];
        for (int i = 0; i<chars.length; i++) {
            this.chars[i]=chars[i];
            if (chars[i] == 'a') counter++;
        }
    }

    public int compareTo(SeqChar o) {
        return counter - o.counter;
    }

    public String toString() {
        return String.valueOf(chars)+" "+String.valueOf(counter);
    }
}
