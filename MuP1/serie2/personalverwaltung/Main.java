import java.util.Locale;

public class Main {
    public static void main(String[] args)
    {
        Locale.setDefault(Locale.US); // Points in decimal numbers

        Verwaltung verwaltung = new Verwaltung(20);
        // Initialize all new objects of type "Angestellter" or "Arbeiter"
        verwaltung.addMitarbeiter(new Angestellter("Klaus Schmidt", 4200));
        verwaltung.addMitarbeiter(new Angestellter("Peter Altmaier", 2500));
        verwaltung.addMitarbeiter(new Angestellter("Lisa Poepping", 3100));

        verwaltung.addMitarbeiter(new Arbeiter("Kurt Wovoreit", 26, 8));
        verwaltung.addMitarbeiter(new Arbeiter("Michelle Johanson", 31, 7));
        verwaltung.addMitarbeiter(new Arbeiter("Judith Schole", 51, 48));

        // Just for demonstration of removing -> add sabine
        Mitarbeiter sabine = new Angestellter("Sabine Adler", 4050);
        verwaltung.addMitarbeiter(sabine);

        // ------------------------------------------------
        // Tasks from worksheet
        System.out.printf("Personalkosten: %.2f Euro\n", verwaltung.berechnePersonalkosten());

        verwaltung.removeMitarbeiter(sabine); // remove one employee
        System.out.printf("Personalkosten: %.2f Euro\n", verwaltung.berechnePersonalkosten());

        System.out.print("\n");
        verwaltung.zeigeArbeiterMitWenigerAlsXStunden(10); // Employees with less than x hours of work

    }
}
