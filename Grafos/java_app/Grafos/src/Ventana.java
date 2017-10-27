import javax.swing.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.File;
import java.util.Scanner;

public class Ventana extends JFrame
{

    private DrawPanel can;
    public Grafo grafo;

    public static void main(String[] args)
    {
        new Ventana();
    }

    public Ventana()
    {
        this.grafo = new Grafo();

        MenuListener ml = new MenuListener(this);

        this.can = new DrawPanel(this.grafo);
        this.can.addMouseListener(ml);
        this.can.addMouseMotionListener(ml);

        this.setBounds(100, 100,400,400);
        this.setTitle("Grafos");
        this.addWindowListener(
                new WindowAdapter()
                {
                    @Override
                    public void windowClosing(WindowEvent e)
                    {
                        System.exit(0);
                    }
                }
        );

        this.add(can);

        this.setVisible(true);
    }

    private String readFile(String pathname)
    {
        try
        {
            File file = new File(pathname);
            StringBuilder fileContents = new StringBuilder((int) file.length());
            Scanner scanner = new Scanner(file);
            String lineSeparator = System.getProperty("line.separator");

            try
            {
                while (scanner.hasNextLine())
                {
                    fileContents.append(scanner.nextLine() + lineSeparator);
                }
                return fileContents.toString();
            }
            finally
            {
                scanner.close();
            }
        }
        catch (Exception ex)
        {
            System.err.println(ex.toString());
        }

        return null;
    }

    public void addNodo(int x, int y)
    {
        String valor = JOptionPane.showInputDialog(this,"Valor del nodo?:","Grafos",JOptionPane.QUESTION_MESSAGE);
        this.grafo.addNodo(x, y, valor);
        this.can.repaint();
    }

    public void addArista(Nodo origen, Nodo destino)
    {
        String valor = JOptionPane.showInputDialog(this,"Valor de la arista?:","Grafos",JOptionPane.QUESTION_MESSAGE);
        this.grafo.addArista(valor, origen, destino, false);
        this.can.repaint();
    }

    public void delNodo(Nodo objetivo)
    {
        this.grafo.eliminarNodo(objetivo);
        this.can.repaint();
    }

    public void editNodo(Nodo objetivo)
    {
        String valor = JOptionPane.showInputDialog(this,"Valor del nodo?:","Grafos",JOptionPane.QUESTION_MESSAGE);
        this.grafo.editarNodo(objetivo.valor, valor);
        this.can.repaint();
    }

    public void moveNodo(Nodo objetivo, int x, int y)
    {
        objetivo.x = x;
        objetivo.y = y;

        for (Arista a: objetivo.aristas)
        {
            a.x.set(0, x);
            a.y.set(0, y);
        }

        for (Nodo n: this.grafo.nodos)
        {
            for (Arista a: n.aristas)
            {
                if(a.destino == objetivo)
                {
                    a.x.set(1, x);
                    a.y.set(1, y);
                }
            }
        }

        this.can.repaint();
    }

}
