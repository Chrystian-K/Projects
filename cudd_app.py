
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from database import DataBase
import os
import datetime
import re
import ast
import fileinput
from tempfile import mkstemp
from shutil import move
from os import remove

cwd = os.getcwd()
files = os.listdir(cwd)  

numbers = str(list(range(-100000,100000)))

cuddy = {}

f = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt","r")
file = f.read()
with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt","r") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        cuddy[line[0]] = line[2]


class Login(GridLayout):

    def __init__(self,**kwargs):
        super(Login, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text= "ID"))
        self.logID = TextInput(multiline=False)
        self.inside.add_widget(self.logID)

        self.inside.add_widget(Label(text= "Password"))
        self.logPassword = TextInput(multiline=False)
        self.inside.add_widget(self.logPassword)

        self.add_widget(self.inside)

        self.submit = Button(text="Login", font_size=40)
        self.submit.bind(on_release=self.logInButton)
        self.add_widget(self.submit)

        self.submit = Button(text="Create an account", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)
    
    def return_button(self,instance):
        change_screen.screen_manager.current = "Create Account"
        change_screen.screen_manager.transition.direction = "up"
    
    def logInButton(self,instance):
        logID = self.logID.text
        logPassword = self.logPassword.text

        if db.validate(self.logID.text, self.logPassword.text):

            change_screen.screen_manager.current = "Main Page"
            change_screen.screen_manager.transition.direction = "left"

        else:
            pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid ID or password.'),
                  size_hint=(None, None), size=(400, 400))
            pop.open()
            self.logID.text = ""
            self.logPassword.text = ""

class MainWindow(Screen):
    current = ""

    def on_enter(self, *args):
        logID, logPassword, created = db.get_user(self.current)
        addItemName, addQuantity = cuddy.get_item(self.current)

class DataBase():

    def __init__(self,*_):
        
        self.us = None
        self.file = None
        self.load()
   
    def load(self):
        
        self.file = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/users.txt", "r")
        self.us = {}

        for line in self.file:
            user, password, email, created = line.strip().split(";") 
            self.us[user] = (password, created)

        self.file.close()

    def get_user(self, user):
        if user in self.us:
            return self.us[user]
        else:
            return -1

    def add_user(self, user, password):

        if user not in self.us:
            self.us[user.strip()] = (password.strip(), DataBase.get_date())
            self.save()
            pop = Popup(title='Notification',
                  content=Label(text='User added to Data Base'),
                  size_hint=(None, None), size=(400, 400))

            pop.open()
        else:
            pop = Popup(title='Notification',
                  content=Label(text='User already exsist'),
                  size_hint=(None, None), size=(400, 400))

            pop.open()

    def validate(self, user, password):
        if self.get_user(user) != -1:
            return self.us[user][0] == password
        else:
            return False

    def save(self):
        with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/users.txt", "w") as f:
            for user in self.us:
                f.write(user + ";" + self.us[user][0] + ";" + self.us[user][1] + ";" + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

class CreateAccount(GridLayout):
    def __init__(self,**kwargs):
        super(CreateAccount, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text= "Please provide ID"))
        self.logID = TextInput(multiline=False)
        self.inside.add_widget(self.logID)

        self.inside.add_widget(Label(text= "Please provide Password"))
        self.logPassword = TextInput(multiline=False)
        self.inside.add_widget(self.logPassword)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_release=self.logInButton)
        self.add_widget(self.submit)

        self.submit = Button(text="Go back", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)
    
    def return_button(self,instance):
        change_screen.screen_manager.current = "Login"
        change_screen.screen_manager.transition.direction = "down"
    
    def logInButton(self,instance):
        logID = self.logID.text
        logPassword = self.logPassword.text

        if self.logID.text != "" and self.logPassword.text != "":
            if self.logPassword != "":
                db.add_user(self.logID.text, self.logPassword.text)

                self.logID.text = ""
                self.logPassword.text = ""

            else:
                pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

                pop.open()
        else:
            pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

            pop.open()


class MyGrid(GridLayout):

    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text="Welcome to the cuddy, please choose one of the following options ", font_size=25))

        self.submit = Button(text="Add item", font_size=40)
        self.submit.bind(on_press=self.button_add)
        self.add_widget(self.submit)

        self.submit = Button(text="Remove Item", font_size=40)
        self.submit.bind(on_press=self.button_remove)
        self.add_widget(self.submit)

        self.submit = Button(text="Search for Item", font_size=40)
        self.submit.bind(on_press=self.button_search)
        self.add_widget(self.submit)

        self.submit = Button(text="Show Cuddy", font_size=40)
        self.submit.bind(on_press=self.button_showCuddy)
        self.add_widget(self.submit)

        self.submit = Button(text="End program", font_size=40)
        self.submit.bind(on_press=self.end)
        self.add_widget(self.submit)

    def button_add(self,instance):
        change_screen.screen_manager.current = "Add"
        change_screen.screen_manager.transition.direction = "left"

    def button_remove(self,instance):
        change_screen.screen_manager.current = "Remove"
        change_screen.screen_manager.transition.direction = "left"
    
    def button_search(self,instance):
        change_screen.screen_manager.current = "Search"
        change_screen.screen_manager.transition.direction = "left"

    def button_showCuddy(self,instance):
        change_screen.screen_manager.current = "Search All"
        change_screen.screen_manager.transition.direction = "left"

    def end(self,instance):
        quit()
    
