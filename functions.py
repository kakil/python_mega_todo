FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local

def write_todos(todos_local, filepath=FILEPATH):
    """
    Write the to-do item list in a text file
    :param todos_local: list of items read
    :param filepath: path to the file
    :return:
    """
    with open(filepath, 'w') as file_local:

     file_local.writelines(todos_local)