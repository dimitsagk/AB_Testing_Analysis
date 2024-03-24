import pandas as pd

def cleaning(df_clients, df_trace, df_roster):
    '''
    Function for data cleaning, addressing issues identified during initial exploration.
    Takes the three dataframes as input and returns three cleaned dataframe. Additionally, provides a dataframe 
    from df_clients with rows containing only client_id values, if needed for further analysis.
    '''

    ## Dropping null values

    # Making a dataframe with the rows that only have client_id, and will be deleted, in case I need it in the future
    df_clients_with_na =  df_clients[df_clients.isna().sum(axis=1) > 7]
    # Making a new dataframe with deleted rows that have as values only the client_id
    df_clients = df_clients.dropna(thresh = 8)


    ## Dropping duplicated values
    df_trace = df_trace.drop_duplicates()
    
    
    ## Filling null values

    # Replacing the null values at df_roster with "Undefined"
    df_roster["Variation"] = df_roster["Variation"].apply(str).replace('nan','Undefined')


    ## Formatting

    # Formatting df_roster columns as lowercase, to match all the other colomn names
    df_roster.columns = df_roster.columns.map(str.lower)
    # "client_id" to be casted as string, no intention to to perform mathematical operations on it
    df_roster.client_id = df_roster.client_id.apply(str)
    
    # "client_id" to be casted as string, no intention to to perform mathematical operations on it
    df_clients.client_id = df_clients.client_id.apply(str)
    # casting the columns that I have tested are not real float number to integers
    df_clients[["clnt_tenure_yr","clnt_tenure_mnth","num_accts", "calls_6_mnth",
                "logons_6_mnth"]] = df_clients[["clnt_tenure_yr","clnt_tenure_mnth","num_accts", "calls_6_mnth","logons_6_mnth"]].map(int)

    # "client_id" to be casted as string, no intention to to perform mathematical operations on it
    df_trace.client_id = df_trace.client_id.apply(str)
    # casting date_time as datetime pandas object
    df_trace.date_time = pd.to_datetime(df_trace.date_time,format='%Y-%m-%d %H:%M:%S')


    return df_clients, df_trace, df_roster, df_clients_with_na
