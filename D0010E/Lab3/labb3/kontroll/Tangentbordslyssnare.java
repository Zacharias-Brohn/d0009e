package labb3.kontroll;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import static labb3.modell.Väderstreck.*;

import labb3.modell.Nivå;

public class Tangentbordslyssnare implements KeyListener {
	private Nivå enNivå;

	public Tangentbordslyssnare(Nivå enNivå) {
		this.enNivå = enNivå;
	}

	@Override
    public void keyPressed(KeyEvent e) {
        char keyChar = e.getKeyChar();
        switch (keyChar) {
            case 'w':
                this.enNivå.hoppaÅt(NORR);
                break;
            case 'd':
                this.enNivå.hoppaÅt(ÖSTER);
                break;
            case 's':
                this.enNivå.hoppaÅt(SÖDER);
                break;
            case 'a':
                this.enNivå.hoppaÅt(VÄSTER);
                break;
            default:
                // Handle other keys if necessary
                break;
        }
    }

	@Override
	public void keyTyped(KeyEvent e) {
		// Används inte men måste implementeras eftersom keyTyped finns i
		// gränssnittet KeyListener.
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// Används inte men måste implementeras eftersom keyReleased finns is
		// gränssnittet KeyListener.
	}
}
