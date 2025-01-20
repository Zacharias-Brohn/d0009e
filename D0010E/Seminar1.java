public class Gauss {
    public static void main(Strin[] args ) {
        int sum = 0;
        for ( int i = 1; i <= 100; i++ ) {
            sum += i;
        }
        System.out.println(sum);
    }
}

public class Loopar {
    public static void main( String[] args ) {
        int n = 0;
        int MAX = 12;

        while ( n < MAX ) {
            System.out.println(n);
            n += 2;
        }
        for ( int j = 1; j <= n; j++ ) {
            if ( n % j == 0 ) {
                System.out.println( j + " delar " + n + " jämnt!" );
            }
        }
        do {
            System.out.println( n );
            n -= 3;
        } while ( n > 0 );
        }
    }
}

public class Skottår {
    static boolean jämntDelbar( int t, int n ) {
        return t % n == 0;
    }
    static boolean ärSkottår( int år ) {
        if ( jämntDelbar( år, 4 ) ) {
            if ( jämntDelbar( år, 100 ) ) {
                return ( jämntDelbar( år, 400 ) );
                } else {
                    return true;
                }
            } else {
                return false;
            }
        }
    }
    public static void main( String[] args ) {
        int årtal = 2024;
        System.out.println( ärSkottår( årtal ) );
    }
}

