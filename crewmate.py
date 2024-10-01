'''
    Python file to implement the class CrewMate
'''
from heap import Heap

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.Treasury=[]
        self.time_added=[]
        self.current_load=0
        self.min_priority_treasure=None
        self.min_priority_node=None # special
    
    # Add more methods if required