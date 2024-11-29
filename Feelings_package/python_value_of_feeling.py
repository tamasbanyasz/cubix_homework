from numpy import fromiter, average
from random import randint

class ValueOfFeeling:
    def __init__(self):
        self.list_of_average_values = []
    
    @classmethod    
    def create_generator_obj(cls,fromiter_end):  # Create generator object with specified iterable range 0-2. 
        
        print("Generator object: ", fromiter((i for i in range(0, fromiter_end)), int))
        return (i for i in range(0, fromiter_end))
        
        '''
            fromiter_end = 3;  # Numbers 0 to 2
            
            # 1 moment
            Generator object:  [0 1]
            
            # 2 moment
            Generator object:  [0 1 2]
            
            # 3 moment
            Generator object:  [0 1 2]
            
        '''
    
    @classmethod
    def number_of_generator_obj(cls, number_of_generator_obj):
        
        '''
        Add to a list the average of the generator object in fast way.
        
        The "number_of_generator_obj" define the wanted number of generator objects.
        
        In this case we would like 3 object because of the 'First moment', 'Second moment', 'Third moment'.
        
        Then we added each moment's average values to list. 
        
        '''
        
        cls.list_of_average_values = ([average(next(cls.create_generator_obj(randint(1, 300000)))) for i in range(number_of_generator_obj)])
        print(f"Average list: {cls.list_of_average_values}")
        
        for i in range(number_of_generator_obj):
            print(f"Check {i + 1} - Generator object's average value")
            print(average(next(cls.create_generator_obj(randint(1, 3)))))
            
            '''
            
             # 1 moment
            Check 1 - Generator object's average value
                Generator object:  [0 1 2]
                
                1.0
                
            # 2 moment    
            Check 1 - Generator object's average value
                Generator object:  [0 1]
                
                0.5
            
            # 3 moment
            Check 3 - Generator object's average value
            Generator object:  [0 1]
            
                0.5
            
            '''

    @classmethod
    def get_list_of_average_values(cls):
        yield iter(cls.list_of_average_values) # Get the full list with the average values
        
        '''
                       First moment    Second momment   Third moment
        Average list: [np.float64(0.5), np.float64(1.0), np.float64(1.0)]
        
        '''
           
    @classmethod   
    def get_average_value_from_list_of_average_values(cls): # Get the each row average values from the list
        return average(cls.list_of_average_values, axis=0)
    
    '''
            Feeling  First moment  Second moment  Third moment   Average
        1   Happy           0.5            1.0           1.0     0.833333
        
    '''
    
if __name__ == "__main__":
    ValueOfFeeling()

