import pandas as pd
def console_input(text=''):
    """
    Function to receive input from the console.

    Parameters:
    - text (str): Optional. Prompt text to display to the user before input.

    Returns:
    - str: The input received from the console.
    """
    return input(text)

def file_input(file_name):
    """
    Function to read input from a file.

    Parameters:
    - file_name (str): The name of the file to read input from.

    Returns:
    - str: The content read from the file.
    """
    with open(f'data/{file_name}','r') as file:
        text=''.join([line for line in file.readlines()])
    return text

def pandas_input(file_name):
    """
    Function to read input from a file using pandas.

    Parameters:
    - file_name (str): The name of the file to read input from.

    Returns:
    - pandas.DataFrame: The data read from the file as a pandas DataFrame.
    """
    data=pd.read_csv(f'data/{file_name}')
    return data.to_string()