# from backend.businessLogic.noteManager import NoteManager
from entites.note import Note
from action import Action
from console import Console

class NoteCreateAction(Action):

    def __init__(self, user, parentAction = None):
        self.LoggedUser = user
        super().__init__(parentAction)

    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title("Crear nota", separatorChar="-")
            title  = input("Ingresa título: ")
            description = input("Ingresa descripción: ")
            
            answer = ""
            while answer not in ["S", "N"]:
                Console.Clear()
                answer = input(f"""\n¿Confirma los datos ingresados?[S] SI, [N] NO \n\tTítulo: {title}\n\tDescripción: {description}\nRespuesta: """).upper()
            
            if answer == "S":
                note = Note(title=title, description=description, userId=self.LoggedUser.Id)
                manager = NoteManager()
                count = manager.Create(note)
                
                Console.Clear()
                if count >= 1:
                    input("\nSe agrego una nueva nota!")
                else:
                    input("\nNo se ha podido guardar la nota!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")

        return None
    
    
    def IsValidAction(self, option):
        return option == None
