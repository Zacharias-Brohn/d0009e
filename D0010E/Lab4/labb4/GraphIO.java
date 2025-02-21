import java.util.Arrays;
import java.io.IOException;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class GraphIO {

    static public void readFile(Graph g, String filename) throws IOException {
        try {
            File file = new File( filename );
            Scanner readLine = new Scanner( file );
            if ( !readLine.hasNextLine()) {
                throw new IOException( "File is empty" );
            }
            String firstline = readLine.nextLine();
            if ( !firstline.matches( "\\d+" )) {
                throw new IOException( "First line must be a number" );
            }
            for ( int i = 0; i < Integer.parseInt( firstline ); i++ ) {
                if ( readLine.hasNextLine() ) {
                    String line = readLine.nextLine();
                    String[] strNode = line.split( " " );
                    int[] node = Arrays.stream( strNode )
                        .mapToInt( Integer::parseInt ).toArray();
                    g.addNode( node[ 0 ], node[ 1 ], node[ 2 ] );
                } else {
                    throw new IOException( "File is missing nodes" );
                }
            }
            while ( readLine.hasNextLine() ) {
                String line = readLine.nextLine();
                String[] strEdge = line.split( " " );
                int[] edge = Arrays.stream( strEdge )
                    .mapToInt( Integer::parseInt ).toArray();
                g.addEdge( edge[ 0 ], edge[ 1 ], edge[ 2 ] );
            }
        } catch ( FileNotFoundException e ) {
            throw new IOException( e );
        }
    }
}
