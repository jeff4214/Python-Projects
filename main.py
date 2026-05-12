
while True:
    user_action = input("Type add, edit, remove or show :")
    user_action = user_action.strip()          ## TO REMOVE SPACE BEFORE OR AFTER USER INPUT

    match user_action:
        case "add":
            todo = input("Enter a todo :") + "\n"
                                                         ##This part will avoid overwriting in todos.txt
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt" , "w")
            file.writelines(todos)
            file.close()
        case "show" :
            file = open("todos.txt" , "r")               #This will show the file content before we run add commanddsa
            todos = file.readlines()
            file.close()

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
            new_todo = input("Enter a new todo : ")
            file = open("todos.txt" , "r")
            todos = file.readlines()
            file.close()
            todos[number] = new_todo
            file = open("todos.txt" , "w")
            file.writelines(todos)
            file.close()
        case "complete" :
            user_action = int(input("Enter Item you want to delete:"))
            todos.pop(user_action-1)
            file = open("todos.txt" , "w")
            file.writelines(todos)
            file.close()
            file = open("todos.txt" , "r")
            todos = file.readlines()
            file.close()
            print("Done")
        case "exit":
            break

print("DONE")