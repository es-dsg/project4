class ChooseQuote:
    def __init__(self):
        '''default constructor method'''
        self.list = []
        self.listName = ""
        self.number = int()
  
    def __init__(self, list, listName, number):
        '''parameterized constructor method'''
        self.list = list
        self.listName = listName
        self.number = int(number)
   
    def __str__(self):
        return f'You chose from the {self.listName} list and you got quote {self.number}'
    
    def chooseQuote(self):
        quote = self.list[self.number]
        return quote
    
    def set_list(self, list):
        self.list = list

    def set_listName(self, listName):
        self.listName = listName

    def set_number(self, number):
        self.number = number

    def get_list(self):
        return self.list
    
    def get_listName(self):
        return self.listName
    
    def get_number(self):
        return self.number