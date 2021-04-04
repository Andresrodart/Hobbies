import java.text.Collator;

/**
 * Exmaple
 */
public class Exmaple {

    public static void main(String[] args) {
        // Compare two strings in the default locale
        Collator myCollator = Collator.getInstance();
        if( myCollator.compare("tamaño", "tamano") == 0 )
            System.out.println("abc is less than ABC");
        else
            System.out.println("abc is greater than or equal to ABC");
    }
}