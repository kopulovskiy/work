tasks = []

def add_task(task):
    tasks.append(task)
print("task added.")

def complete_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
    tasks[task_index] = "✓ " + tasks[task_index]
    print("zada4a vipolnena.")
    else:
print ("incorrect index.")

def delete_task(task_index):
    if task_index >= 0 and task_index < len (tasks):
        deleted_task = tasks.pop(task_index)
        print ("zada4a udalena", deleted_task)
    else:
        print ("incorrect index.")

def show_tasks():
    if len(tasks) > 0:
        print ("spisok zada4")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
        else:
            print("spisok pust.")

def todo_list():
    print("simple tasks")
    while true:
        print("simple")
        while True:
            print("\make choise:")
            print("1. add task")
            print("2. mark as complate")
            print("3. delete task")
            print("4. show tasks")
            print("5. exit")

            choice = input("make ur choice(1/2/3/4/5): ") 
            if choice == '1':
                task = input("vedite zada4u:")
                add_task(task)
            elif choice == '2':
                task_index = int(input("vvedite index dlya otmetki"))
                complete_task(task_index)
            elif choice == '3':
                task_index = int(input("show task for delete:"))
                delete_task(task_index)
            elif choice == '4':
                show_tasks()
            elif choice == '5':
                print ("exit")
                break
            else:
                print ("incorrect")

todo_list()
        