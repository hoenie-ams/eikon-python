"""
Example code to retrieve time series for an index and its constituents.
Step by step with explanations for demo purposes.
"""

import datetime

import eikon
import pandas as pd

# From the "Application ID Generator" in Eikon. Normally you want to hide this in an environment variable.
APPLICATION_ID = 'XXXXXXXXXXXXXXXXXXXX'

# Set the Application ID
eikon.set_app_id(APPLICATION_ID)


def retrieve_time_series(index: str, days: int) -> pd.DataFrame:
    """
    Returns a dataframe with time series data for an index and
    all of its constituents.
    """
    # Define the index RIC and the index chain codes
    index_ric = f'.{index}'
    index_chain = f'0#.{index}'
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=days)

    # Read the index into empty dataframe
    df = eikon.get_timeseries([index_ric],
                              start_date=start,
                              end_date=end,
                              fields='CLOSE')

    # Rename "CLOSE" column to the index name to prevent clash
    df = df.rename(columns={'CLOSE': index_ric})

    # Read in more stocks
    symbols = eikon.get_data(index_chain, 'TR.RIC')[0]['RIC']
    for symbol in symbols:
        df_temp = eikon.get_timeseries([symbol],
                                       start_date=start,
                                       end_date=end,
                                       fields='CLOSE')
        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'CLOSE': symbol})

        # Join the two dataframes
        df = df.join(df_temp[symbol])

    return df


if __name__ == "__main__":
    INDEX = 'OBX'           # Name of the index
    NUMBER_OF_DAYS = 10     # Number of days of history you would like to receive
    print(retrieve_time_series(INDEX, NUMBER_OF_DAYS))
