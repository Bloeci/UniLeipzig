public class Verwaltung
{
    private Mitarbeiter[] mitarbeiter;

    public Verwaltung (int anzahlMitarbeiter)
    {
        mitarbeiter = new Mitarbeiter[anzahlMitarbeiter];
    }

    public Mitarbeiter[] getMitarbeiter() {
        return mitarbeiter;
    }

    // Adding new "Mitarbeiter"
    public boolean addMitarbeiter(Mitarbeiter neuerMitarbeiter)
    {
        boolean checkAdd = false; // Variable for Check state, stay 'false' if array hasn't a empty place
        for (int i = 0; i < mitarbeiter.length; i++)
        {
            if (mitarbeiter[i] == null)
            {
                mitarbeiter[i] = neuerMitarbeiter;
                checkAdd = true;
                break;
            }
        }
        return checkAdd;
    }

    // Remove specific "Mitarbeiter"
    public boolean removeMitarbeiter(Mitarbeiter alterMitarbeiter)
    {
        boolean checkRemove = false; // Variable for Check state, stay 'false' if can't find "Mitarbeiter"
        for (int i = 0; i < mitarbeiter.length; i++)
        {
            if (mitarbeiter[i] == alterMitarbeiter)
            {
                mitarbeiter[i] = null;
                checkRemove = true;
                break;
            }
        }
        return checkRemove;
    }

    // Calculate all cost
    public double berechnePersonalkosten()
    {
        double sumOfAll = 0;
        for (int i = 0; i < mitarbeiter.length; i++)
        {
            if (mitarbeiter[i] != null)
            {
                sumOfAll += mitarbeiter[i].berechneVerdienst();
            }

        }
        return sumOfAll;
    }

    // Employee with less than X hour of work
    public void zeigeArbeiterMitWenigerAlsXStunden(double stunden)
    {
        boolean justZero = true;
        System.out.printf("Arbeiter mit weniger als %.1f Stunden:\n", stunden);
        for (int i = 0; i < mitarbeiter.length; i++)
        {
            // Test for "null" and other classes
            if (mitarbeiter[i] != null && mitarbeiter[i] instanceof Arbeiter)
            {
                if (((Arbeiter) mitarbeiter[i]).getGeleisteteStunden() < stunden)
                {
                    //String arbeiter = ((Arbeiter)mitarbeiter[i]).toString();
                    System.out.print(mitarbeiter[i]); // System.out.print -> calls toString() - Methode
                    justZero = false;
                }
            }

        }

        // Print statement for 0 employees
        if (justZero) System.out.println("Keine Arbeiter gefunden!");
    }
}
