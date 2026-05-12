
while True:
    user_action = input("Type add, edit, remove or show :")
    user_action = user_action.strip()          ## TO REMOVE SPACE BEFORE OR AFTER USER INPUT

    match user_action:
        case "add":
            todo = input("Enter a todo :") + "\n"
                                                         ##This part will avoid overwriting in todos.txt
            #file = open("todos.txt", "r")
            #todos = file.readlines()
            #file.close()

            with open("todos.txt" , "r") as file:        # This will do the same as line 10-12
                todos = file.readlines()

            todos.append(todo)

            #file = open("todos.txt" , "w")
            #file.writelines(todos)
            #file.close()

            with open("todos.txt" , "w") as file:
                file.writelines(todos)

        case "show" :
            #file = open("todos.txt" , "r")               #This will show the file content before we run add commanddsa
            #todos = file.readlines()
            #file.close()

            with open("todos.txt" , "r") as file:
                todos = file.readlines()

            ##new_todo = []                                #Here We want to remove the emptly line between each printed item

            ##for i in todos :
                ##new_item = i.strip('\n')
                ##new_todo.append(new_item)       LIST COMPREHENSION         This is just for demonstration to realise what happened

            ## new_todos = [item.strip('\n') for item in todos]    # This will remove the gap between each line


            for index , item in enumerate(todos):
                item = item.strip('\n')                  #LIST COMPREHENSION         # This will remove the gap too
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter a number to edit :"))
            number = number - 1

            with open("todos.txt" , "r") as file:
                todos = file.readlines()

            new_todo = input('Enter a new todo : ')
            todos[number] = new_todo + '\n'

            with open("todos.txt" , "w") as file:
                file.writelines(todos)

        case "complete" :
            number = int(input("Enter a number to complete :"))

            with open("todos.txt" , "r") as file:
                todos = file.readlines()

            index = number -1
            todo_to_temove = todos[index].strip('\n')
            todos.pop(number - 1)

            with open("todos.txt" , "w") as file:
                file.writelines(todos)

            message = f"Task {todo_to_temove} has been completed."

            print(message)

        case "exit":
            break

print("DONE")