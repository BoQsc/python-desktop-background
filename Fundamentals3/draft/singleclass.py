class Taskbar():
    #taskbar_exists = False
    def update():
        Taskbar.taskbar_exists = True

Taskbar.update()
print(Taskbar.taskbar_exists)
Taskbar.taskbar_exists = True

def hello():
    print(Taskbar.taskbar_exists)

hello()
input()