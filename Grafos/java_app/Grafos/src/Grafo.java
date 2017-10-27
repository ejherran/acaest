import java.util.LinkedList;
import java.util.HashMap;

public class Grafo
{
    public LinkedList<Nodo> nodos;

    public Grafo()
    {
        this.nodos = new LinkedList<>();
    }

    public void addNodo(int x, int y, String valor)
    {
        Nodo nuevo = new Nodo(x, y, valor);
        this.nodos.add(nuevo);
    }

    public void addArista(String valor, Nodo origen, Nodo destino, boolean isDoble)
    {
        Arista nueva = new Arista(valor, origen, destino, isDoble);
        origen.aristas.add(nueva);

        nueva.addPoint(origen.x, origen.y);
        nueva.addPoint(destino.x, destino.y);


        if(isDoble)
        {
            Arista nueva2 = new Arista(valor, destino, origen, isDoble);
            destino.aristas.add(nueva2);
        }
    }

    public Nodo buscarNodo(String valor)
    {
        Nodo res = null;

        for(int i = 0; i < this.nodos.size(); i++)
        {
            if(this.nodos.get(i).valor == valor)
            {
                res = this.nodos.get(i);
                break;
            }
        }

        return res;
    }

    public Nodo buscarNodo(int x, int y)
    {
        Nodo res = null;

        for(int i = 0; i < this.nodos.size(); i++)
        {
            if(this.nodos.get(i).x == x && this.nodos.get(i).y == y)
            {
                res = this.nodos.get(i);
                break;
            }
        }

        return res;
    }

    public Arista buscarArista(String valor, Nodo origen, Nodo destino)
    {
        Arista res = null;

        for(int i = 0; i < this.nodos.size(); i++)
        {
            for (int j = 0; j < this.nodos.get(i).aristas.size(); j++)
            {
                Arista foo = this.nodos.get(i).aristas.get(j);

                if(foo.valor == valor && foo.origen == origen && foo.destino == destino)
                {
                    res = foo;
                    break;
                }
            }

            if(res != null)
                break;
        }

        return res;
    }

    public void editarNodo(String viejo, String nuevo)
    {
        Nodo objetivo = this.buscarNodo(viejo);
        objetivo.valor = nuevo;
    }

    public void editarAristaValor(String viejo, Nodo origen, Nodo destino, String nuevo)
    {
        Arista objetivo = this.buscarArista(viejo, origen, destino);
        objetivo.valor = nuevo;

        if(objetivo.isDoble)
        {
            objetivo = this.buscarArista(viejo, destino, origen);
            objetivo.valor = nuevo;
        }
    }

    public void editarAristaDestino(String viejo, Nodo origen, Nodo destino, Nodo nuevo)
    {
        Arista objetivo = this.buscarArista(viejo, origen, destino);
        objetivo.destino = nuevo;

        if(objetivo.isDoble)
        {
            objetivo.isDoble = false;

            objetivo = this.buscarArista(viejo, destino, origen);
            objetivo.isDoble = false;
        }
    }

    public void eliminarNodo(Nodo objetivo)
    {
        for (int i = 0; i < this.nodos.size(); i++)
        {
            if(this.nodos.get(i) != objetivo)
            {
                LinkedList<Arista> vivos = new LinkedList<>();

                for (int j = 0; j < this.nodos.get(i).aristas.size(); j++)
                {
                    if(this.nodos.get(i).aristas.get(j).destino != objetivo)
                    {
                        vivos.add(this.nodos.get(i).aristas.get(j));
                    }
                }

                this.nodos.get(i).aristas = vivos;
            }
        }

        this.nodos.remove(objetivo);
    }

    public void eliminarArista(Arista objetivo)
    {
        Nodo ori = objetivo.origen;
        ori.aristas.remove(objetivo);

        if(objetivo.isDoble)
        {
            Arista contraria = this.buscarArista(objetivo.valor, objetivo.destino, objetivo.origen);
            Nodo des = contraria.origen;
            des.aristas.remove(contraria);
        }
    }

    public Nodo tocar(int x, int y)
    {
        for (Nodo n : this.nodos)
        {
            double d = Math.pow( (n.x-x), 2 ) + Math.pow( (n.y-y), 2 );
            d = Math.sqrt(d);

            if(d <= 25.0)
                return n;
        }

        return null;
    }

    public void ver()
    {
        for (int i = 0; i < this.nodos.size(); i++)
        {
            System.out.println(this.nodos.get(i).valor);

            for (int j = 0; j < this.nodos.get(i).aristas.size(); j++)
            {
                System.out.println(this.nodos.get(i).aristas.get(j).valor+" -> "+this.nodos.get(i).aristas.get(j).destino.valor+" : "+this.nodos.get(i).aristas.get(j).isDoble);
            }
        }
    }

    public void bfs(String ori)
    {
        HashMap<String, String> padres = new HashMap();
        HashMap<String, Integer> costos = new HashMap();
        LinkedList<String> vistos = new LinkedList();
        LinkedList<Nodo> cola = new LinkedList();


        Nodo origen = this.buscarNodo(ori);
        if(origen != null)
        {
            for (Nodo n:this.nodos)
            {
                padres.put(n.valor, null);
                costos.put(n.valor, 65535);
            }

            costos.replace(origen.valor, 0);
            cola.add(origen);

            while(cola.size() > 0)
            {

                Nodo q = cola.pop();

                for (Arista a : q.aristas)
                {
                    Nodo v = a.destino;
                    if(!vistos.contains(v.valor))
                    {
                        costos.replace(v.valor, costos.get(q.valor)+1);
                        padres.replace(v.valor,q.valor);

                        if(!cola.contains(v))
                            cola.add(v);
                    }
                }

                vistos.add(q.valor);
            }

            for (String v:vistos)
            {
                System.out.println(v);
            }

            for (String v:costos.keySet())
            {
                System.out.println(v+" "+costos.get(v));
            }

            for (String v:padres.keySet())
            {
                System.out.println(v+" "+padres.get(v));
            }
        }

    }

