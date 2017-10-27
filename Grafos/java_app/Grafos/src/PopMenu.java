import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;

public class PopMenu extends JPopupMenu
{
    private Ventana parent;

    public int posX;
    public int posY;

    private Nodo objetivo;
    private Nodo destino;

    public int estado;

    private JMenuItem agregarNodo;
    private JMenuItem agregarArista;
    private JMenuItem editarNodo;
    private JMenuItem editarDireccionArista;
    private JMenuItem editarValorArista;
    private JMenuItem eliminarNodo;
    private JMenuItem eliminarArista;

    public PopMenu(Ventana parent)
    {
        this.parent = parent;

        this.estado = 0;

        this.agregarNodo = new JMenuItem("Agregar Nodo");
        this.agregarNodo.addActionListener(e -> parent.addNodo(posX, posY));

        this.agregarArista = new JMenuItem("Agregar Arista");
        this.agregarArista.addActionListener(e -> chEstado(2));

        this.editarNodo = new JMenuItem("Editar Nodo");
        this.editarNodo.addActionListener(e -> parent.editNodo(this.objetivo));

        this.editarDireccionArista = new JMenuItem("Editar Dirección De La Arista");

        this.editarValorArista = new JMenuItem("Editar Valor De La Arista");

        this.eliminarNodo = new JMenuItem("Eliminar Nodo");
        this.eliminarNodo.addActionListener(e -> parent.delNodo(this.objetivo));

        this.eliminarArista = new JMenuItem("Eliminar Arista");
    }

    private void chEstado(int es)
    {
        this.estado = es;
    }

    public void hacer(MouseEvent e)
    {
        this.posX = e.getX();
        this.posY = e.getY();

        if(this.estado == 0)
        {
            this.objetivo = this.parent.grafo.tocar(posX, posY);
            if(this.objetivo != null)
                this.estado = 1;
            else
                this.estado = 0;
        }
        else if(this.estado == 1)
        {
            this.estado = 0;
            this.objetivo = null;
        }
        else if(this.estado == 2)
        {
            this.destino = this.parent.grafo.tocar(posX, posY);
            if(destino != null)
            {
                this.parent.addArista(this.objetivo, this.destino);
                this.estado = 0;
            }
        }
    }

    public void mover(MouseEvent e)
    {
        this.parent.moveNodo(this.objetivo, e.getX(), e.getY());
    }

    public void activar(MouseEvent e)
    {
        this.removeAll();
        this.posX = e.getX();
        this.posY = e.getY();

        this.objetivo = this.parent.grafo.tocar(posX, posY);

        if(objetivo != null)
        {
            this.add(editarNodo);
            this.add(eliminarNodo);
            this.add(new JSeparator());
            this.add(agregarArista);
        }
        else
        {
            this.add(this.agregarNodo);
        }

        this.show(e.getComponent(), posX, posY);
    }
}
