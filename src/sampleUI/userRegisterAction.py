from businessLogic.userManager import UserManager
from businessLogic.validationException import ValidationException
from entites.user import User
from sampleUI.action import Action
from sampleUI.console import Console

class UserRegisterAction(Action):

    def FollowInstructions(self):
        try:
            Console.Clear()
            Console.Title("Sigue los pasos para registrarte","-")
            names  = input("Ingresa tu(s) nombre(s): ")
            lastNames = input("Ingresa tu(s) apellidos(s): ")
            email  = input("Ingresa tu email: ")
            password  = input("Ingresa tu contraseña: ").encode('utf8')
            passwordConfirm = input("Confirma tu contraseña: ").encode('utf8')
            
            answer = ""
            while answer not in ["S", "N"]:
                Console.Clear()
                answer = input(f"""\n¿Confirma los datos ingresados?[S] SI, [N] NO \n\tNombre(s): {names}\n\tApellido(s): {lastNames}\n\temail(s): {email}\nRespuesta: """).upper()
            
            if answer == "S":
                answer = ""
                fieldToCorrect = None
                manager = UserManager()

                while answer not in ["S", "N"]:
                    user = User(names, lastNames, email, password)
                    try:
                        count = manager.SignUp(user, passwordConfirm)
                    except ValidationException as ex:
                        fieldToCorrect = ex.Field
                        answer = input(f"{str(ex)} \n¿Desea corregir los campos?").upper()
                    else:
                        answer = "N"
                
                    if answer == "S":
                        Console.Clear()
                        if fieldToCorrect == "Password":
                            password  = input("Ingresa tu contraseña: ").encode('utf8')
                            passwordConfirm = input("Confirma tu contraseña: ").encode('utf8')
                        elif fieldToCorrect == "Email":
                            email  = input("Ingresa tu email: ")
                        answer = ""
                    
                Console.Clear()
                if count >= 1:
                    input(f"\nSe ha registrado {user.Email} correctamente!")
                else:
                    input("\nNo se ha podido completar el registro!")
        except Exception:
            print("Oops, ocurrió un error no esperado.")

        return None
    
    
    def IsValidAction(self, option):
        return option == None
