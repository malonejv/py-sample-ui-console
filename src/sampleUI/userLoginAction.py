from businessLogic.userManager import UserManager
from sampleUI.action import Action
from sampleUI.console import Console
from sampleUI.userLoggedAction import UserLoggedAction


class UserLoginAction(Action):
    
    __LoggedUser = None

    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title("Inicio de sesión",separatorChar="-")
            email  = input("Ingresa tu email: ")
            password  = input("Ingresa tu password: ")

            manager = UserManager()
            self.__LoggedUser = manager.Login(email, password.encode('utf8'))

            if self.__LoggedUser == None:
                input("El usuario y contraseña ingresados no son validos!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")
            
        return None
    
    
    def IsValidAction(self, option):
        return option == None


    def GetNextAction(self):
        if self.__LoggedUser != None:
            nextAction = UserLoggedAction(self.__LoggedUser)
            nextAction.Init()
        return self