class AddItem(GridLayout):

    def __init__(self,**kwargs):
        super(AddItem, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()    
        self.inside.cols = 2

        self.inside.add_widget(Label(text="What do you want to add "))
        self.addItemName = TextInput(multiline=False)
        self.inside.add_widget(self.addItemName)

        self.inside.add_widget(Label(text="How much (only number) "))
        self.addQuantity = TextInput(multiline=False)
        self.inside.add_widget(self.addQuantity)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_release=self.add_item_button)
        self.add_widget(self.submit)

        self.submit = Button(text="Return to Menu", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)
    
    def return_button(self,instance):
        change_screen.screen_manager.current = "Main Page"
        change_screen.screen_manager.transition.direction = "right"
    
    def add_item_button(self,instance):
        addItemName = self.addItemName.text
        addQuantity = self.addQuantity.text
        if self.addItemName.text != "":
            if self.addQuantity.text != "":
                if self.addQuantity.text in numbers:
                    if addItemName in cuddy:
                        with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt", "a+") as file:
                            if addItemName in cuddy:
                                addQuantity = int(cuddy[addItemName]) + int(addQuantity)
                                addQuantity = str(addQuantity)
                        fin = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                        fout = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "wt")
                        for line in fin:
                            fout.write( line.replace(cuddy[addItemName], addQuantity) )
                        fin.close()
                        fout.close()
                        move("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                            #file.write(self.addItemName.text +" : "+ addQuantity +"\n")
                        #file.write(file)
            
                    else:
                        cuddy[addItemName] = int(addQuantity)
                        with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt", "a+") as file:
                            file.write(self.addItemName.text +" : "+ self.addQuantity.text +"\n")
                        
                    pop = Popup(title='Item added',
                        content=Label(text=addItemName + " is in cuddy in amount of "+ addQuantity),
                        size_hint=(None, None), size=(400, 400))
                        
                    pop.open()
     
                else:
                    pop = Popup(title='Invalid format',
                        content=Label(text='Please provide number only'),
                        size_hint=(None, None), size=(400, 400))
                    pop.open()
            else:
                pop = Popup(title='Invalid quantity',
                    content=Label(text='Please provide quntity'),
                    size_hint=(None, None), size=(400, 400))
                pop.open()
        else:
            pop = Popup(title='Invalid item',
                content=Label(text='Please add item'),
                size_hint=(None, None), size=(400, 400))
            pop.open()

        self.addItemName.text = ""
        self.addQuantity.text = ""

    
class SearchItem(GridLayout):
    
    def __init__(self,**kwargs):
        super(SearchItem, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()    
        self.inside.cols = 2

        self.inside.add_widget(Label(text="What are you looking for? "))
        self.searchItem = TextInput(multiline=False)
        self.inside.add_widget(self.searchItem)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_release=self.search_item_button)
        self.add_widget(self.submit)

        self.submit = Button(text="Return to Menu", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)
    
    def return_button(self,instance):
        change_screen.screen_manager.current = "Main Page"
        change_screen.screen_manager.transition.direction = "right"

    def search_item_button(self,instance):
        
        searchItem = self.searchItem.text
        
        if self.searchItem.text in file:
            searchItemValue = cuddy[searchItem]
            #searchItemValue = searchItem(file.split()[2])
            pop = Popup(title='Item Found',
                content=Label(text=searchItem + " is in the cuddy in amount of " + searchItemValue),
                size_hint=(None, None), size=(400, 400))        
            pop.open()
        else:
            pop = Popup(title='Item Not Found',
                content=Label(text=searchItem + " is not on the list"),
                size_hint=(None, None), size=(400, 400))    
            pop.open()
      

        self.searchItem.text = ""

        
class ShowCuddy(GridLayout):
    
    def __init__(self,**kwargs):
        super(ShowCuddy, self).__init__(**kwargs)

        self.cols = 1
        
        with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt") as file:
            for f in file:
                file_content = file.read()

        self.add_widget(Label(text=str(file_content)))

        self.submit = Button(text="Return to Menu", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)

    def return_button(self,instance):
        change_screen.screen_manager.current = "Main Page"
        change_screen.screen_manager.transition.direction = "right"
    
class RemoveItem(GridLayout):
    
    def __init__(self,**kwargs):
        super(RemoveItem, self).__init__(**kwargs)
            
        self.cols = 1

        self.inside = GridLayout()    
        self.inside.cols = 2

        self.inside.add_widget(Label(text="What do you want to delete "))
        self.removeItem = TextInput(multiline=False)
        self.inside.add_widget(self.removeItem)

        self.inside.add_widget(Label(text="How much do you want to delete? "))
        self.removeItemValue = TextInput(multiline=False)
        self.inside.add_widget(self.removeItemValue)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_release=self.remove_item_button)
        self.add_widget(self.submit)

        self.submit = Button(text="Return to Menu", font_size=40)
        self.submit.bind(on_press=self.return_button)
        self.add_widget(self.submit)
    
    def return_button(self,instance):
        change_screen.screen_manager.current = "Main Page"
        change_screen.screen_manager.transition.direction = "right"

    def remove_item_button(self,instance):
    
        removeItem = self.removeItem.text
        removeItemValue = self.removeItemValue.text

        if self.removeItem.text != "":
            if self.removeItemValue.text != "":
                if self.removeItemValue.text in numbers:
                    if removeItem in cuddy:
                        if int(removeItemValue) < int(cuddy[removeItem]):
                            with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt", "a+") as file:
                                if removeItem in cuddy:
                                    removeItemValue = int(cuddy[removeItem]) - int(removeItemValue)
                                    cuddy[removeItem] = str(cuddy[removeItem])
                                    removeItemValue = str(removeItemValue)
                            fin = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                            fout = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "wt")
                            for line in fin:
                                fout.write(line.replace(cuddy[removeItem], removeItemValue) )
                            fin.close()
                            fout.close()
                            move("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                            pop = Popup(title='Item Found',
                                content=Label(text=removeItem + " removed from Cuddy in amount of " + removeItemValue),
                                size_hint=(None, None), size=(400, 400))        
                            pop.open()

                        elif int(removeItemValue) >= int(cuddy[removeItem]):
                            with open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt", "a") as file:  
                                removeItemValue = str(removeItemValue)
                            fin = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                            fout = open("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "wt")
                            for line in fin:
                                if removeItem in line:
                                    line = line.rstrip()
                                    line = line.replace(line,"")
                                fout.write(line)
                            fin.close()
                            fout.close()
                            move("C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy_temp.txt", "C:/Users/Chrystek/AppData/Local/Programs/Python/Python38-32/Python/cuddy.txt")
                            pop = Popup(title='Item Found',
                                content=Label(text=removeItem + " removed from Cuddy"),
                                size_hint=(None, None), size=(400, 400))        
                            pop.open()

                        else:
                            pop = Popup(title='Invalid Quantity',
                                content=Label(text='Not ennough amount in cuddy'),
                                size_hint=(None, None), size=(400, 400))
                            pop.open()
                    else:
                        pop = Popup(title='Invalid Item',
                            content=Label(text='Item is not in cuddy'),
                            size_hint=(None, None), size=(400, 400))
                        pop.open()
                else:
                    pop = Popup(title='Invalid format',
                        content=Label(text='Please provide number only'),
                        size_hint=(None, None), size=(400, 400))
                    pop.open()
            else:
                pop = Popup(title='Invalid item',
                    content=Label(text='Please provide quantity'),
                    size_hint=(None, None), size=(400, 400))
                pop.open()
        else:
            pop = Popup(title='Invalid item',
                content=Label(text='Please add item'),
                size_hint=(None, None), size=(400, 400))
            pop.open()
                
        self.removeItem.text = ""
        self.removeItemValue.text = "" 
        
db = DataBase()

class MyApp(App):
    def build(self):
        
        self.screen_manager = ScreenManager()

        self.login = Login()
        screen = Screen(name = "Login")
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)

        self.create_account = CreateAccount()
        screen = Screen(name = "Create Account")
        screen.add_widget(self.create_account)
        self.screen_manager.add_widget(screen)

        self.my_grid = MyGrid()
        screen = Screen(name = "Main Page")
        screen.add_widget(self.my_grid)
        self.screen_manager.add_widget(screen)

        self.add = AddItem()
        screen = Screen(name = "Add")
        screen.add_widget(self.add)
        self.screen_manager.add_widget(screen)

        self.remove_item = RemoveItem()
        screen = Screen(name = "Remove")
        screen.add_widget(self.remove_item)
        self.screen_manager.add_widget(screen)

        self.search_item = SearchItem()
        screen = Screen(name = "Search")
        screen.add_widget(self.search_item)
        self.screen_manager.add_widget(screen)

        self.searchAll_item = ShowCuddy()
        screen = Screen(name = "Search All")
        screen.add_widget(self.searchAll_item)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    change_screen = MyApp()
    change_screen.run()
