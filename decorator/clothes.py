
from decorator import Decorator
from component import Component

class Shapka(Decorator):

    def operation(self) -> str:
       
        return f"A person wears shapka({self.component.operation()})"


class Kurtka(Decorator):
  
    def operation(self) -> str:
        return f"A person wears kurtka({self.component.operation()})"
    
def executor(component: Component) -> None:
   
    print(f"RESULT: {component.operation()}", end="")

   


