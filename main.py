from app.io import input, output
def main():
    console_input=input.console_input('Enter text from console: ')
    file_input=input.file_input('text.txt')
    pandas_input=input.pandas_input('data.csv')

    output.console_output(f'Text from console input: {console_input}')
    output.console_output(f'Text from file input: {file_input}')
    output.console_output(f'Text from pandas input:\n{pandas_input}')

    output.file_output('console_input.txt',console_input)
    output.file_output('file_input.txt',file_input)
    output.file_output('pandas_input.txt',pandas_input)


if __name__=='__main__':
    main()