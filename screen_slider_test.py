import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

cuddy = {}

class MyGrid(GridLayout):

    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols:2

        self.add_widget(Label(text="Welcome to the cuddy, please choose one ofthe following options "))
        self.name = TextInput(multiline=False)
        #self.add_widget(self.name)
        
        self.submit = Button(text="Add item", font_size=40)
        self.submit.bind(on_press=self.button_add)
        self.add_widget(self.submit)

    def button_add(self,instance):
        change_screen.screen_manager.current = "Add"
        change_screen.screen_manager.transition.direction = "left"

        
class AddItem(GridLayout):

    #change_screen.screen_manager.current = "Add Item"

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
        self.submit.bind(on_press=self.add_item_button)
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

        if addItemName in cuddy:
            cuddy[addItemName] += int(addQuantity)
        else:
            cuddy[addItemName] = int(addQuantity)

        print(addItemName, "added to cuddy in amount of", addQuantity)

        self.addItemName.text = ""
        self.addQuantity.text = ""

class MyApp(App):
    def build(self):
        #return MyGrid()
        self.screen_manager = ScreenManager()

        self.my_grid = MyGrid()
        screen = Screen(name = "Main Page")
        screen.add_widget(self.my_grid)
        self.screen_manager.add_widget(screen)

        self.add = AddItem()
        screen = Screen(name = "Add")
        screen.add_widget(self.add)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    change_screen = MyApp()
    change_screen.run()
