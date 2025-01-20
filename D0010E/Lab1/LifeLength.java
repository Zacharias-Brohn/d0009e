import java.util.Scanner;
import java.util.LinkedHashMap;
import java.util.Map;

public class LifeLength {
    public static int iterateF( int a0, int n ) {
        int value = a0;
        for ( int i = 0; i < n; i++ ) {
            value = f1( value );
        }
        return value;
    }

    public static int recLifeLength( int a0 ) {
        count = 0;
        if ( a0 == 1 ) {
            return 0;
        } else {
            return 1 + recLifeLength( f1( a0 ) );
        }
    }

    public static int iterLifeLength( int a0 ) {
        int value = a0;
        int count = 0;
        while ( value != 1 ) {
            value = f1( value );
            count++;
        }
        return count;
    }

    public static String intsToString( int a0 ) {
        return "The life length of " + a0 + " is " + iterLifeLength( a0 ) + ".";
    }

    public static int f1( int a0 ) {
        if ( a0 == 1 ) {
            return 1;
        } else if (a0 % 2 == 0) {
            return a0 / 2;
        } else {
            return 3 * a0 + 1;
        }
    }

    public static int f2( int a0 ) {
        int value = f1( a0 );
        return f1( value );
    }

    public static int f4( int a0 ) {
        int value = f2( a0 );
        return f2( value );
    }

    public static int f8( int a0 ) {
        int value = f4( a0 );
        return f4( value );
    }

    public static int f16( int a0 ) {
        int value = f8( a0 );
        return f8( value );
    }

    public static int f32( int a0 ) {
        int value = f16( a0 );
        return f16( value );
    }

    public static void main( String[] args ) {
        int a0 = 0;
        int n = 0;
        Scanner scan = new Scanner( System.in );
        do {
            try {
                System.out.print( "Skriv in ett heltal (> 0): " );
                a0 = scan.nextInt();

                if ( a0 == 0 ) {
                    break;
                }

                System.out.print( "\n" + intsToString( a0 ) + "\n" );
            } catch ( Exception e ) {
                System.out.println( "\nFel: Ej ett heltal > 0\n" );
                // Clear scanner buffer
                scan.next();
            }
        //do {
        //    try {
        //        System.out.print( "Skriv in ett heltal (> 0): " );
        //        a0 = scan.nextInt();
        //
        //        if ( a0 == 0 ) {
        //            break;
        //        }
        //
        //        System.out.print( "\nAnge antal iterationer (> 0): " );
        //        n = scan.nextInt();
        //
        //        System.out.println( 
        //            "\nf" + n + "(" + a0 + ") = " + iterateF( a0, n ) + "\n" 
        //        );
        //
        //    } catch ( Exception e ) {
        //        System.out.println( "\nFel: Ej ett heltal > 0\n" );
        //        // Clear scanner buffer
        //        scan.next();
        //    }
            

        //do {
        //    try {
        //        System.out.print( "Skriv in ett heltal större än 0: " );
        //        a0 = scan.nextInt();
        //    } catch ( Exception e ) {
        //        System.out.println( "Fel: Ej ett heltal > 0" );
        //    }
        //    if ( a0 == 0 ) {
        //        break;
        //    }


            //// LinkedHashMap of function values
            //LinkedHashMap<String, Integer> dictionary = new LinkedHashMap<>();
            //dictionary.put( "f(1)", f1( a0 ) );
            //dictionary.put( "f(2)", f2( a0 ) );
            //dictionary.put( "f(4)", f4( a0 ) );
            //dictionary.put( "f(8)", f8( a0 ) );
            //dictionary.put( "f(16)", f16( a0 ) );
            //dictionary.put( "f(32)", f32( a0 ) ); 
            //
            //// Print out the values one after another
            //for (Map.Entry<String, Integer> entry : dictionary.entrySet()) {
            //    System.out.println(entry.getKey() + " = " + entry.getValue() + "\n");
            //}
        } while ( a0 > 0 );
        scan.close();
    }
}
