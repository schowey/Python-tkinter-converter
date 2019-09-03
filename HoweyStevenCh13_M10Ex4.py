import tkinter
#Create the class for the GUI
class TempConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #Create three frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        #The first frame will be a label and entry box
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a temperature you wanted converted to Fahrenheit:")
        self.temp_entry = tkinter.Entry (self.top_frame, width = 10)
        #Make them side by side
        self.prompt_label.pack(side = 'left')
        self.temp_entry.pack( side = 'left')
        
        self.desr_label = tkinter.Label(self.mid_frame, text = 'Your temperature in fahrenheit:')
        #Create StringVar, make blank, and then display in following label
        self.value = tkinter.StringVar()

        self.farh_label = tkinter.Label (self.mid_frame, textvariable = self.value)

        self.desr_label.pack(side = 'left')
        self.farh_label.pack (side = 'left')

        self.calc_button = tkinter.Button (self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button (self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        #Pack the buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):

        temp = float(self.temp_entry.get())

        fahrenheit = (temp * 9/5) + 32
        #fahrenheit will be made into string and stroed in StrinVar from above
        self.value.set(fahrenheit)

temp_converter = TempConverterGUI()