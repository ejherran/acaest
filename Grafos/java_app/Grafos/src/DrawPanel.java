import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.Font;

public class DrawPanel extends JPanel
{
    private Grafo grafo;

    public DrawPanel(Grafo grafo)
    {
        this.grafo = grafo;
    }

    public void paint(Graphics g)
    {
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        this.clear(g2);

        for (Nodo nodo:this.grafo.nodos)
        {
            for (Arista a: nodo.aristas)
            {
                g2.setColor(Color.BLUE);
                g2.drawLine(a.x.get(0), a.y.get(0), a.x.get(1), a.y.get(1));
            }
        }

        for (Nodo nodo:this.grafo.nodos)
        {
            g2.setColor(Color.RED);
            g2.fillOval(nodo.x-25, nodo.y-25, 50, 50);
            g2.setColor(Color.GREEN);
            g2.setFont(new Font("Monospace", Font.BOLD, 20));
            g2.drawString(nodo.valor, nodo.x-7, nodo.y+5);
        }
    }

    private void clear(Graphics2D g2)
    {
        g2.setColor(Color.BLACK);
        g2.fillRect(0, 0, this.getWidth(),this.getHeight());
    }
}
