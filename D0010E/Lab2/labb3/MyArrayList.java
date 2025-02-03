package labb3;

import java.io.Serializable;
import java.util.Collection;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.RandomAccess;
import java.util.Spliterator;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;

@SuppressWarnings("serial")
public class MyArrayList<E> implements Serializable, Cloneable, Iterable<E>,
		Collection<E>, List<E>, RandomAccess {

    	// ---------------------------------------------------------------

	public static void main(String[] args) {
		MyArrayList<String> strlist = new MyArrayList<String>();
		System.out.println(strlist.add( "hi" ) );
		// testa metoder härifrån
		
	}

    	// ---------------------------------------------------------------
    
    private E[] array;
    private int size;

	public MyArrayList(int initialCapacity) {
		/* ska implementeras */
        if ( initialCapacity < 0 ) {
            throw new IllegalArgumentException( "Illegal Capacity: " + initialCapacity );
        }

        array = ( E[] ) new Object[ initialCapacity ];
        size = 0;
	}

	public MyArrayList() {
		/* ska implementeras */
        this( 10 );
	}

    private void checkIndex( int index ) {
        if ( index < 0 || index >= size ) {
            throw new IndexOutOfBoundsException( "Incorrect index: " + index );
        }
    }

	// -- 1 --

	@Override
	public int size() {
		/* ska implementeras */
	    return size;
	}

	@Override
	public boolean isEmpty() {
		/* ska implementeras */
        return size == 0;
	}

	@Override
	public void clear() {
		/* ska implementeras */
        array = ( E[] ) new Object[ array.length ];
        size = 0;
    }

	// -- 2 --

	public void ensureCapacity(int minCapacity) {
		/* ska implementeras */
        if ( array.length < minCapacity ) {
            E[] newArray = ( E[] ) new Object[ minCapacity ];
            System.arraycopy( array, 0, newArray, 0, size );
            array = newArray;
        }
	}

	public void trimToSize() {
		/* ska implementeras */
        if ( array.length > size ) {
            ensureCapacity( size );
        }
	}
    
	// -- 3 --
    
	@Override
	public void add(int index, E element) {
		/* ska implementeras */
        checkIndex( index );
        ensureCapacity( size + 1 );

        System.arraycopy(
            array,
            index,
            array,
            index + 1,
            ( size - 1 ) - index
        );

        array[ index ] = element;
        size++;
	}

	@Override
	public boolean add(E e) {
		/* ska implementeras */
        ensureCapacity( size + 1 );

        array[ size ] = e;
        size++;
		return true;
    }

        // -- 4 --
    
	@Override
	public E get(int index) {
		/* ska implementeras */
        checkIndex( index );
		return array[ index ]; /* bara med för att Eclipse inte ska klaga */
	}

	@Override
	public E set(int index, E element) {
		/* ska implementeras */
        checkIndex( index );

        E originalElement = get( index );

        array[ index ] = element;

		return originalElement; /* bara med för att Eclipse inte ska klaga */
	}

	// -- 5 --

	@Override
	public E remove(int index) {
		/* ska implementeras */
        checkIndex( index );

        E originalElement = get( index );

        System.arraycopy( 
            array,
            index + 1,
            array, index,
            ( size - 1 ) - index 
        );

        array[ size - 1 ] = null;
        size--;

		return originalElement; /* bara med för att Eclipse inte ska klaga */
	}

	protected void removeRange(int fromIndex, int toIndex) {
		/* ska implementeras */
        if ( fromIndex > toIndex ) {
            throw new IndexOutOfBoundsException( 
                fromIndex + " is larger than " + toIndex 
            );
        }
        checkIndex( fromIndex );
        checkIndex( toIndex + 1 );

        System.arraycopy( array, toIndex, array, fromIndex, size - toIndex );

        for ( int i = size - ( toIndex - fromIndex ); i < toIndex; i++ ) {
            array[ i ] = null;
        }
	}

	// -- 6 --

	@Override
	public int indexOf(Object o) {
		/* ska implementeras */
        for ( int i = 0; i < size - 1; i++ ) {
            if ( o.equals( get( i ) ) ) {
                return i;
            }
        }
		return -1;
	}

	@Override
	public boolean remove(Object o) {
		/* ska implementeras */
        int index = indexOf( o );
        if ( contains( o ) ) {
            remove( index );
            return true;
        }
		return false;
	}
    
	@Override
	public boolean contains(Object o) {
		/* ska implementeras */
        int index = indexOf( o );
        if ( o == get( index ) ) {
            return true;
        }
		return false; /* bara med för att Eclipse inte ska klaga */
	}

	// -- 7 --

	@Override
	public Object clone() {
		/* ska implementeras */
        try {
            MyArrayList<E> clonedArray = ( MyArrayList<E> ) super.clone();
            clonedArray.array = this.array.clone();
            return clonedArray;
        } catch ( CloneNotSupportedException e ) {
            throw new AssertionError();
        }
	}

	@Override
	public Object[] toArray() {
		/* ska implementeras */
        Object[] newArray = new Object[ size - 1 ];
        System.arraycopy( array, 0, newArray, 0, size - 1 );
		return newArray; /* bara med för att Eclipse inte ska klaga */
	}

	// --- Rör ej nedanstående kod -----------------------------------

	public MyArrayList(Collection<? extends E> c) {
		throw new UnsupportedOperationException();
	}

	private class InternalIterator implements Iterator {
		int current = 0;

		@Override
		public boolean hasNext() {
			return current < size();
		}

		@Override
		public Object next() {
			return get(current++);

		}

	}

	@Override
	public Iterator<E> iterator() {
		return new InternalIterator();
	}

	@Override
	public boolean addAll(int index, Collection<? extends E> c) {
		throw new UnsupportedOperationException();
	}

	@Override
	public boolean addAll(Collection<? extends E> c) {
		throw new UnsupportedOperationException();
	}

	@Override
	public boolean removeAll(Collection<?> c) {
		throw new UnsupportedOperationException();
	}

	@Override
	public boolean retainAll(Collection<?> c) {
		throw new UnsupportedOperationException();
	}

	@Override
	public int lastIndexOf(Object o) {
		throw new UnsupportedOperationException();
	}

	@Override
	public <T> T[] toArray(T[] a) {
		throw new UnsupportedOperationException();
	}

	@Override
	public ListIterator<E> listIterator(int index) {
		throw new UnsupportedOperationException();
	}

	@Override
	public ListIterator<E> listIterator() {
		throw new UnsupportedOperationException();
	}

	@Override
	public List<E> subList(int fromIndex, int toIndex) {
		throw new UnsupportedOperationException();
	}

	@Override
	public void forEach(Consumer<? super E> action) {
		throw new UnsupportedOperationException();
	}

	@Override
	public Spliterator<E> spliterator() {
		throw new UnsupportedOperationException();
	}

	@Override
	public boolean removeIf(Predicate<? super E> filter) {
		throw new UnsupportedOperationException();
	}

	@Override
	public void replaceAll(UnaryOperator<E> operator) {
		throw new UnsupportedOperationException();
	}

	@Override
	public void sort(Comparator<? super E> c) {
		throw new UnsupportedOperationException();
	}

	@Override
	public boolean containsAll(Collection<?> c) {
		throw new UnsupportedOperationException();
	}

}
