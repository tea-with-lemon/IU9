import javax.swing.*;
import java.awt.*;

public class Graphic {
    private JPanel mainPanel;
    private CanvasPanel canvasPanel;
    private JComboBox comboBox1;
    private JSpinner spinnerA;
    private JSpinner spinnerB;
    private JSpinner pointSpinner;
    private JLabel x0;
    private JLabel colourTouch;

    public Graphic() {
        spinnerA.addChangeListener(e -> canvasPanel.setA((Integer) spinnerA.getValue()));
        spinnerB.addChangeListener(e -> canvasPanel.setB((Integer) spinnerB.getValue()));
        pointSpinner.addChangeListener(e -> canvasPanel.setX0((Integer) pointSpinner.getValue()));
        comboBox1.addActionListener(e -> {
            String color= (String) comboBox1.getSelectedItem();
            if (color=="Красный") canvasPanel.setC(Color.red);
            else if (color=="Зеленый") canvasPanel.setC(Color.green);
            else if (color=="Желтый") canvasPanel.setC(Color.yellow);
            else if (color=="Синий") canvasPanel.setC(Color.blue);
            else if (color=="Фиолетовый") canvasPanel.setC(Color.magenta);
        });
        spinnerA.setValue(1);
        spinnerB.setValue(1);
        pointSpinner.setValue(5);
        canvasPanel.setA((Integer) spinnerA.getValue());
        canvasPanel.setB((Integer) spinnerB.getValue());
        canvasPanel.setX0((Integer) pointSpinner.getValue());
        canvasPanel.setC(Color.red);
    }
    public static void main(String[] args) {
        JFrame frame = new JFrame("Построение касательной к графику");
        frame.setContentPane(new Graphic().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
    private void createUIComponents() {
        canvasPanel=new CanvasPanel();
    }
}
class CanvasPanel extends JPanel {
    private int a,b,x0;
    private Color c;
    private double calculate(double x) {return a*Math.pow(x,2)/b;}
    private double calcDiff(double x) { return 2*a*x/b;}
    private double calcKasat(double x) {return calculate(x0)+calcDiff(x0)*(x-x0);}
    public void setC(Color c) {this.c=c; repaint();}
    public void setA(int a) {this.a=a; repaint();}
    public void setB(int b) {this.b=b; repaint();}
    public void setX0(int x0) {this.x0=x0; repaint();}
    protected  void paintComponent (Graphics g) {
        super.paintComponent(g);
        int width, height;
        width=this.getWidth();
        height=this.getHeight();
        g.drawLine(0,0,0,height);
        g.drawLine(0,height-1,width,height-1);
        for (int i=0; i<width; i++) {
            int x1, y1, x2, y2;
            x1=i;x2=i+1;
            y1=height-(int)(calculate(((double)x1)/width*10)*10);
            y2=height-(int)(calculate(((double)x2)/width*10)*10);
            System.out.println(x1+" "+y1+" "+x2+" "+y2);
            g.drawLine(x1,y1,x2,y2);
            y1=height-(int)(calcKasat(((double)x1)/width*10)*10);
            y2=height-(int)(calcKasat(((double)x2)/width*10)*10);
            g.setColor(c);
            g.drawLine(x1,y1,x2,y2);
            g.setColor(Color.BLACK);
        }
    }
}
