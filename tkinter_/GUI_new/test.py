class Student:
    name:str
    age:int
    address:str

    def details(self):
        self.name="Rujnee"
        self.age=28
        self.address="Eichendorffstrße 10"

        print(f"Name:{self.name}\nAge:{self.age}\nAddress:{self.address}")


Student().details()