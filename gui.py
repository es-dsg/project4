from tkinter import *
from choosequote import *
import random
happy = ["No matter how obsessed you've been with your own vanishing, there will always be someone who still wants you whole. - Hanif Abdurraqib", "And I had a feeling I could be someone - Tracy Chapman", "Baby. I love you. And I'm going to build us a table and a whole lot of folks going to be eating off it for a long, long time to come. - James Baldwin", "The English lesson was that 'I am' is a complete sentence. - Brad Aaron Modlin", "I'm going to make it through this year if it kills me - The Mountain Goats"]
ok = ["I want an excuse to change my life. - Franny Choi", "And I said, 'do you want to see the west with me? Because love's out there and I can't leave it be.' - Ethel Cain", "Fine, then, I'll take it, the tree seems to say, a new slick leaf unfurling like a fist to an open palm, I'll take it all. - Ada Limon", "You say it like it is an apology: I thought this was a love story. You say it with hope. Timid and without conviction. - Simon Jimenez", "I'm not saying that I would have been able to [...] tell some story that would have kept him alive until the ambulance lights flooded our little corner of Ohio. - Hanif Abdurraqib"]
sad = ["Think that you haven't been kissed by a man since your father died. Think this is no moment to be strong - Michael Lasser", "...and I'd feel like if something didn't happen, if something didn't happen soon, it felt like I was just gonna... like someday, I was just gonna... - Bruce Springsteen", "There is something so repetitive about grief. First the stupid hope, then the violence of remembering. - Jackie Kay", "He grasped at me, wrestling and caressing at once, fluid and iron at once, saliva spraying from his lips and his eyes full of tears... - James Baldwin", "I need you to tell me that my life was worthwhile, and I need you to tell me that you love me. / No. I'm not going to tell you that unless you fight. - House M.D. 8x21 'Holding On'"]

class MyGUI:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Quote Picker")
        self.mainWindow.geometry("400x400")

    ############################## Frames
        self.frame1 = Frame(self.mainWindow, borderwidth = 4)
        self.frame1.grid(row = 0, column = 0)
        
    ################################### Labels'
        self.listName = Label(self.frame1, text = "How are you feeling? Type happy, ok, or sad.")
        self.listName.grid(row = 0, column = 0)

    #################################### entry
        self.enterListName = Entry(self.frame1, text = "Values", width = 20)
        self.enterListName.grid(row = 1, column = 0)


    ################################### submit button
        self.submitButton = Button(self.frame1, text = "submit", command = self.process)
        self.submitButton.grid(row = 1, column = 1)


        mainloop()


    def process(self):
        num =  random.randint(0, 4)
        if self.enterListName.get() == "happy" or self.enterListName.get() == "Happy":
            '''using default constuctor
            quoteObject = ChooseQuote()
            quoteObject.set_list(["No matter how obsessed you've been with your own vanishing, there will always be someone who still wants you whole. - Hanif Abdurraqib", "And I had a feeling I could be someone - Tracy Chapman", "Baby. I love you. And I'm going to build us a table and a whole lot of folks going to be eating off it for a long, long time to come. - James Baldwin", "The English lesson was that 'I am' is a complete sentence. - Brad Aaron Modlin", "I'm going to make it through this year if it kills me - The Mountain Goats"])
            quoteObject.set_listName("happy")
            quoteObject.set_number(num)            
            '''
            
            '''using parameterized constructor'''
            quoteObject = ChooseQuote(happy, self.enterListName.get(), num)
            print(quoteObject.chooseQuote())

        elif self.enterListName.get() == "ok" or self.enterListName.get() == "Ok" or self.enterListName.get() == "OK":
            quoteObject = ChooseQuote(ok, self.enterListName.get(), num)
            print(quoteObject.chooseQuote())

        elif self.enterListName.get() == "sad" or self.enterListName.get() == "Sad":
            quoteObject = ChooseQuote(sad, self.enterListName.get(), num)
            print(quoteObject.chooseQuote())

        else: 
            try:
                print(quoteObject.chooseQuote())
            except UnboundLocalError: 
                print("Error")