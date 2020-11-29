public class Marktanteil
{
    private int kaeuferVonA;
    private int kaeuferVonB;

    // Constructor
    public Marktanteil (int kaeuferVonA, int kaeuferVonB)
    {
        this.kaeuferVonA = kaeuferVonA;
        this.kaeuferVonB = kaeuferVonB;
    }

    // Get kauferA
    public int getKaeuferVonA()
    {
        return kaeuferVonA;
    }

    // get kauferB
    public int getKaeuferVonB()
    {
        return kaeuferVonB;
    }

    /*
    Core Function of this class, updating all states from buyer
    @param bleibBeiA - probability of buyer to buy product A
    @param bleibBeiB - probability of buyer to buy product B
     */
    public Marktanteil naechsterTag(double bleibBeiA, double bleibBeiB)
    {
        double zufall;
        int kaufA = 0, kaufB = 0;

        // Loop over buyer of A
        for (int i = 1; i < kaeuferVonA+1; i++) {
            zufall = Math.random();
            if (zufall <= bleibBeiA) {
                kaufA += 1;
            } else {
                kaufB += 1;
            }
        }

        // Loop over buyer of B
        for (int i = 1; i < kaeuferVonB+1; i++) {
            zufall = Math.random();
            if (zufall <= bleibBeiB) {
                kaufB += 1;
            } else {
                kaufA += 1;
            }
        }

        // Return new object 'Marktanteil' with updated number of buyers
        return new Marktanteil(kaufA, kaufB);
    }

    // Update 'toString()' Methode
    public String toString()
    {
        float alleKaeufer = kaeuferVonA + kaeuferVonB;
        double anteilA = Math.round(100*(kaeuferVonA / alleKaeufer));
        double anteilB = Math.round(100*(kaeuferVonB / alleKaeufer));

        String personA, personB;
        personA = "Käufer Produkt A: " + kaeuferVonA + " (" + anteilA + "%)";
        personB = "Käufer Produkt B: " + kaeuferVonB + " (" + anteilB + "%)";
        return ("Marktanteil " + personA + " " + personB);

    }

}
