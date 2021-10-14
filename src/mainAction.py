
from console import Console
from action import Action
from userLoginAction import UserLoginAction
from userRegisterAction import UserRegisterAction

class MainAction(Action):

    def FollowInstructions(self, info = None):
        Console.Clear()
        print("""********************************\n

Acciones disponibles:
- [R] Registro
- [L] Login
- [T] Terminar

********************************
""")

        return input("Seleccione la acción a ejecutar: ").upper()

    
    def IsValidAction(self, option):
        return option in ["R", "1", "L", "2", "T", "3"]

    
    def GetNextAction(self):
        nextAction = None
        if self.SelectedOption == "R" or self.SelectedOption == "1":
            nextAction = UserRegisterAction(self)
        elif self.SelectedOption == "L" or self.SelectedOption == "2":
            nextAction = UserLoginAction(self)
        elif self.SelectedOption == "T" or self.SelectedOption == "3":
            exit()
        nextAction.Init()
        return self
