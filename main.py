import tkinter as tk

def convertLength():
    try:
        value = float(entryLength.get())
        if varLength.get() == "inches to cm":
            result = value * 2.54
        elif varLength.get() == "cm to inches":
            result = value / 2.54
        resultLabel.config(text=f"Result: {result:.2f} {lengthUnits[varLength.get()]}")
    except ValueError:
        resultLabel.config(text="Invalid input")

def convertWeight():
    try:
        value = float(entryWeight.get())
        if varWeight.get() == "pounds to kg":
            result = value * 0.453592
        elif varWeight.get() == "kg to pounds":
            result = value / 0.453592
        resultLabel.config(text=f"Result: {result:.2f} {weightUnits[varWeight.get()]}")
    except ValueError:
        resultLabel.config(text="Invalid input")

root = tk.Tk()
root.title('Unit Converter')

lengthFrame = tk.Frame(root)
lengthFrame.pack(pady=10)

lengthLabel = tk.Label(lengthFrame, text="Length:")
lengthLabel.grid(row=0, column=0)

entryLength = tk.Entry(lengthFrame)
entryLength.grid(row=0, column=1)

varLength = tk.StringVar()
varLength.set("inches to cm")

lengthUnits = {
    "inches to cm": "cm",
    "cm to inches": "inches"
}

lengthDropdown = tk.OptionMenu(lengthFrame, varLength, *lengthUnits.keys())
lengthDropdown.grid(row=0, column=2)

lengthConvertButton = tk.Button(lengthFrame, text="Convert", command=convertLength)
lengthConvertButton.grid(row=0, column=3)

weightFrame = tk.Frame(root)
weightFrame.pack(pady=10)

weightLabel = tk.Label(weightFrame, text="Weight:")
weightLabel.grid(row=0, column=0)

entryWeight = tk.Entry(weightFrame)
entryWeight.grid(row=0, column=1)

varWeight = tk.StringVar()
varWeight.set("pounds to kg")

weightUnits = {
    "pounds to kg": "kg",
    "kg to pounds": "pounds"
}

weightDropdown = tk.OptionMenu(weightFrame, varWeight, *weightUnits.keys())
weightDropdown.grid(row=0, column=2)

weightConvertButton = tk.Button(weightFrame, text="Convert", command=convertWeight)
weightConvertButton.grid(row=0, column=3)

resultLabel = tk.Label(root, text='')
resultLabel.pack(pady=10)

root.mainloop()
