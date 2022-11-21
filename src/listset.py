"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        ...  # FIXME

        y = list(init) #O(init)
        self.data = []  #O(1)

        for i in y: #O(y)
            if i not in self.data: 
                self.data.append(i)
        
        # O(init+y^selv.data) 
                
    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  # FIXME

        for i in self.data:
            if x == i:
                return True
        return False

        #O(selv.data) linear time

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ...  # FIXME

        if not self.data:
            return False
        else:
            return True

        #O(selv.data) linear time

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  # FIXME

        if x not in self.data:
            self.data.append(x)
        
        #O(selv.data) linear time

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...  # FIXME

        self.data.remove(x)

        #O(selv.data) linear time
    
    def __repr__(self) -> str:
        return f'{self.data}'

