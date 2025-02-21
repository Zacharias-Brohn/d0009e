package labb3.modell;

import java.util.ArrayList;

public enum Väderstreck {
	NORR(0), ÖSTER(1), SÖDER(2), VÄSTER(3);

    private final int tal;

    private Väderstreck(int tal) {
        this.tal = tal;
    }

    public int index() {
        return this.tal;
    }
}
