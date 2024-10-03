'''
    This file contains the class definition for the StrawHat class.
'''
from custom import Node,Heap_2
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.crew=Heap_2(0,[])
        for i in range(m):
            new_crewmate=CrewMate()
            self.crew.insert(new_crewmate)
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        min_load_crewmate=self.crew.init_array[0]
        min_load_crewmate.Treasury.append(treasure)
        min_load_crewmate.time_added.append(treasure.arrival_time)
        self.crew.extract()
        if min_load_crewmate.contain_treasure==0:
            self.crew.crewmates_contain_load.append(min_load_crewmate)
            min_load_crewmate.contain_treasure=1

        if min_load_crewmate.current_load > treasure.arrival_time:
            min_load_crewmate.current_load += treasure.size
        else:
            min_load_crewmate.current_load = treasure.size+treasure.arrival_time

        self.crew.insert(min_load_crewmate)

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        
        completion_time_list=[]

        for crew_mate in self.crew.crewmates_contain_load:
            if len(crew_mate.Treasury)!=0:
                treasure_heap = Heap_2(1,[]) # making heap for priority of node of treasure
                arrival_times = crew_mate.time_added # list of arrival_times when treasure added.
                treasures = crew_mate.Treasury # list of treasures.
                current_time = arrival_times[0] # store first treasure arrival time.
                min_p_node = None

                for i in range(len(treasures)):

                    priority=arrival_times[i] + treasures[i].size # priority of ith treasure at arrival time
                    treasure_node = Node(priority,treasures[i]) # make node 

                    attempt_insert = False

                    if min_p_node is None:
                        min_p_node = treasure_node

                    if i>0:
                        time_spent = arrival_times[i]-arrival_times[i-1]
                    
                        while(time_spent!=0 and len(treasure_heap.init_array)):    
                            if time_spent < min_p_node.remaining_size:
                                current_time += time_spent
                                
                                min_p_node.priority-=time_spent
                                min_p_node.remaining_size-=time_spent
                                if min_p_node.priority > treasure_node.priority:
                                    min_p_node = treasure_node
                                elif min_p_node.priority == treasure_node.priority:
                                    if min_p_node.treasure.id > treasure_node.treasure.id:
                                        min_p_node = treasure_node
                                
                                time_spent=0 # update time_spent

                            elif time_spent == min_p_node.remaining_size:
                                current_time += time_spent
                                min_p_node.remaining_size-=time_spent 
                                min_p_node.treasure.completion_time = current_time
                                completion_time_list.append((min_p_node.treasure)) # update completion time list

                                treasure_heap.extract()

                                min_p_node = treasure_heap.top()
                                
                                time_spent=0 # update time_stemp

                            else:
                                current_time+=min_p_node.remaining_size
                                time_spent-=min_p_node.remaining_size # update time_stemp
                                min_p_node.remaining_size=0 #  set remaining size of this node to zero
                                min_p_node.treasure.completion_time = current_time
                                completion_time_list.append((min_p_node.treasure)) # update completion time list

                                treasure_heap.extract()

                                if current_time < arrival_times[i] and len(treasure_heap.init_array)==0:
                                    current_time = arrival_times[i]

                                min_p_node = treasure_heap.top()
                                
                                    
                    if attempt_insert == False:
                        attempt_insert=True
                        if min_p_node is None:
                            min_p_node=treasure_node
                        treasure_heap.insert(treasure_node) # insert treasure_node to treasure_heap assign above

                
                while(len(treasure_heap.init_array)!=0):
                    if min_p_node is None:
                        min_p_node = treasure_heap.init_array[0]
                    current_time+=min_p_node.remaining_size
                    min_p_node.treasure.completion_time = current_time
                    completion_time_list.append((min_p_node.treasure)) # update completion time list
                    treasure_heap.extract()
                    if len(treasure_heap.init_array)!=0:
                        min_p_node = treasure_heap.init_array[0] 

        completion_time_list.sort(key=lambda x: x.id)

        return completion_time_list