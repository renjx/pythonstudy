from typing import overload


class Car:
    @overload
    def run(self) -> None:
        pass

    @overload
    def run(self, destination: str) -> str:
        pass

    def run(self, arg=None):
        if arg:
            print(arg)
            return 1
        else:
            print("haha")


car = Car()
car.run(1)
print(type(car.run(1)))
