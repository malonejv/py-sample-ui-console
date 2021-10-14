from __future__ import annotations

class Action:

    def __init__(self, parentAction:Action = None):
        self.ParentAction = parentAction


    def Init(self):
        """
        Summary
            It initialize the workflow of the current action class.\n
            Prints a message if an error occurs.
        """
        try:
            self.SelectedOption=""

            # As long as it is not a valid action, I show an action message to choose.
            while not self.IsValidAction(self.SelectedOption):
                self.SelectedOption = self.FollowInstructions()
            
            # After choose a valid action call to get next action
            self.nextAction = self.GetNextAction()
            

            self.__ChangeAction()

        except Exception:
            print("Oops, ocurrió un error no esperado.")


    def FollowInstructions(self) -> str:
        """
        Defines the message to display on the screen and list the actions that the user can choose.

        ----
        Returns a string that represents the selected action.
        """

        return ""

    def IsValidAction(self, option):
        """
        Evaluates wheather the option passed as parameter is a valid action.

        ----
        Returns true or false wheather the action is valid or not.
        """
        return True

    def GetNextAction(self) -> Action: #para usar mi clase como tipo de devolución importo: from __future__ import annotations
        """
        Gets the selected next action.


        """
        return None

    def __ChangeAction(self):
        """
        Changes the workflow to the next action.
        """
        if self.nextAction != None:
            if self.nextAction.ParentAction != None:
                self.nextAction.ParentAction.Init()
            else:
                self.nextAction.Init()