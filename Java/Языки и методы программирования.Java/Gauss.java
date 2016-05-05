import java.util.Scanner;

public class Gauss {
    public static void main(String[] args) {
        int n;
        int[][] chislitel=new int[5][6], znamenatel=new int[5][6];
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n + 1; j++) {
                chislitel[i][j] = scanner.nextInt();
                znamenatel[i][j] = 1;
            }
        }
        for (int i = 0; i < n; i++) {
            if (chislitel[i][i] == 0) {
                for (int j = i+1; j < n; j++) {
                    if (chislitel[j][i] != 0) {
                        for (int z = 0; z < n + 1; z++) {
                            int buf=chislitel[i][z];chislitel[i][z] = chislitel[j][z];chislitel[j][z] = buf;
                            buf=znamenatel[i][z];znamenatel[i][z] = znamenatel[j][z];znamenatel[j][z] = buf;
                        }
                        break;
                    }
                }
                if (chislitel[i][i] == 0) {
                    System.out.println("No solution");
                    return;
                }
            }
            int ch = chislitel[i][i];
            int zn = znamenatel[i][i];
            for (int j = 0; j < n + 1; j++) {
                chislitel[i][j] = chislitel[i][j] * zn;
                znamenatel[i][j] = znamenatel[i][j] * ch;
                int k = nod(Math.abs(chislitel[i][j]), Math.abs(znamenatel[i][j]));
                if (k == 0) {
                    System.out.println("No solution");
                    return;
                }
                chislitel[i][j] = chislitel[i][j] / k;
                znamenatel[i][j] = znamenatel[i][j] / k;
            }
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                ch = chislitel[j][i];
                zn = znamenatel[j][i];
                for (int z = 0; z < n + 1; z++) {
                    chislitel[j][z] = chislitel[j][z] * zn * znamenatel[i][z] - ch * znamenatel[j][z] * chislitel[i][z];
                    znamenatel[j][z] *= zn * znamenatel[i][z];
                    int k = nod(Math.abs(chislitel[j][z]), Math.abs(znamenatel[j][z]));
                    chislitel[j][z] /= k;
                    znamenatel[j][z] /= k;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (chislitel[i][n]==0) System.out.println("0/1");
            else if (chislitel[i][n]<0 && znamenatel[i][n]<0) System.out.printf("%d/%d\n", -chislitel[i][n], -znamenatel[i][n]);
            else if (chislitel[i][n]>0 && znamenatel[i][n]<0) System.out.printf("%d/%d\n", -chislitel[i][n], -znamenatel[i][n]);
            else System.out.printf("%d/%d\n", chislitel[i][n], znamenatel[i][n]);
        }
    }
    private static int nod(int x, int y) {
        if(x==0 || y==0) return x+y;
        else if (x>y) return nod(x%y, y);
        else return nod(x, y%x);
    }
}
