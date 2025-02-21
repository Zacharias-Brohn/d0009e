package labb3.modell;

import java.util.Observable;
import java.util.ArrayList;

public class Nivå extends Observable {

    public Rum startrum;
    public ArrayList<Rum> rum;

	public Nivå(Rum startrum, ArrayList<Rum> rum) {
        this.startrum = startrum;
        this.rum = rum;

        try {
            if (!rum.contains(startrum)) {
                throw new IllegalArgumentException(
                        "Startrummet finns inte i rum"
                        );
            }
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        for (Rum r : rum) {
            try {
                Rum s = rum.get(rum.indexOf(r)+1);
                if ( s != null ) {
                    if ( r.getPosX() < s.getPosX() + s.getBredd() &&
                            r.getPosX() + r.getBredd() > s.getPosX() &&
                            r.getPosY() < s.getPosY() + s.getHöjd() &&
                            r.getPosY() + r.getHöjd() > s.getPosY() ) {
                        throw new IllegalArgumentException(
                                "Rummen överlappar varandra"
                                );
                            }
                }
            } catch (IndexOutOfBoundsException e) {
            }
        }
	}

    public ArrayList<Rum> getRum() {
        return this.rum;
    }

    public Rum getCurrentRoom() {
        return this.startrum;
    }

	public void hoppaÅt(Väderstreck väderstreck) {
        if ( this.startrum.finnsUtgångÅt(väderstreck) ) {
            this.startrum = this.startrum.gångenÅt(väderstreck).getTill();
            setChanged();
            notifyObservers();
        }
	}
}
