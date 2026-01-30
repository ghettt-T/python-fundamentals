task = []
task1 = input("Enter a task: ")
task2 = input("Enter another task: ")
task.append(task1)
task.append(task2)
print("\nYourtask:")
for i in range(len(task)):
    print(f"{i + 1}. {task[i]}")