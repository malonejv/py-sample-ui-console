from backend.businessLogic.abstract.noteBusinessComponent import NoteBusinessComponent
from action import Action
from console import Console
from noteCreateAction import NoteCreateAction
from noteDeleteAction import NoteDeleteAction
from noteUpdateAction import NoteUpdateAction


class UserLoggedAction(Action):
    
    __loggedUser=None
    __manager = None
    __notesId = {}
    
    def __init__(self, user, manager: NoteBusinessComponent, parentAction = None):
        super().__init__(parentAction)
        self.__loggedUser = user
        self.__manager = manager

    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title(f"Bienvenido { self.__loggedUser.Name }!")
            
            notes = self.__manager.GetByUser(self.__loggedUser.Id)

            i = 1
            for note in notes:
                self.__notesId[i]=note.Id
                print(f"{i} - { note.Title}")
                i+=1
            print("""\n********************************

Acciones disponibles:
    - [C] Crear nota
    - [E] Eliminar nota
    - [M] Modificar nota
--------------------------------
    - [S] Cerrar sesión

********************************
""")
        except Exception:
            print("Oops, ocurrió un error no esperado.")

        return input("Seleccione la acción a ejecutar: ").upper()

    
    def IsValidAction(self, option):
        return option in ["C", "E", "M", "S", "1", "2", "3", "4"]

    def GetNextAction(self):
        nextAction = None

        if self.SelectedOption == "C" or self.SelectedOption == "1":
            nextAction = NoteCreateAction(self.__loggedUser)
        elif self.SelectedOption == "E" or self.SelectedOption == "2":
            nextAction = NoteDeleteAction(self.__loggedUser, self.__notesId)
        elif self.SelectedOption == "M" or self.SelectedOption == "3":
            nextAction = NoteUpdateAction(self.__loggedUser, self.__notesId)
        elif self.SelectedOption == "S" or self.SelectedOption == "4":
            return None

        nextAction.Init()
        return self