public class Mitarbeiter
{
    private String name;

    // Constructor
    public Mitarbeiter (String name) {
        this.name = name;
    }

    // Name
    public String getName() {
        return name;
    }

    // Verdienst
    public double berechneVerdienst () { return 0.0; }

    // Override "toString"
    public String toString() {
        return name;
    }
}
