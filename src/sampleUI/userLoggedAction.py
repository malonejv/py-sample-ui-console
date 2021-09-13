from businessLogic.noteManager import NoteManager
from sampleUI.action import Action
from sampleUI.console import Console
from sampleUI.noteCreateAction import NoteCreateAction
from sampleUI.noteDeleteAction import NoteDeleteAction
from sampleUI.noteUpdateAction import NoteUpdateAction


class UserLoggedAction(Action):
    
    notesId = {}
    
    def __init__(self, user, parentAction = None):
        self.LoggedUser = user
        super().__init__(parentAction)

    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title(f"Bienvenido { self.LoggedUser.Name }!")
            manager = NoteManager()
            notes = manager.GetByUser(self.LoggedUser.Id)

            i = 1
            for note in notes:
                self.notesId[i]=note.Id
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
            nextAction = NoteCreateAction(self.LoggedUser)
        elif self.SelectedOption == "E" or self.SelectedOption == "2":
            nextAction = NoteDeleteAction(self.LoggedUser, self.notesId)
        elif self.SelectedOption == "M" or self.SelectedOption == "3":
            nextAction = NoteUpdateAction(self.LoggedUser, self.notesId)
        elif self.SelectedOption == "S" or self.SelectedOption == "4":
            return None

        nextAction.Init()
        return self