    public void dfs(String ori)
    {
        HashMap<String, String> padres = new HashMap();
        HashMap<String, Integer> costos = new HashMap();
        LinkedList<String> vistos = new LinkedList();
        LinkedList<Nodo> pila = new LinkedList();


        Nodo origen = this.buscarNodo(ori);
        if(origen != null)
        {
            for (Nodo n:this.nodos)
            {
                padres.put(n.valor, null);
                costos.put(n.valor, 65535);
            }

            costos.replace(origen.valor, 0);
            pila.add(origen);

            while(pila.size() > 0)
            {

                Nodo q = pila.pop();

                for (Arista a : q.aristas)
                {
                    Nodo v = a.destino;
                    if(!vistos.contains(v.valor))
                    {
                        costos.replace(v.valor, costos.get(q.valor)+1);
                        padres.replace(v.valor,q.valor);

                        if(!pila.contains(v))
                            pila.push(v);
                    }
                }

                vistos.add(q.valor);
            }

            for (String v:vistos)
            {
                System.out.println(v);
            }

            for (String v:costos.keySet())
            {
                System.out.println(v+" "+costos.get(v));
            }

            for (String v:padres.keySet())
            {
                System.out.println(v+" "+padres.get(v));
            }
        }

    }

    public int getMin(LinkedList<Nodo> cola, HashMap<String, Integer> costos)
    {
        String tmp = cola.get(0).valor;

        for (Nodo x:cola)
        {
            if(costos.get(tmp) > costos.get(x.valor))
                tmp = x.valor;
        }

        int ind = 0;
        while(ind < cola.size())
        {
            if(cola.get(ind).valor.equals(tmp))
                break;
            else
                ind = ind+1;
        }

        return ind;
    }

    public void dijkstra(String ori)
    {
        HashMap<String, String> padres = new HashMap();
        HashMap<String, Integer> costos = new HashMap();
        LinkedList<String> vistos = new LinkedList();
        LinkedList<Nodo> cola = new LinkedList();


        Nodo origen = this.buscarNodo(ori);
        if(origen != null)
        {
            for (Nodo n:this.nodos)
            {
                padres.put(n.valor, null);
                costos.put(n.valor, 65535);
            }

            costos.replace(origen.valor, 0);
            cola.add(origen);

            while(cola.size() > 0)
            {

                int min = this.getMin(cola, costos);
                Nodo q = cola.get(min);
                cola.remove(min);

                for (Arista a : q.aristas)
                {
                    Nodo v = a.destino;
                    if(!vistos.contains(v.valor))
                    {
                        if(costos.get(v.valor) > costos.get(q.valor)+Integer.parseInt(a.valor))
                        {
                            costos.replace(v.valor, costos.get(q.valor) + Integer.parseInt(a.valor));
                            padres.replace(v.valor, q.valor);
                        }

                        if(!cola.contains(v))
                            cola.add(v);
                    }
                }

                vistos.add(q.valor);
            }

            for (String v:vistos)
            {
                System.out.println(v);
            }

            for (String v:costos.keySet())
            {
                System.out.println(v+" "+costos.get(v));
            }

            for (String v:padres.keySet())
            {
                System.out.println(v+" "+padres.get(v));
            }
        }

    }

    public int getHeuro(LinkedList<Nodo> cola, HashMap<String, Integer> costos, Nodo destino)
    {
        Nodo tmp = cola.get(0);

        for (Nodo x:cola)
        {
            double f1 = Math.abs(x.x-destino.x)+Math.abs(x.y-destino.y);
            double f2 = Math.abs(tmp.x-destino.x)+Math.abs(tmp.y-destino.y);

            if(costos.get(tmp.valor)+f2 > costos.get(x.valor)+f1)
                tmp = x;
        }

        int ind = 0;
        while(ind < cola.size())
        {
            if(cola.get(ind).valor.equals(tmp.valor))
                break;
            else
                ind = ind+1;
        }

        return ind;
    }

    public void aStar(String ori, String des)
    {
        HashMap<String, String> padres = new HashMap();
        HashMap<String, Integer> costos = new HashMap();
        LinkedList<String> vistos = new LinkedList();
        LinkedList<Nodo> cola = new LinkedList();


        Nodo origen = this.buscarNodo(ori);
        if(origen != null)
        {
            Nodo destino = this.buscarNodo(des);

            for (Nodo n:this.nodos)
            {
                padres.put(n.valor, null);
                costos.put(n.valor, 65535);
            }

            costos.replace(origen.valor, 0);
            cola.add(origen);

            while(cola.size() > 0)
            {

                int min = this.getHeuro(cola, costos, destino);
                Nodo q = cola.get(min);
                cola.remove(min);

                for (Arista a : q.aristas)
                {
                    Nodo v = a.destino;
                    if(!vistos.contains(v.valor))
                    {
                        if(costos.get(v.valor) > costos.get(q.valor)+Integer.parseInt(a.valor))
                        {
                            costos.replace(v.valor, costos.get(q.valor) + Integer.parseInt(a.valor));
                            padres.replace(v.valor, q.valor);
                        }

                        if(!cola.contains(v))
                            cola.add(v);
                    }
                }

                vistos.add(q.valor);
            }

            for (String v:vistos)
            {
                System.out.println(v);
            }

            for (String v:costos.keySet())
            {
                System.out.println(v+" "+costos.get(v));
            }

            for (String v:padres.keySet())
            {
                System.out.println(v+" "+padres.get(v));
            }
        }

    }
}
