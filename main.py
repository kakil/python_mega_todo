import functions
import time

def run_todo():

    user_prompt = "Type add, show, edit, complete, or exit: "

    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(now)

    while True:
        user_action = input(user_prompt)
        user_action = user_action.strip()

        if user_action.startswith('add') or user_action.startswith('new'):
            todo = user_action[4:] + '\n'

            todos = functions.get_todos('files/todos.txt')

            # print(f"Current todos: {todos}")
            todos.append(todo.title())
            # print(f"Todos after append: {todos}")

            functions.write_todos(todos)

        elif user_action.startswith('show'):
            todos = functions.get_todos()

            # check if there's any alphanumeric characters in any line
            has_alphanumeric = any(any(char.isalnum() for char in line) for line in todos)
            if not has_alphanumeric:
                print("All todos are complete.")
            else:
                # new_todos = []

               # for item in todos:
               #     new_item = item.strip('\n')
               #     new_todos.append(new_item)
               # new_todos = todos
               #  new_todos = [item.strip('\n') for item in todos]

                for index, item in enumerate(todos):
                    item = item.strip('\n')
                    row = f"{index + 1}- {item}"
                    print(row)

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                number = number - 1

                todos = functions.get_todos()

                new_todo = input("Enter new todo: ")
                todos[number] = new_todo.title() + '\n'

                functions.write_todos(todos)
            except ValueError:
                print("Your command is not valid")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])
                # number = int(input("Number of the todo to complete: "))

                todos = functions.get_todos()

                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)

                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
            except IndexError:
                print("There is no item with that number")
                continue

        elif user_action.startswith('exit'):
            break
        else:
            print("Command is not valid")

    print("Bye!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_todo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
