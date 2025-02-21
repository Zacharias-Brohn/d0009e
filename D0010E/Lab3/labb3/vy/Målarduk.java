package labb3.vy;

import java.awt.BasicStroke;
import java.awt.Graphics2D;
import java.awt.Graphics;
import javax.swing.JPanel;

import labb3.modell.Gång;
import labb3.modell.Nivå;
import labb3.modell.Rum;
import labb3.modell.Väderstreck;
import labb3.verktyg.Punkt;
import labb3.verktyg.Grafik;
import static labb3.GlobalaKonstanter.*;

public class Målarduk extends JPanel {

	private final Nivå enNivå;

	public Målarduk(Nivå enNivå) {
		this.enNivå = enNivå;
        this.setBackground(MARKFÄRG);
        this.setFocusable(true);
	}

    @Override
	protected void paintComponent(Graphics g) {
        super.paintComponent(g);

		// TODO: Lägg till kod som ritar ut en grafisk vy av enNivå.
		//
		// För att underlätta finns hjälpmetoder som ska skrivas klara. Studera
		// noga bilderna i labbinstruktionen för att få fram formlerna för
		// bas- och pivotpunkternas koordinater. Använd ritmetoderna i klassen
		// labb3.verktyg.Grafik. Anropa hjälpmetoderna från paintComponent.
        for (Rum r : this.enNivå.getRum()) {
            ritaRum(g, r);
        }
        for (Rum r : this.enNivå.getRum()) {
            ritaGångarFrånRum(g, r);
        }
        ritaMarkörFörVarAnvändarenÄr(g);
	}

	private void ritaRum(Graphics g, Rum ettRum) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setColor(ettRum.getColor());
        g2d.fillRect(
            ettRum.getPosX(),
            ettRum.getPosY(),
            ettRum.getBredd(),
            ettRum.getHöjd()
        );
        g2d.setColor(VÄGGFÄRG);
        g2d.setStroke(new BasicStroke(VÄGGTJOCKLEK));
        g2d.drawRect(
            ettRum.getPosX() - HALV_VÄGGTJOCKLEK,
            ettRum.getPosY() - HALV_VÄGGTJOCKLEK,
            ettRum.getBredd() + VÄGGTJOCKLEK,
            ettRum.getHöjd() + VÄGGTJOCKLEK
        );
	}

	private void ritaGångarFrånRum(Graphics g, Rum ettRum) {
        for ( Väderstreck i : Väderstreck.values() ) {
            boolean finnsUtgång = ettRum.finnsUtgångÅt( i );
            if ( ettRum.finnsUtgångÅt( i ) == true ) {
                ritaGång( g, ettRum.gångenÅt( i ));
            }
        }
	}

    private Punkt baspunkt(Rum ettRum, Väderstreck enRiktning) {
        switch ( enRiktning ) {
            case NORR:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd() / 2,
                    ettRum.getPosY()
                );
            case ÖSTER:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd(),
                    ettRum.getPosY() + ettRum.getHöjd() / 2
                );
            case SÖDER:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd() / 2,
                    ettRum.getPosY() + ettRum.getHöjd()
                );
            case VÄSTER:
                return new Punkt(
                    ettRum.getPosX(),
                    ettRum.getPosY() + ettRum.getHöjd() / 2
                );
        }
		return null;
	}

	private Punkt pivotpunkt(Rum ettRum, Väderstreck enRiktning) {
        int offset = HALV_VÄGGTJOCKLEK + VÄGGTJOCKLEK;
        switch ( enRiktning ) {
            case NORR:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd() / 2,
                    ettRum.getPosY() - offset
                );
            case ÖSTER:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd() + offset,
                    ettRum.getPosY() + ettRum.getHöjd() / 2
                );
            case SÖDER:
                return new Punkt(
                    ettRum.getPosX() + ettRum.getBredd() / 2,
                    ettRum.getPosY() + ettRum.getHöjd() + offset
                );
            case VÄSTER:
                return new Punkt(
                    ettRum.getPosX() - offset,
                    ettRum.getPosY() + ettRum.getHöjd() / 2
                );
        }
		return null;
	}

	private void ritaGång(Graphics g, Gång enGång) {
        Punkt fbas = baspunkt( enGång.getFrån(), enGång.getRiktningUtUrFrån());
        Punkt fpivot = pivotpunkt(
            enGång.getFrån(),
            enGång.getRiktningUtUrFrån()
        );
        Punkt tbas = baspunkt( enGång.getTill(), enGång.getRiktningInITill());
        Punkt tpivot = pivotpunkt(
            enGång.getTill(),
            enGång.getRiktningInITill()
        );
        Grafik.drawThickLine(g, fbas, fpivot, VÄGGTJOCKLEK, GÅNGFÄRG);
        Grafik.drawThickLine(g, tbas, tpivot, VÄGGTJOCKLEK, GÅNGFÄRG);
        Grafik.drawThickLine(g, fpivot, tpivot, VÄGGTJOCKLEK, GÅNGFÄRG);
        Grafik.fillCircle(g, fpivot, HALV_VÄGGTJOCKLEK, GÅNGFÄRG);
        Grafik.fillCircle(g, tpivot, HALV_VÄGGTJOCKLEK, GÅNGFÄRG);
	}

	private void ritaMarkörFörVarAnvändarenÄr(Graphics g) {
        Punkt mitt = new Punkt(
            this.enNivå.getCurrentRoom().getPosX() +
            this.enNivå.getCurrentRoom().getBredd() / 2,
            this.enNivå.getCurrentRoom().getPosY() +
            this.enNivå.getCurrentRoom().getHöjd() / 2
        );
        Grafik.fillCircle(g, mitt, HALV_VÄGGTJOCKLEK, ANVÄNDARFÄRG);
	}
}
