from backend.businessLogic.abstract.userBusinessComponent import UserBusinessComponent
from action import Action
from console import Console
from userLoggedAction import UserLoggedAction



class UserLoginAction(Action):
    
    __manager = None
    __loggedUser = None

    def __init__(self , manager: UserBusinessComponent, parentAction: Action = None):
        super().__init__(parentAction=parentAction)
        self.__manager = manager
    
    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title("Inicio de sesión",separatorChar="-")
            email  = input("Ingresa tu email: ")
            password  = input("Ingresa tu password: ")

            self.__loggedUser = self.__manager.Login(email, password.encode('utf8'))

            if self.__loggedUser == None:
                input("El usuario y contraseña ingresados no son validos!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")
        return None
    
    
    def IsValidAction(self, option):
        return option == None


    def GetNextAction(self):
        if self.__loggedUser != None:
            nextAction = Provide[Application.loggedAction]# UserLoggedAction(self.__loggedUser)
            nextAction.Init()
        return self