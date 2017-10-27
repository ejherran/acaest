import java.util.LinkedList;

public class Nodo
{
    public int x;
    public int y;
    public String valor;
    public LinkedList<Arista> aristas;

    public Nodo(int x, int y, String valor)
    {
        this.x = x;
        this.y = y;
        this.valor = valor;

        this.aristas = new LinkedList<>();
    }
}
