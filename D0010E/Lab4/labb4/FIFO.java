import java.util.ArrayList;
import java.util.NoSuchElementException;

public class FIFO implements Queue {
    private ArrayList<Object> queue;
    private int size;
    private int maxSize;
    private int head;

    public FIFO() {
        this.queue = new ArrayList<>();
        this.size = 0;
        this.maxSize = 0;
        this.head = 0;
    }

    public void add( Object item ) {
        if ( this.size() == this.maxSize() ) {
            this.queue.add( item );
            this.maxSize++;
        } else {
            this.queue.add( item );
        }
        this.size++;
    }

    public void removeFirst() {
        first();
        this.queue.remove(0);
        this.size--;
    }

    public int size() {
        return this.size;
    }

    public int maxSize() {
        return this.maxSize;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public Object first() {
        if (this.isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        return this.queue.get(this.head);
    }

    @Override
    public boolean equals(Object f) {
        if (this == f) {
            throw new ClassCastException( f + " is not equals to " + this );
        }
        if (!(f instanceof FIFO)) return false;

        FIFO other = (FIFO) f;
        if (this.size() != other.size()) return false;

        for (int i = 0; i < this.size(); i++) {
            Object thisElem = this.queue.get(i);
            Object otherElem = other.queue.get(i);

            if (thisElem == null) {
                if (otherElem != null) return false;
            } else {
                if (!thisElem.equals(otherElem)) return false;
            }
        }
        return true;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Queue: ");
        for ( Object f : this.queue ) {
            sb.append( "(" + String.valueOf(f) + ") " );
        }
        return sb.toString();
    }
}
