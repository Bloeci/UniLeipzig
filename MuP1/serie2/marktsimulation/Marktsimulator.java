public class Marktsimulator
{
    private double bleibBeiA;
    private double bleibBeiB;
    private Marktanteil[] tagesMarktanteil;

    // Constructor
    public Marktsimulator(
            Marktanteil start, int tage, double bleibBeiA, double bleibBeiB)
    {
        this.bleibBeiA = bleibBeiA;
        this.bleibBeiB = bleibBeiB;

        tagesMarktanteil = new Marktanteil[tage+1];
        tagesMarktanteil[0] = start;

        simuliere();
    }

    // Simulation
    public void simuliere()
    {
        for (int i = 1; i < tagesMarktanteil.length; i++) {
            Marktanteil neuerMarktanteil = tagesMarktanteil[i-1].naechsterTag(bleibBeiA, bleibBeiB);
            tagesMarktanteil[i] = neuerMarktanteil;
        }
    }

    public void zeigeMarktverlauf()
    {
        System.out.println("Marktentwicklung");

        // Print statement for evolution of product A
        System.out.print("Produkt A: ");
        for (int i = 0; i < tagesMarktanteil.length; i++) {
            Marktanteil marktanteilA = tagesMarktanteil[i];
            System.out.print(marktanteilA.getKaeuferVonA() + " ");
        }

        // Print statement for evolution of product B
        System.out.print("\nProdukt B: ");
        for (int i = 0; i < tagesMarktanteil.length; i++) {
            Marktanteil marktanteilB = tagesMarktanteil[i];
            System.out.print(marktanteilB.getKaeuferVonB() + " ");
        }

        System.out.print("\nFinale Marktaufteilung\n");
        System.out.print(tagesMarktanteil[tagesMarktanteil.length - 1].toString());

    }
}
