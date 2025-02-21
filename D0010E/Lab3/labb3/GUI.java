package labb3;

import java.util.Observable;
import java.util.Observer;
import java.awt.Dimension;
import javax.swing.JFrame;

import labb3.kontroll.Tangentbordslyssnare;
import labb3.modell.Rum;
import labb3.modell.Nivå;
import labb3.vy.Målarduk;

public class GUI extends JFrame implements Observer {

	private Målarduk målarduk;
    private Observable observable;

	public GUI(Nivå enNivå) {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        enNivå.addObserver(this);

        målarduk = new Målarduk(enNivå);

        int maxX = 0;
        int maxY = 0;
        for (Rum r : enNivå.rum) {
            int eleMaxX = r.getPosX() + r.getBredd();
            int eleMaxY = r.getPosY() + r.getHöjd();

            if (eleMaxX > maxX) {
                maxX = eleMaxX;
            }
            if (eleMaxY > maxY) {
                maxY = eleMaxY;
            }
        }

        målarduk.setPreferredSize(new Dimension(maxX + 25, maxY + 25));

        målarduk.addKeyListener(new Tangentbordslyssnare(enNivå));

        this.setContentPane(målarduk);
        this.setVisible(true);
        this.pack();
	}

    @Override
	public void update(Observable o, Object arg) {
		this.målarduk.repaint();
	}
}
