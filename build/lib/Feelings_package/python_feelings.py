from .python_value_of_feeling import ValueOfFeeling as vf
from random import choice
import pandas as pd
 
class Feelings:
    def __init__(self):
        self.feelings = ["Happy", "Hate", "Calm", "Sad", "Joy", "Anger"]
        self.starter_df = pd.DataFrame(columns = ['Feeling', 'First moment', 'Second moment', 'Third moment', 'Average'])
 
    def create_feel(self, list_of_values, average_value): # create feel by random feeling and the list of average values
        return (choice(self.feelings), *list_of_values, average_value)
    
    def append_datas_to_starter_dataframe(self):
        
        '''
        Iteration: The cycle runs twice, each iteration generates an emotion (can be customized later). 
            
        To create generator objects: 
            vf.number_of_generator_obj(3) creates three generator objects. The average of the moments of generators becomes available. 
            
        To add a new emotion to your DataFrame: Adds the name, three moment values, and average of the new emotion to the starter_df DataFrame.
        
        '''
        
        for _ in range(50): # number of feelings
            vf.number_of_generator_obj(3) # We use 3 generator object, because we have '3 moments' (Number of generator obj)
            
            # Add feelings to DataFrame
            self.starter_df.loc[len(self.starter_df)] = self.create_feel(next(vf.get_list_of_average_values()), 
                                                          vf.get_average_value_from_list_of_average_values())
                  
    def cleared_masked_datas(self): # Masking DataFrame by feelings
        
        '''
        To create a mask: 
        The DataFrame creates a mask (logical indexing) based on each emotion. 
        
        Filtration: Use the mask to filter out lines associated with a particular emotion. 
        
        Generator output: Returns the filtered data and the corresponding emotion name one by one.

        '''
       
        for feeling in self.starter_df['Feeling']:
            mask = self.starter_df['Feeling'] == feeling
             
            datas_by_mask = pd.DataFrame(self.starter_df[mask])
            
            yield datas_by_mask, feeling
           
    def reshape_df_columns_by_feelings_and_they_values(self):
        
        '''
        Change shapes: It replaces the column names with the sentiment names, and then stores the values in a new DataFrame. 
        
        Direction: The new columns are stored sorted, the result is the itemized, sorted snapshot values.
        
        '''
        
        new_df = pd.DataFrame()

        for cleared_masked_datas_with_feeling in self.cleared_masked_datas():
            
            cleared_masked_datas = cleared_masked_datas_with_feeling[0].drop(columns=['Feeling', 'Average']).T
            print("cleared mased datas", cleared_masked_datas)
                     
            new_col = pd.DataFrame(cleared_masked_datas.values.ravel('F'), 
                                   columns = [cleared_masked_datas_with_feeling[1]])
            
            sorted_new_col = new_col.sort_values(by=[cleared_masked_datas_with_feeling[1]]).reset_index(drop=True)
            
            
            new_df[cleared_masked_datas_with_feeling[1]] = sorted_new_col
        
        return new_df
    
    def feelings_one_by_one(self):
        
        '''
        To expand data: Each emotion is displayed on separate lines, with moments and identifiers added.
        
        '''
        
        separated_feelings = []
        
        for cleared_masked_datas_with_feeling in self.cleared_masked_datas():
            
            cleared_masked_datas = cleared_masked_datas_with_feeling[0].drop(columns=['Feeling', 'Average']).T
            
            get_feeling = cleared_masked_datas.stack()
            
            separated_feelings.append(get_feeling.reset_index().rename(columns={'level_0': 'Moments', 'level_1':'feeling_id', 0: 'value'}))
            
        return separated_feelings
 
if __name__ == "__main__":
    Feelings()
 
