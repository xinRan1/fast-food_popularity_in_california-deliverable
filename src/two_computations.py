#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pandas as pd
import numpy as np



def get_time_period(dates1, dates2):
    """returns a dates list that contains dates in the period of investigation
    dates1 array
    dates2 array"""
    # get the start date and end date of the period 
    first_date = datetime.datetime.strptime(dates1[0], '%Y-%m-%d').date()
    last_date = datetime.datetime.strptime(dates1[-1], '%Y-%m-%d').date()
    all_dates = np.concatenate((dates1, dates2))
    dates_list = []
    # get dates in this period from two dates lists
    for date in all_dates:
        date_t = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if date_t >= first_date and date_t <= last_date:
            dates_list.append(date_t)
    # convert the format of dates list to string as the indices of dataframes do  
    dates = [date.strftime('%Y-%m-%d') for date in dates_list]
    return dates

def county_with_most_popularity(df):
    """returns the name of county with the most fast-food popularity
    df pandas dataframe"""
    df_in_order = df.sort_values(by=['Total_popularity'], ascending=False)
    return df_in_order.County.values[0]

