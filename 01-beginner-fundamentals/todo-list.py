import os

class TaskObject:
   def __init__(self):
      self.title = ""
      self.description = ""
      self.createAt = None

class TaskManager:
   def __init__(self, file: str):
      self.fileName = file
      if not os.path.exists(self.fileName):
          with open(self.fileName, "x") as f:
              f.write("{}")
   

class AppBase:
   def __init__(self, router: dict):
      self.breadcrumbs = []
      self.router = router

   def navigate_to(self, screen: str, isBack: bool = False):
      self.clean_screen()
      if not isBack:
        self.breadcrumbs.append(screen)
      self.router[screen]()
   
   def header_options(self, options: dict = None):
        inlineOptions = ""
        size = 50
        line = "-"*size

        if options:
            for key, value in options.items():
                inlineOptions = f"{inlineOptions}  [{key}]{value}"

        print(f"{line} Todo List {line}")
        if options:
            print(inlineOptions)

        line = line * 2
        print(f"{line}-----------")

   def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

   def go_back(self):
    if len(self.breadcrumbs) > 0:
        self.breadcrumbs.pop()
        prev = self.breadcrumbs[-1]
        self.navigate_to(prev, True)
    else:
       self.navigate_to("home")

class App(AppBase):
   def __init__(self, task_manager):
      router = {
        "home": self.view_home_screen,
        "new_task": self.view_new_task
      }
      self.task_manager = task_manager
      super().__init__(router)
   
   def nav_input_options(self, label, options:dict):
        while True:
          try:
            result = input(label)
            return options[result]
          except:
              print("Invalid Select Option")

   def view_new_task(self):
        options = {
            "1": "Go to back"
        }
        self.header_options(options)
        
        nav_option = self.nav_input_options("Choose an option: ",{
            "1": self.go_back
        })
        nav_option()

   def view_home_screen(self):
        options = {
            "1": "New task",
            "2": "Move task",
            "3": "Remove task"
        }
        self.header_options(options)
        nav_option = self.nav_input_options("Choose an option: ",{
            "1": lambda : self.navigate_to("new_todo")
        })
        nav_option()

if __name__ == "__main__":
    try:
        task_manager = TaskManager("todo.json")
        app = App(task_manager)
        app.navigate_to("home")
    except:
        os.system('cls' if os.name == 'nt' else 'clear')

