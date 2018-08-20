import Tkinter

class App:
    """ The Main Window """

    # Variables
    window = None

    # Constructor
    def __init__(self):
        # Initialize window
        self.window = Tkinter.Tk()
        self.window.title("Coin Analysis")
        # self.window.geometry('1000x591')
        self.window.resizable(width=False, height=False)
        self.window.configure(
            background="#ffffff"
        )
        # self.window.columnconfigure(50)
    
    # Create header Label
    def create_header(self):
        Tkinter.Label(
            self.window, 
            text ="Altcoins Buy/Sell Confidence",
            fg = "#ffffff",
            bg = "#428bca",
            font = "Verdana 14 bold",
            anchor="w"
        ).grid(
            row=0,
            column=0, 
            sticky='ew', 
            columnspan=50,
            ipadx=100,
            ipady=10
        )

    # Creating labels for price table
    def create_price_table_label(self, label_text):
        return Tkinter.Label(
            self.window, 
            text =label_text,
            fg = "#000000",
            bg = "#ffffff",
            font = "Verdana 10",
            anchor="w"
        )
    
    def load_price_table_label(self, label, rown = 0, columnn = 0):
        label.grid(
            row=rown,
            column=columnn, 
            sticky='ew',
            ipady = 2.5
        )
    
    def create_coin_selector_checkbox(self, checkbox_text="Text", checkbox_value="Value"):
        return Tkinter.Checkbutton(
            self.window, 
            text = checkbox_text,
            variable=checkbox_value
        )

    def load_coin_selector_checkbox(self, checkbox, rown = 0, columnn = 0):
        checkbox.grid(
            row=rown,
            column=columnn, 
            sticky='ew',
            ipady = 2.5
        )
    
    # Load the Window
    def load(self):
        self.window.mainloop()

# # -- End Class