def console_output(text):
    """
    Function to display output to the console.

    Parameters:
    - text (str): The text to be displayed on the console.

    Returns:
    - None
    """
    print(text)


def file_output(file_name,text):
    """
    Function to write output to a file.

    Parameters:
    - file_name (str): The name of the file to write output to.
    - text (str): text to output to file

    Returns:
    - None
    """
    with open(f'data/{file_name}','w') as file:
        file.write(text)

