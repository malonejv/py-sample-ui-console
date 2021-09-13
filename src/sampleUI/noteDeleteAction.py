from businessLogic.noteManager import NoteManager
from entites.note import Note
from sampleUI.action import Action
from sampleUI.console import Console

class NoteDeleteAction(Action):

    notesId = {}
    
    def __init__(self, user, notesId, parentAction = None):
        self.LoggedUser = user
        self.notesId = notesId
        super().__init__(parentAction)

    def FollowInstructions(self):
        try:
            noteIndex  = int(input("Indique la nota a eliminar: "))
            noteId = self.notesId[noteIndex]
            
            manager = NoteManager()
            note = manager.GetById(noteId)
            Console.Clear()
            
            answer = ""
            while answer not in ["S", "N"]:
                Console.Clear()
                answer = input(f"""\n¿Confirma la eliminación de la nota?[S] SI, [N] NO \n\tTítulo: {note.Title}\n\tDescripción: {note.Description}\nRespuesta: """).upper()
            
            if answer == "S":
                count = manager.Delete(note)
                
                Console.Clear()
                if count >= 1:
                    input("\nSe ha eliminado la nota!")
                else:
                    input("\nNo se ha podido eliminar la nota!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")

        return None
    
    
    def IsValidAction(self, option):
        return option == None
