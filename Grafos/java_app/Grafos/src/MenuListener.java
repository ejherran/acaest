import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;

public class MenuListener extends MouseAdapter implements MouseMotionListener
{
    private PopMenu menu;

    public MenuListener(Ventana parent)
    {
        this.menu = new PopMenu(parent);
    }

    public void mousePressed(MouseEvent e)
    {
        if (e.isPopupTrigger())
        {
            this.doPop(e);
        }

    }

    public void mouseReleased(MouseEvent e)
    {
        if (e.isPopupTrigger())
        {
            this.doPop(e);
        }
        else if(e.getButton() == 1)
            this.menu.hacer(e);
    }

    public void mouseMoved(MouseEvent e)
    {
        System.out.println(this.menu.estado);
        if(this.menu.estado == 1)
        {
            this.menu.mover(e);
        }
    }

    private void doPop(MouseEvent e)
    {
        this.menu.activar(e);
    }
}
