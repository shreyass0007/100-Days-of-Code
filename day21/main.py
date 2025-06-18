class Animal:
    def __init__(self):
        self.num_eye=2
    def breath(self):
        print("Inhale,Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("movng in water")
    def breathe(self):
        super().breath()
        print("doing under water")


nemo=Fish()
nemo.swim()
nemo.breathe()
