package labb3.modell;

import java.awt.Color;
import labb3.modell.Väderstreck;
import labb3.modell.Gång;
import java.util.ArrayList;

public class Rum {

    private Color golvfärg;
    private int bredd;
    private int höjd;
    private int övX;
    private int övY;
    private Gång[] gångar;

	public Rum(Color golvfärg, int bredd, int höjd, int övX, int övY) {
        this.golvfärg = golvfärg;
        this.bredd = bredd;
        this.höjd = höjd;
        this.övX = övX;
        this.övY = övY;
        this.gångar = new Gång[labb3.GlobalaKonstanter.ANTAL_VÄDERSTRECK];
	}

    public Color getColor() {
        return this.golvfärg;
    }

    public int getBredd() {
        return this.bredd;
    }

    public int getHöjd() {
        return this.höjd;
    }

    public int getPosX() {
        return this.övX;
    }

    public int getPosY() {
        return this.övY;
    }

    public Boolean finnsUtgångÅt(Väderstreck väderstreck) {
        return this.gångar[väderstreck.index()] != null;
    }

    public Gång gångenÅt(Väderstreck väderstreck) {
        try {
            return this.gångar[väderstreck.index()];
        } catch (ArrayIndexOutOfBoundsException e) {
            throw new IllegalArgumentException("Det finns ingen gång i den riktningen.", e);
        }
    }

	public static void kopplaIhop(Rum från, Väderstreck riktningUtUrFrån,
			Rum till, Väderstreck riktningInITill) {
        Gång gång = new Gång(från, riktningUtUrFrån, till, riktningInITill);
        Gång invgång = new Gång(till, riktningInITill, från, riktningUtUrFrån);
        if ( !från.finnsUtgångÅt( riktningUtUrFrån ) && !till.finnsUtgångÅt( riktningInITill )) {
            från.gångar[riktningUtUrFrån.index()] = gång;
            till.gångar[riktningInITill.index()] = invgång;
        }	
    }
}
