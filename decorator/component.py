class Component():

    def operation(self) -> str:
        pass


class Person(Component):
   
    def operation(self) -> str:
        return "Person"