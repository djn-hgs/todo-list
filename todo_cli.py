import todo

my_list = todo.ToDoList()

while True:
    print('Current tasks:')

    for index, task in enumerate(my_list.todo_list):
        print(f'{index} - {task}')

    print('Choices:')
    print('1 - Add task')
    print('2 - Mark task done')
    print('3 - Set task priority')
    print('4 - Delete task')

    choice = input('Select one:')

    if choice == '1':
        ...

    elif choice == '2':
        ...

    elif choice == '3':
        ...

    elif choice == '4':
        ...

    else:
        print('Choice not recognised')