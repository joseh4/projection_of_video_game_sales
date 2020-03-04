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

GENRE_CRITIC_COUNT_AVG = {'Sports' : video_game_df[video_game_df['Genre'] == 'Sports']['Critic_Count'].mean(),
              'Platform': video_game_df[video_game_df['Genre'] == 'Platform']['Critic_Count'].mean(),
              'Racing': video_game_df[video_game_df['Genre'] == 'Racing']['Critic_Count'].mean(),
              'Role-Playing': video_game_df[video_game_df['Genre'] == 'Role-Playing']['Critic_Count'].mean(),
              'Puzzle': video_game_df[video_game_df['Genre'] == 'Puzzle']['Critic_Count'].mean(),
              'Misc': video_game_df[video_game_df['Genre'] == 'Misc']['Critic_Count'].mean(),
              'Shooter': video_game_df[video_game_df['Genre'] == 'Shooter']['Critic_Count'].mean(),
              'Simulation': video_game_df[video_game_df['Genre'] == 'Simulation']['Critic_Count'].mean(),
              'Action': video_game_df[video_game_df['Genre'] == 'Action']['Critic_Count'].mean(),
              'Fighting': video_game_df[video_game_df['Genre'] == 'Fighting']['Critic_Count'].mean(),
              'Adventure' : video_game_df[video_game_df['Genre'] == 'Adventure']['Critic_Count'].mean(),
              'Strategy' : video_game_df[video_game_df['Genre'] == 'Strategy']['Critic_Count'].mean(),
}


# Fix user score to get the average values
video_game_df['User_Score'] = video_game_df['User_Score'].replace(to_replace = 'tbd', value = np.nan).astype(float)

GENRE_USER_SCORE_AVG = {'Sports' : video_game_df[video_game_df['Genre'] == 'Sports']['User_Score'].mean(),
              'Platform': video_game_df[video_game_df['Genre'] == 'Platform']['User_Score'].mean(),
              'Racing': video_game_df[video_game_df['Genre'] == 'Racing']['User_Score'].mean(),
              'Role-Playing': video_game_df[video_game_df['Genre'] == 'Role-Playing']['User_Score'].mean(),
              'Puzzle': video_game_df[video_game_df['Genre'] == 'Puzzle']['User_Score'].mean(),
              'Misc': video_game_df[video_game_df['Genre'] == 'Misc']['User_Score'].mean(),
              'Shooter': video_game_df[video_game_df['Genre'] == 'Shooter']['User_Score'].mean(),
              'Simulation': video_game_df[video_game_df['Genre'] == 'Simulation']['User_Score'].mean(),
              'Action': video_game_df[video_game_df['Genre'] == 'Action']['User_Score'].mean(),
              'Fighting': video_game_df[video_game_df['Genre'] == 'Fighting']['User_Score'].mean(),
              'Adventure' : video_game_df[video_game_df['Genre'] == 'Adventure']['User_Score'].mean(),
              'Strategy' : video_game_df[video_game_df['Genre'] == 'Strategy']['User_Score'].mean(),
}

GENRE_USER_COUNT_AVG = {'Sports' : video_game_df[video_game_df['Genre'] == 'Sports']['User_Count'].mean(),
              'Platform': video_game_df[video_game_df['Genre'] == 'Platform']['User_Count'].mean(),
              'Racing': video_game_df[video_game_df['Genre'] == 'Racing']['User_Count'].mean(),
              'Role-Playing': video_game_df[video_game_df['Genre'] == 'Role-Playing']['User_Count'].mean(),
              'Puzzle': video_game_df[video_game_df['Genre'] == 'Puzzle']['User_Count'].mean(),
              'Misc': video_game_df[video_game_df['Genre'] == 'Misc']['User_Count'].mean(),
              'Shooter': video_game_df[video_game_df['Genre'] == 'Shooter']['User_Count'].mean(),
              'Simulation': video_game_df[video_game_df['Genre'] == 'Simulation']['User_Count'].mean(),
              'Action': video_game_df[video_game_df['Genre'] == 'Action']['User_Count'].mean(),
              'Fighting': video_game_df[video_game_df['Genre'] == 'Fighting']['User_Count'].mean(),
              'Adventure' : video_game_df[video_game_df['Genre'] == 'Adventure']['User_Count'].mean(),
              'Strategy' : video_game_df[video_game_df['Genre'] == 'Strategy']['User_Count'].mean(),
}


PUBLISHER_GLOBAL_AVG = {}

for publisher in global_df['Publisher'].unique():
    PUBLISHER_GLOBAL_AVG[publisher] = global_df[global_df['Publisher'] == publisher]['Global_Sales'].mean()


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


NUMERICS = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']