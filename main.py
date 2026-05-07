from operator import index

todos = []

while True:
    user_action = input("Type add, edit or show :")
    user_action = user_action.strip()          ## TO REMOVE SPACE BEFORE OR AFTER USER INPUT

    match user_action:
        case "add":
            todo = input("Enter a todo :")
            todos.append(todo.capitalize())
        case "show" :
            for index , item in enumerate(todos):  ## to count the items
                 print(index ,"-" ,  item)
        case "edit":
            number = int(input("Enter a number to edit :"))
            number = number - 1
            new_todo = input("Enter a new todo")
            todos[number] = new_todo.capitalize()
        case "exit":
            break
print("DONE")