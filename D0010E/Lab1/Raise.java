import java.util.Scanner;

public class Raise {
    private static int recRaiseHalfCount = 0;
    private static int recRaiseOneCount = 0;

    public static double recRaiseHalf( double x, int k ) {
        recRaiseHalfCount++;
        int raiseHalf = k / 2;
        if ( k == 0 ) {
            return 1;
        } else if ( k % 2 == 0 ) {
            return recRaiseHalf( x, raiseHalf ) * recRaiseHalf( x, raiseHalf );
        } else {
            return x * recRaiseHalf( x, raiseHalf ) * recRaiseHalf( x, raiseHalf );
        }
    }

    public static double recRaiseOne( double x, int k ) {
        recRaiseOneCount++;
        if ( k == 0 ) {
            return 1;
        } else {
            return x * recRaiseOne( x, k - 1 );
        }
    }

    public static void main( String[] args ) {
        Scanner scan = new Scanner( System.in );
        double x = 1.5;
        int k = 0;
        do {
            try {
                System.out.print( "\nEnter number for k: " );
                k = scan.nextInt();
                if ( k == 0 ) {
                    break;
                }
                System.out.println( "Half: " + recRaiseHalf( x, k ) );
                System.out.println( "Half count: " + recRaiseHalfCount );
                System.out.println( "One: " + recRaiseOne( x, k ) );
                System.out.println( "One count: " + recRaiseOneCount );
                recRaiseHalfCount = 0;
                recRaiseOneCount = 0;
            } catch ( Exception e ) {
                System.out.println( "Error: Not an integer" );
                scan.next();
            }
        } while ( true );
    }
}