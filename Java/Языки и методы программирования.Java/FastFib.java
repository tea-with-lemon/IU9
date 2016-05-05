import java.math.BigInteger;
import java.util.Scanner;

public class FastFib {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        BigInteger[][] matrixQ = {
                {BigInteger.ONE,BigInteger.ONE},
                {BigInteger.ONE,BigInteger.ZERO},
        };
        BigInteger[][] matrixV= {
                {BigInteger.ONE},
                {BigInteger.ZERO},
        };
        BigInteger[][] matrixHelp= {
                {BigInteger.ZERO, BigInteger.ZERO},
                {BigInteger.ZERO, BigInteger.ZERO}
        };//вспомогательная матрица при перемножении
        while (n> 0) {
            if ((n&1)==1) {
                matrixHelp[0][0]=matrixV[0][0].multiply(matrixQ[0][0]).add(matrixV[1][0].multiply(matrixQ[1][0]));
                matrixHelp[0][1]=matrixV[0][0].multiply(matrixQ[0][1]).add(matrixV[1][0].multiply(matrixQ[1][1]));
                matrixV[0][0]=matrixHelp[0][0];
                matrixV[1][0]=matrixHelp[0][1];
            }
            matrixHelp[0][0]=matrixQ[0][0].multiply(matrixQ[0][0]).add(matrixQ[0][1].multiply(matrixQ[1][0]));
            matrixHelp[0][1]=matrixQ[0][0].multiply(matrixQ[0][1]).add(matrixQ[0][1].multiply(matrixQ[1][1]));
            matrixHelp[1][0]=matrixQ[1][0].multiply(matrixQ[0][0]).add(matrixQ[1][1].multiply(matrixQ[1][0]));
            matrixHelp[1][1]=matrixQ[1][0].multiply(matrixQ[0][1]).add(matrixQ[1][1].multiply(matrixQ[1][1]));
            matrixQ[0][0]=matrixHelp[0][0];
            matrixQ[0][1]=matrixHelp[0][1];
            matrixQ[1][0]=matrixHelp[1][0];
            matrixQ[1][1]=matrixHelp[1][1];
            n >>= 1;
        }
        System.out.println(matrixV[1][0]);
    }
}

