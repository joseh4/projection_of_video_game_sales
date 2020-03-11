def build_interactions(data, target, interact):
    """
    When given a dataframe will add interactions base on specified columns names
    
    Parameters
    ----------
    data 		: [Pandas Dataframe] 	: data used to make interactions  
    target 		: [String] 				: Column name to use for interactions
    interact 	: [list of string] 		: Columns by name to create interaction columns from (
    
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
    row 			: Dataframe row.
    avg_dict 		: A dictionary of the average of the catagorical values in the target column of the dataframe
    target_col 		: index of where the target column is in the dataframe
    effected_col 	: index of where the effected column is in the dataframe
    
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
	
def feature_extract_mean_count_median(df, columns, target, return_trig=[True, True, True]):
    """
    Using a dataframe this method can get the mean, median, and count of any columns specified in relation 
    to a target variable. The columns must be catagorical 
    
    Parameters
    ----------
    df          : [Pandas Dataframe] : Dataframe/Data.
    columns     : [List of Strings]  : list of catagory column names
    target      : [String]           : index of where the target column is in the dataframe
    return_trig : [List of Boolean]  : triggers for what extractions to  perform.
                                       Index 1 = Counts, index 2 = mean, index 3 = median 
    
    Returns
    -------
    a dataframe with new features mean, median, and count for all catagorical columns and specfied triggers
    """
    
    for name in columns:
        if return_trig[0] == True:
            _ =  df[name].value_counts()
            df[f'{name}_Count'] = df[name].map(lambda value: _[value])
        if return_trig[1] == True:
            _ =  df.groupby(name).mean()[target]
            df[f'{name}_Mean'] = df[name].map(lambda value: _[value])
        if return_trig[2] == True:
            _ =  df.groupby(name).median()[target]
            df[f'{name}_Median'] = df[name].map(lambda value: _[value])

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