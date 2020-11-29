public class Arbeiter extends Mitarbeiter
{
    private double stundenlohn;
    private double geleisteteStunden;

    public Arbeiter (String name, double stundenlohn, double geleisteteStunden) {
        super(name);
        this.stundenlohn = stundenlohn;
        this.geleisteteStunden = geleisteteStunden;
    }

    // Getter and Setter for attribute "stundenlohn"
    public double getStundenlohn() {
        return stundenlohn;
    }
    public void setStundenlohn(double stundenlohn) {
        this.stundenlohn = stundenlohn;
    }

    // Getter and Setter for attribute "geleisteteStunden"
    public double getGeleisteteStunden() {
        return geleisteteStunden;
    }
    public void setGeleisteteStunden(double geleisteteStunden) {
        this.geleisteteStunden = geleisteteStunden;
    }

    // Method
    public double berechneVerdienst() {
        return (getStundenlohn() * getGeleisteteStunden());
    }

    // Override "toString"
    public String toString() {
        return String.format("%s Stundenlohn: %.2f Euro, geleistete Stunden: %.1f Stunden\n",
                this.getName(), getStundenlohn(), getGeleisteteStunden());
    }

}
