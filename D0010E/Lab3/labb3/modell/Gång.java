package labb3.modell;

public class Gång {

    private Rum från;
    private Väderstreck riktningUtUrFrån;
    private Rum till;
    private Väderstreck riktningInITill;

	public Gång(Rum från, Väderstreck riktningUtUrFrån, Rum till,
			Väderstreck riktningInITill) {
        this.från = från;
        this.riktningUtUrFrån = riktningUtUrFrån;
        this.till = till;
        this.riktningInITill = riktningInITill;
	}

    public Rum getFrån() {
        return this.från;
    }

    public Väderstreck getRiktningUtUrFrån() {
        return this.riktningUtUrFrån;
    }

    public Rum getTill() {
        return this.till;
    }

    public Väderstreck getRiktningInITill() {
        return this.riktningInITill;
    }
}
