import java.util.LinkedList;

public class Arista
{
    public LinkedList<Integer> x;
    public LinkedList<Integer> y;
    public String valor;

    public Nodo origen;
    public Nodo destino;
    public boolean isDoble;

    public Arista(String valor, Nodo origen, Nodo destino, boolean isDoble)
    {
        this.valor = valor;
        this.origen = origen;
        this.destino = destino;
        this.isDoble = isDoble;

        this.x = new LinkedList<>();
        this.y = new LinkedList<>();
    }

    public void addPoint(int x, int y)
    {
        this.x.add(x);
        this.y.add(y);
    }
}
