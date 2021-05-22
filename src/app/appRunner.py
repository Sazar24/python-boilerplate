from src.app.services.exampleService import ExampleService


class App:
    def run(self):
        print("The App has been started.")

        a: int = ExampleService().getNumber()
        print(f"liczba:  {a}")
