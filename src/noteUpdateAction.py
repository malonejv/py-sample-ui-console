from businessLogic.noteManager import NoteManager
from entites.note import Note
from action import Action
from console import Console

class NoteUpdateAction(Action):

    notesId = {}
    
    def __init__(self, user, notesId, parentAction = None):
        self.LoggedUser = user
        self.notesId = notesId
        super().__init__(parentAction)

    def FollowInstructions(self):
        try:
            noteIndex  = int(input("Indique la nota a actualizar: "))
            noteId = self.notesId[noteIndex]
            
            manager = NoteManager()
            note = manager.GetById(noteId)

            descriptionMessage = f"Título: {'' if note.Title == None else note.Title }\nDescripción: {'' if note.Description == None else note.Description}"

            Console.Clear()
            Console.Title("Actualizar nota", descriptionMessage, "-")
            
            title  = input("Ingresa título: ")
            description = input("Ingresa descripción: ")
            
            answer = ""
            while answer not in ["S", "N"]:
                Console.Clear()
                answer = input(f"""\n¿Confirma los datos ingresados?[S] SI, [N] NO \n\tTítulo: {title}\n\tDescripción: {description}\nRespuesta: """).upper()
            
            if answer == "S":
                note.Title = title
                note.Description = description
                count = manager.Update(note)
                
                Console.Clear()
                if count >= 1:
                    input("\nSe ha actualizado la nota!")
                else:
                    input("\nNo se ha podido guardar la nota!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")

        return None
    
    
    def IsValidAction(self, option):
        return option == None
