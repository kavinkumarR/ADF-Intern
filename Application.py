class Application:
    def get(self):
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))
        self.gender=input("Enter the gender")
        self.salary=float(input("Enter the salary"))
        self.state=input("enter the state")
        self.city=input("enter the city")
    def display(self):
        print("Name:    "+self.name+"\nAge: "+str(self.age)+"\nGender:   "+self.gender+"\nSalary:   "+str(self.salary)+"\nState:   "+self.state+"\nCity:  "+self.city)

if __name__ == '__main__':
    obj=Application()
    try:
        obj.get()
    except ValueError:
        print("Invaild Input")
    else:
        obj.display()
