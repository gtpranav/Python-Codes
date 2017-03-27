class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

#billy = Parent("Cyrus", "blue")

#print(billy.last_name)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("last name - "+self.last_name)
        print("eye_color - "+self.eye_color)
        print("number of toys - "+str(self.number_of_toys))

miley = Child("Cyrus", "blue", 5)

#print(miley.number_of_toys)
#print(miley.eye_color)
miley.show_info()
