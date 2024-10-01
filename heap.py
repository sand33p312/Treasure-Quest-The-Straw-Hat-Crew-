'''
Python Code to implement a heap with general comparison function
'''
def comparison_function(key1,key2):
    pass

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.init_array=init_array
        # self.comparison_function=comparison_function
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.init_array.append(value)
        self._upheap(len(self.init_array)-1)
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if len(self.init_array)!=0:
            self._swap(0,len(self.init_array)-1)
            min_element=self.init_array.pop()
            self._downheap(0)
            return min_element

    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if len(self.init_array)!=0:
            return self.init_array[0]
    
    # You can add more functions if you want to

    def _parent(self,j):
        return (j-1)//2
    
    def _left(self,j):
        return 2*j+1
    
    def _right(self,j):
        return 2*j+2
    
    def _has_left(self,j):
        return self._left(j)<len(self.init_array)
    
    def _has_right(self,j):
        return self._right(j)<len(self.init_array)
    
    def _swap(self,i,j):
        self.init_array[i],self.init_array[j] = self.init_array[j],self.init_array[i]
    
    def _upheap(self,j):
        parent=self._parent(j)
        if j>0 and self.init_array[parent] > self.init_array[j]:
            self._swap(j,parent)
            self._upheap(parent)

    def _downheap(self,j):
        if self._has_left(j):
            left=self._left(j)
            small_child=left
            if self._has_right(j):
                right=self._right(j)
                if self.init_array[right]<self.init_array[left]:
                    small_child=right
            if self.init_array[j]>self.init_array[small_child]:
                self._swap(j,small_child)
                self._downheap(small_child)
                

            