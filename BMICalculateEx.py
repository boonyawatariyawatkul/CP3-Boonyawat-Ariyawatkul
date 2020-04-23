from tkinter import *
import math
def calculateBMI(event):
    x=float(textBoxHeight.get())
    y=float(textBoxWeight.get())
    BMI = y/(math.pow(x/100,2))
    print(y/(math.pow(x/100,2)))
    if BMI > 30.0:
        labelBMI.configure(text=str(BMI)+' Obese')
    elif BMI >25.0 and BMI < 29.9:
        labelBMI.configure(text=str(BMI) +' Fat')
    elif BMI>23.0 and BMI<24.9:
        labelBMI.configure(text=str(BMI) +' Overweight')
    elif BMI > 18.6 and BMI< 22.9:
        labelBMI.configure(text=str(BMI)+" Average")
    else:
        labelBMI.configure(text=str(BMI)+ " Too Thin")
#.get() acquire from widget
#.configure export to widget
main = Tk()
labelHeight = Label(main, text="Height (cm)")
labelHeight.grid(row=0,column =0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(main, text="Weight (Kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)
button = Button(main,text='Calculate BMI',)
button.bind('<Button-1>', calculateBMI)
button.grid(row=2,column=0)
labelBMI = Label(main,text='Result')
labelBMI.grid(row=2,column=1)


main.mainloop()