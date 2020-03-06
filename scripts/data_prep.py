"""
-Unable to identify developers and rating. classifying nan values as unknown for now
"""

global_df['Developer'].fillna('Unknown', inplace=True)
global_df['Rating'].fillna('Unknown', inplace=True)