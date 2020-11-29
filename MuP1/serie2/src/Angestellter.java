public class Angestellter extends Mitarbeiter
{
    private double gehalt;

    // Constructor
    public Angestellter (String name, double gehalt)
    {
        super(name);
        this.gehalt = gehalt;
    }

    // Setter and Getter "gehalt"
    public double getGehalt() {
        return gehalt;
    }
    public void setGehalt(double gehalt) {
        this.gehalt = gehalt;
    }

    // Method "berechneVerdienst" -> return "getGehalt"
    public double berechneVerdienst() {
        return this.gehalt;
    }

    // Override toString - Method
    public String toString() {
        return String.format("%s Gehalt: %.2f Euro\n", this.getName(), getGehalt());
    }
}
