class School:
    def __init__(self, name, address, location):
    
        self.name = name
        self.address = address
        self.location = location

    def _init_student(self, student_name): 
            print(f"Student: {student_name}")

    def _init_address(self, address):
         print(f"Address: {address}")

    def _init_location(self, location):
         print(f"Location: {location}")

School1 = School("City Parents", "2448", "Mengo")
School2 = School("SilverSpoon", "1223", "Kansanga")


         
