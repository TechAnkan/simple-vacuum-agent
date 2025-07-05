import random 
class Environment(object):
    def __init__(self):
        self.locationcondition = {'A': 0 , 'B':0}
        self.locationcondition['A'] = random.randint(0, 1)
        self.locationcondition['B'] = random.randint(0, 1) 
    
class SimpleReflexVaccumAgent(Environment):
    def __init__(self , Environment):
        super().__init__()
        print(Environment.locationcondition)
        score = 0
        vaccumlocation = random.randint(0, 1)
        if vaccumlocation == 0: 
            print("The vaccum is in location A")
            print("Location A is dirty") if Environment.locationcondition['A'] == 1 else print("Location A is clean")
            if Environment.locationcondition['A'] == 1:
                print("Cleaning location A")
                Environment.locationcondition['A'] = 0
                score += 1
                print("The locaion A is now clean")
            print("The vaccum is now in location B")
            print("Location B is dirty") if Environment.locationcondition['B'] == 1 else print("Location B is clean")
            if Environment.locationcondition['B'] == 1: 
                print("Cleaning location B")
                Environment.locationcondition['B'] = 0
                score += 1
                print("The locaion B is now clean")
            print("Environment is clean ")
        elif vaccumlocation == 1: 
            print("The vaccum is in location B")
            print("Location B is dirty") if Environment.locationcondition['B'] == 1 else print("Location B is clean")
            if Environment.locationcondition['B'] == 1:
                print("Cleaning location B")
                Environment.locationcondition['B'] = 0
                score += 1
                print("The locaion B is now clean")
            print("The vaccum is now in location A")
            print("Location A is dirty") if Environment.locationcondition['A'] == 1 else print("Location A is clean")
            if Environment.locationcondition['A'] == 1: 
                print("Cleaning location A")
                Environment.locationcondition['A'] = 0
                score += 1
                print("The locaion A is now clean")
        print("Environment is clean")
        print(Environment.locationcondition)
        print("Performance Measure:", score)
        
theenvironment = Environment()
thevacuum = SimpleReflexVaccumAgent(theenvironment)
            