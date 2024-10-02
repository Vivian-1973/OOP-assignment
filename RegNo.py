class Student:

    def __init__ (self, name, registration_number):
        self.name = name
        self.registration_number = registration_number
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Registration_number: {self.registration_number}")

student1 = Student("Atwine Vivian", "regM23B13-001")
student1.display_details()

student2 = Student("Natukunda Ritah", "regM23B13-002")
student2.display_details()

student3 = Student("Murungi Trinity", "regM23B13-003")
student3.display_details
