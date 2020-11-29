public class Main {

    public static void main(String[] args) {

        Marktanteil startMarkt = new Marktanteil(5000, 5000);
        Marktsimulator marktsimulator = new Marktsimulator(startMarkt, 20, 0.8, 0.7);
        marktsimulator.zeigeMarktverlauf();

    }

}
