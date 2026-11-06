import tkinter as tk
from ui import DayCalculatorUI

def main():
    root = tk.Tk()
    DayCalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()