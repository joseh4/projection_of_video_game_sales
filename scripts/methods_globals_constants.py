def build_interaction(data, target, interact):
    """
    When given a dataframe will add interactions base on specified columns names
    
    Parameters
    ----------
    data :  Dataframe 
    target : Column to use for interactions (string)
    interact : Columns by name to create interaction columns from (string)
    
    Returns
    -------
    a dataframe with interactions
    """

    #Add the interaction for Adevnture and platform
    for col in interact:
        data[f'{target}_IN_{col}'] = data[target]  * data.loc[:, col]
        
    return data


def fillna_average_by_target_column(row, avg_dict, target_col, effected_col):
    """
    When given a row of a dataframe, this method will use the target column to fill nan values with 
    the average associated with the catagorical values in the effected column. 
    
    Parameters
    ----------
    row :  Dataframe row.
    avg_dict : A dictionary of the average of the catagorical values in the target column of the dataframe
    target_col : index of where the target column is in the dataframe
    effected_col :  index of where the effected column is in the dataframe
    
    Returns
    -------
    a dataframe row with effect column value changed if it is null
    """
    try:
        if np.isnan(row[effected_col]):      
            row[effected_col] = np.round(avg_dict[row[target_col]], 2)
    except:
        pass #row[effected_col] = "???"
        
    return row

def create_frequency_wide_df(data, col_a, col_b, ints=False):
    """
    Given 2 columns and a dataframe, this method can create new dataframe that can be used to make a wide style dataframe 
    betweem the values in columns A and B. It counts the frequency of values
    
    Parameters
    ----------
    col_a : [String] : column that will be indexed
    col_b : [String] : column where all unique values will be new columns in the new dataframe
    data : [Pandas Dataframe] : the dataframe
    ints : [Boolean] : Determine rather to fill nulls with zeros and convert dataframe values to integers 
    
    Returns
    ----------
    dataframe in wide style
    """
    
    # Create a new dataframe h
    df = pd.DataFrame(data.groupby(col_a)[col_b].value_counts())
    
    #rename column b to represent what it is 
    df.rename(columns={col_b : "value_counts"}, inplace=True)
    
    #Reset index get dataframe in a form where the pivot method will work correctly
    df.reset_index(inplace=True)
    df = df.pivot(index=col_a, columns=col_b, values='value_counts')
    
    if ints == True:
        df = df.fillna(0).astype('int32')   
    
    return df
	
	
NUMERICS = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
"""
GENRE_CRITIC_SCORE_AVG = {'Sports' : video_game_df[video_game_df['Genre'] == 'Sports']['Critic_Score'].mean(),
              'Platform': video_game_df[video_game_df['Genre'] == 'Platform']['Critic_Score'].mean(),
              'Racing': video_game_df[video_game_df['Genre'] == 'Racing']['Critic_Score'].mean(),
              'Role-Playing': video_game_df[video_game_df['Genre'] == 'Role-Playing']['Critic_Score'].mean(),
              'Puzzle': video_game_df[video_game_df['Genre'] == 'Puzzle']['Critic_Score'].mean(),
              'Misc': video_game_df[video_game_df['Genre'] == 'Misc']['Critic_Score'].mean(),
              'Shooter': video_game_df[video_game_df['Genre'] == 'Shooter']['Critic_Score'].mean(),
              'Simulation': video_game_df[video_game_df['Genre'] == 'Simulation']['Critic_Score'].mean(),
              'Action': video_game_df[video_game_df['Genre'] == 'Action']['Critic_Score'].mean(),
              'Fighting': video_game_df[video_game_df['Genre'] == 'Fighting']['Critic_Score'].mean(),
              'Adventure' : video_game_df[video_game_df['Genre'] == 'Adventure']['Critic_Score'].mean(),
              'Strategy' : video_game_df[video_game_df['Genre'] == 'Strategy']['Critic_Score'].mean(),
}

STYLE = {'purple' : '\033[95m',
               'cyan' : '\033[96m',
               'darkcyan' : '\033[36m',
               'blue' : '\033[94m',
               'green' : '\033[92m',
               'yellow' : '\033[93m',
               'red' : '\033[91m',
               'bold' : '\033[1m',
               'underline' : '\033[4m',
               'end' : '\033[0m'
}
"""